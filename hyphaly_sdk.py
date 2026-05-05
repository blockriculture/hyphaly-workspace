"""
Hyphaly SDK Client - Agent-to-Agent Messaging

A lightweight SDK for interacting with the Hyphaly Public Broker Gateway.
Single file, no external dependencies beyond urllib.
"""

import urllib.request
import urllib.error
import json
import hashlib
import secrets
from typing import Dict, List, Optional, Any


class HyphalyClient:
    """
    Hyphaly SDK Client for agent-to-agent messaging.
    
    Usage:
        client = HyphalyClient(api_key="hyph_sk_live_...", base_url="http://localhost:8001")
        client.register_agent("my-agent", "My Agent")
        client.send_message("target-agent", {"message": "hello"})
        messages = client.poll_messages("my-agent")
        for msg in messages:
            client.ack_message(msg["id"])
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "http://localhost:8001",
        timeout: int = 30
    ):
        """
        Initialize the Hyphaly client.
        
        Args:
            api_key: API key (format: hyph_sk_live_... or hyph_sk_test_...)
            base_url: Gateway base URL (default: http://localhost:8001)
            timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._validate_api_key()
    
    def _validate_api_key(self):
        """Validate API key format."""
        if not self.api_key.startswith(("hyph_sk_live_", "hyph_sk_test_")):
            raise ValueError("Invalid API key format. Must start with hyph_sk_live_ or hyph_sk_test_")
        if len(self.api_key) != 77:  # 13 prefix + 64 hex chars
            raise ValueError("Invalid API key length. Expected 77 characters (13 prefix + 64 hex)")
    
    def _request(
        self,
        method: str,
        path: str,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> Dict:
        """
        Make an HTTP request to the gateway.
        
        Returns:
            Response dictionary
        """
        url = f"{self.base_url}{path}"
        
        # Prepare headers
        request_headers = {
            "X-Hyphaly-API-Key": self.api_key,
            "User-Agent": "HyphalySDK/1.0"
        }
        if headers:
            request_headers.update(headers)
        
        # Prepare request
        if data:
            request_headers["Content-Type"] = "application/json"
            body = json.dumps(data).encode("utf-8")
        else:
            body = None
        
        req = urllib.request.Request(
            url,
            data=body,
            headers=request_headers,
            method=method
        )
        
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                response_data = response.read().decode("utf-8")
                return json.loads(response_data) if response_data else {}
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("detail", error_body)
            except:
                error_msg = error_body
            raise Exception(f"HTTP {e.code}: {error_msg}")
        except urllib.error.URLError as e:
            raise Exception(f"Connection error: {e.reason}")
    
    # =========================================================================
    # ORGANIZATION & AUTHENTICATION
    # =========================================================================
    
    def register_org(self, name: str, email: str, password: str) -> Dict[str, Any]:
        """
        Register a new organization and get an API key.
        
        Args:
            name: Organization name
            email: Email address
            password: Password
        
        Returns:
            Dict with api_key, org_id, message
        
        Raises:
            Exception: If registration fails
        """
        # Note: This endpoint requires hyphaly_org_credentials table
        # If not available, use an existing API key instead
        try:
            return self._request(
                method="POST",
                path="/api/v1/auth/register",
                data={"name": name, "email": email, "password": password}
            )
        except Exception as e:
            # If table doesn't exist, return helpful error
            if "hyphaly_org_credentials" in str(e).lower():
                raise Exception(
                    "Registration endpoint not available. "
                    "The hyphaly_org_credentials table needs to be created. "
                    "Use an existing API key instead."
                )
            raise
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """
        Login to an existing organization and get a new API key.
        
        Args:
            email: Email address
            password: Password
        
        Returns:
            Dict with api_key, org_id, message
        
        Raises:
            Exception: If login fails
        """
        # Note: This endpoint requires hyphaly_org_credentials table
        try:
            return self._request(
                method="POST",
                path="/api/v1/auth/login",
                data={"email": email, "password": password}
            )
        except Exception as e:
            if "hyphaly_org_credentials" in str(e).lower():
                raise Exception(
                    "Login endpoint not available. "
                    "The hyphaly_org_credentials table needs to be created. "
                    "Use an existing API key instead."
                )
            raise
    
    # =========================================================================
    # AGENT MANAGEMENT
    # =========================================================================
    
    def register_agent(self, agent_id: str, name: str) -> Dict[str, Any]:
        """
        Register a new agent for this organization.
        
        Args:
            agent_id: Unique agent identifier (e.g., "my-agent")
            name: Human-readable agent name
        
        Returns:
            Dict with agent details
        
        Raises:
            Exception: If registration fails
        """
        return self._request(
            method="POST",
            path="/api/v1/agents/register",
            data={"agent_id": agent_id, "name": name}
        )
    
    def list_agents(self) -> List[Dict[str, Any]]:
        """
        List all agents for this organization.
        
        Returns:
            List of agent dictionaries
        """
        response = self._request(method="GET", path="/api/v1/agents")
        return response.get("agents", [])
    
    # =========================================================================
    # MESSAGING
    # =========================================================================
    
    def send_message(self, to_agent: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a message to another agent.
        
        Args:
            to_agent: Recipient agent ID
            payload: Message payload (JSON-serializable dict)
        
        Returns:
            Dict with message_id, status, etc.
        
        Raises:
            Exception: If sending fails
        """
        return self._request(
            method="POST",
            path="/api/v1/messages",
            data={
                "to_agent": to_agent,
                "payload": payload
            }
        )
    
    def poll_messages(self, agent_id: str, limit: int = 10) -> Dict[str, Any]:
        """
        Poll for pending messages for an agent.
        
        Note: This endpoint returns a single message (oldest pending) and a count.
        For multiple messages, call repeatedly until pending_count is 0.
        
        Args:
            agent_id: Agent ID to poll for
            limit: Maximum messages to return (default: 10) - unused in current API
        
        Returns:
            Dict with 'message' (single message or None) and 'pending_count'
        """
        response = self._request(
            method="GET",
            path=f"/api/v1/messages/{agent_id}/poll"
        )
        return response
    
    def ack_message(self, message_id: str) -> bool:
        """
        Acknowledge receipt of a message.
        
        Args:
            message_id: Message ID to acknowledge
        
        Returns:
            True if acknowledged successfully
        """
        try:
            result = self._request(
                method="POST",
                path=f"/api/v1/messages/{message_id}/ack"
            )
            # Response format: {"status": "acknowledged", "delivered_at": "..."}
            return result.get("status") == "acknowledged"
        except Exception as e:
            # If message already acknowledged, treat as success
            if "already delivered" in str(e).lower():
                return True
            raise
    
    def get_message_history(
        self,
        agent_id: str,
        limit: int = 50,
        before: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get message history for an agent.
        
        Args:
            agent_id: Agent ID
            limit: Maximum messages to return (default: 50)
            before: Cursor for pagination (message ID)
        
        Returns:
            List of message dictionaries
        """
        url = f"/api/v1/messages/{agent_id}/history?limit={limit}"
        if before:
            url += f"&before={before}"
        
        response = self._request(method="GET", path=url)
        return response.get("messages", [])


def main():
    """Example usage and basic tests."""
    print("Hyphaly SDK Client")
    print("=" * 50)
    
    # For testing, use a known API key
    API_KEY = "***REMOVED***"
    
    try:
        client = HyphalyClient(api_key=API_KEY, base_url="http://localhost:8001")
        
        # Test 1: List agents
        print("\nTest 1: List agents")
        agents = client.list_agents()
        print(f"Found {len(agents)} agents")
        for agent in agents:
            print(f"  - {agent['agent_id']}: {agent['name']}")
        
        # Test 2: Send a message
        print("\nTest 2: Send message to 'rowan'")
        result = client.send_message("rowan", {"test": "hello from sdk"})
        print(f"Message sent: {result}")
        
        # Test 3: Poll messages for 'nova'
        print("\nTest 3: Poll messages for 'nova'")
        poll_result = client.poll_messages("nova", limit=5)
        message = poll_result.get("message")
        pending_count = poll_result.get("pending_count", 0)
        print(f"Pending messages: {pending_count}")
        if message:
            msg_id = message.get("id")
            print(f"  - {msg_id}: {message.get('payload')}")
            # Acknowledge
            acked = client.ack_message(msg_id)
            print(f"    Acknowledged: {acked}")
        else:
            print("  No messages pending")
        
        # Test 4: Get message history
        print("\nTest 4: Get message history for 'rowan'")
        history = client.get_message_history("rowan", limit=3)
        print(f"Found {len(history)} messages in history")
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
