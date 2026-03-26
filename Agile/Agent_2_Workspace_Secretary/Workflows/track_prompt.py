import json
import os
import sys
import urllib.request
from datetime import datetime


if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def get_prompt_author() -> str:
    return "Duypkk"


def author_to_folder(author: str) -> str:
    return author.strip().replace(" ", "_")


def ensure_file(path: str, title: str) -> None:
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8-sig") as file:
            file.write(f"# {title}\n")


def append_text(path: str, content: str) -> None:
    with open(path, "a", encoding="utf-8-sig") as file:
        file.write(content)


def main() -> int:
    if len(sys.argv) < 5:
        print(
            "Usage: python track_prompt.py <raw_prompt> <activity_summary> <full_answer> <status> [folder]"
        )
        return 1

    raw_prompt = sys.argv[1]
    activity_summary = sys.argv[2]
    full_answer = sys.argv[3]
    status = sys.argv[4]
    folder = sys.argv[5] if len(sys.argv) >= 6 else "Agile"

    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    logs_dir = os.path.join(base_dir, "Logs")
    webhook_file = os.path.join(base_dir, "config", "webhook.txt")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prompt_author = get_prompt_author()
    author_folder = author_to_folder(prompt_author)
    author_logs_dir = os.path.join(logs_dir, author_folder)
    prompt_hist_file = os.path.join(author_logs_dir, "prompt_history.md")
    activity_hist_file = os.path.join(author_logs_dir, "activity_history.md")

    os.makedirs(author_logs_dir, exist_ok=True)
    ensure_file(prompt_hist_file, "Prompt History")
    ensure_file(activity_hist_file, "Activity History")

    prompt_entry = (
        f"\n## [{current_time}]\n"
        f"**Prompt Author**: {prompt_author}\n"
        f"**Prompt Content**: {raw_prompt}\n"
        f"**Status**: {status}\n"
    )

    activity_entry = (
        f"\n## [{current_time}]\n"
        f"**Prompt Author**: {prompt_author}\n"
        f"**Folder**: {folder}\n"
        f"**Prompt Content**: {raw_prompt}\n"
        f"**Activity Summary**:\n{activity_summary}\n"
        f"**Result / Output**:\n{full_answer}\n"
        f"**Status**: {status}\n"
    )

    append_text(prompt_hist_file, prompt_entry)
    append_text(activity_hist_file, activity_entry)

    if os.path.exists(webhook_file):
        with open(webhook_file, "r", encoding="utf-8") as file:
            webhook_url = file.read().strip()

        if webhook_url:
            payload = {
                "text": (
                    "Theo dõi prompt mới trong workspace\n\n"
                    f"Prompt Author: {prompt_author}\n"
                    f"Folder: {folder}\n"
                    f"Prompt: {raw_prompt}\n\n"
                    f"Activity Summary:\n{activity_summary}\n\n"
                    f"Status: {status}\n"
                    f"Timestamp: {current_time}"
                )
            }

            request = urllib.request.Request(webhook_url, method="POST")
            request.add_header("Content-Type", "application/json")
            data = json.dumps(payload).encode("utf-8")

            try:
                with urllib.request.urlopen(request, data=data):
                    pass
            except Exception as exc:
                print(f"Error sending to Google Chat: {exc}")

    print(f"AUTHOR_LOG_DIR={author_logs_dir}")
    print(f"PROMPT_LOG={prompt_hist_file}")
    print(f"ACTIVITY_LOG={activity_hist_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
