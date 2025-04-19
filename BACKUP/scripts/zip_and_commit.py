import os
import zipfile
import datetime
import requests
import subprocess

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
today = datetime.date.today().isoformat()
zip_dir = "BACKUP/exports"
os.makedirs(zip_dir, exist_ok=True)
zip_path = os.path.join(zip_dir, f"backup_{today}.zip")

def create_backup():
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        if os.path.exists("BACKUP/data/chat_backup.json"):
            zipf.write("BACKUP/data/chat_backup.json", arcname="chat_backup.json")
        canva_dir = "BACKUP/data/canva"
        if os.path.exists(canva_dir):
            for file in os.listdir(canva_dir):
                full = os.path.join(canva_dir, file)
                if os.path.isfile(full):
                    zipf.write(full, arcname=f"canva/{file}")

def send_discord_notification():
    if not DISCORD_WEBHOOK_URL: return
    msg = {
        "content": f"✅ Jarvis 今日備份完成：`backup_{today}.zip`"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=msg)
    except Exception as e:
        print("Discord 通知失敗", e)

def git_commit_and_push():
    subprocess.run(["git", "config", "--global", "user.email", "jarvis@auto.bot"])
    subprocess.run(["git", "config", "--global", "user.name", "Jarvis Bot"])
    subprocess.run(["git", "add", zip_path])
    subprocess.run(["git", "commit", "-m", f'📦 Daily backup: backup_{today}.zip'])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    create_backup()
    send_discord_notification()
    git_commit_and_push()
