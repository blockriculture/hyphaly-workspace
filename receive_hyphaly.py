#!/usr/bin/env python3
"""
Receive messages from Hyphaly broker and process them.
"""

import json
import argparse
import urllib.request
from typing import Dict, List, Any, Optional

# Default broker URL
BROKER_URL = "http://localhost:8000"


def receive_and_process(agent_id: str) -> Dict[str, Any]:
    """
    Receive and process all pending messages for the given agent.
    
    Args:
        agent_id: The agent identifier
    
    Returns:
        Dict with status, messages_processed, and payloads list
    """
    processed = 0
    payloads = []
    
    while True:
        # Poll for a pending message
        try:
            req = urllib.request.Request(f"{BROKER_URL}/messages/{agent_id}")
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status != 200:
                    return {
                        'status': 'error',
                        'error': f'HTTP {response.status}',
                        'messages_processed': processed,
                        'payloads': payloads
                    }
                
                data = json.loads(response.read().decode())
                message = data.get('message')
                count_pending = data.get('count_pending', 0)
                
                if message is None or count_pending == 0:
                    # No more messages
                    break
                
                # Print the payload so the agent can read and act on it
                payload = message.get('payload', '')
                print(f"[{agent_id}] Received: {payload}")
                payloads.append(payload)
                
                # Acknowledge the message
                message_id = message.get('id')
                ack_url = f"{BROKER_URL}/messages/{message_id}/ack"
                ack_req = urllib.request.Request(
                    ack_url,
                    data=b'',
                    headers={'Content-Type': 'application/json'},
                    method='POST'
                )
                try:
                    with urllib.request.urlopen(ack_req, timeout=10) as ack_response:
                        if ack_response.status == 200:
                            processed += 1
                            print(f"[{agent_id}] Acknowledged message {message_id}")
                        else:
                            print(f"[{agent_id}] Warning: ack failed with HTTP {ack_response.status}")
                except Exception as e:
                    print(f"[{agent_id}] Error acknowledging message {message_id}: {e}")
                
                # Continue loop to process next message
                
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # No messages
                break
            return {
                'status': 'error',
                'error': f'HTTP {e.code} {e.reason}',
                'messages_processed': processed,
                'payloads': payloads
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'messages_processed': processed,
                'payloads': payloads
            }
    
    return {
        'status': 'ok',
        'messages_processed': processed,
        'payloads': payloads
    }


def main():
    parser = argparse.ArgumentParser(description='Receive and process messages from Hyphaly broker')
    parser.add_argument('--agent', required=True, help='Agent ID to receive messages for')
    args = parser.parse_args()
    
    result = receive_and_process(args.agent)
    print(f"Result: {json.dumps(result, indent=2)}")
    
    if result['status'] == 'ok':
        if result['messages_processed'] == 0:
            print("No pending messages.")
        else:
            print(f"Processed {result['messages_processed']} message(s).")
    else:
        print(f"Error: {result.get('error')}")
        exit(1)


if __name__ == "__main__":
    main()