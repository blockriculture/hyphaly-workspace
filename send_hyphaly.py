#!/usr/bin/env python3
"""
Send messages to the local Hyphaly broker.

Usage:
    send_hyphaly.py <sender_id> <target_agent_id> <message_content> [--message-type TYPE]
    or import and call send_to_broker()

POSTs to http://localhost:8000/messages using the broker envelope format.
"""

import sys
import argparse
import json
import uuid
import requests
from typing import Optional, Dict, Any

# Default broker URL
BROKER_URL = "http://localhost:8000"


def send_to_broker(
    sender_id: str,
    target_agent_id: str,
    message_content: str,
    message_type: Optional[str] = None,
    trace_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Send a message to the Hyphaly broker.
    
    Args:
        sender_id: Sender agent ID
        target_agent_id: Target agent ID
        message_content: Message payload
        message_type: Optional message type (ignored by broker, may be used by client)
        trace_id: Optional trace ID (auto-generated if None)
    
    Returns:
        Response dict from broker (should contain message_id)
    """
    if trace_id is None:
        trace_id = str(uuid.uuid4())
    
    # Build request payload matching broker's MessageIn schema
    payload = {
        "from_agent": sender_id,
        "to_agent": target_agent_id,
        "payload": message_content,
        "trace_id": trace_id
    }
    
    # Add message_type as extra field (broker will ignore it)
    if message_type is not None:
        payload["message_type"] = message_type
    
    # POST to broker
    try:
        response = requests.post(
            f"{BROKER_URL}/messages/{target_agent_id}",
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to broker: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Send a message to the Hyphaly broker")
    parser.add_argument("sender_id", help="Sender agent ID")
    parser.add_argument("target_agent_id", help="Target agent ID")
    parser.add_argument("message_content", help="Message content")
    parser.add_argument("--message-type", "-t", help="Optional message type")
    parser.add_argument("--trace-id", "-r", help="Optional trace ID (auto-generated if not provided)")
    
    args = parser.parse_args()
    
    try:
        result = send_to_broker(
            sender_id=args.sender_id,
            target_agent_id=args.target_agent_id,
            message_content=args.message_content,
            message_type=args.message_type,
            trace_id=args.trace_id
        )
        print(f"Message sent successfully: {json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()