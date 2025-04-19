import requests
import os

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(message):
    if not DISCORD_WEBHOOK_URL:
        return
    data = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

if __name__ == "__main__":
    send_discord_message("✅ Jarvis 系統已部署完成並運行中")
