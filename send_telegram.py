#!/usr/bin/env python3
import sys, urllib.request, json

BOT_TOKEN = "8787658612:AAHDcATz97e12ATv1kEA-Av-br5yg4BsxsM"
CHAT_ID = "705078761"

def send(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = json.dumps({"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            result = json.load(r)
            if result.get("ok"):
                print(f"[send_telegram] delivered (message_id={result['result']['message_id']}")
                return True
            else:
                print(f"[send_telegram] API error: {result}")
                return False
    except Exception as e:
        print(f"[send_telegram] failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_telegram.py 'message'")
        sys.exit(1)
    success = send(" ".join(sys.argv[1:]))
    sys.exit(0 if success else 1)
