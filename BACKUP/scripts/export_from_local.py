import json
import os
import zipfile

def main():
    base_path = "BACKUP/data"
    input_file = os.path.join(base_path, "chat_backup.json")
    canva_dir = os.path.join(base_path, "canva")
    output_dir = os.path.join(base_path, "daily_backup")
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_file):
        return

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    date = data.get("date", "unknown")
    zip_filename = f"backup_{date}.zip"
    zip_path = os.path.join(output_dir, zip_filename)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file, arcname="chat_backup.json")
        if os.path.exists(canva_dir):
            for file in os.listdir(canva_dir):
                file_path = os.path.join(canva_dir, file)
                if os.path.isfile(file_path):
                    zipf.write(file_path, arcname=os.path.join("canva", file))

if __name__ == "__main__":
    main()
