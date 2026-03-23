import sys
import json

# Fix stdout encoding for Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

import urllib.request
from datetime import datetime
import os
import subprocess

def get_prompt_author():
    # Always use Duypkk as requested
    return "Duypkk"

if len(sys.argv) < 5:
    print("Usage: python3 track_prompt.py <prompt> <workflow_steps> <result_output> <status>")
    sys.exit(1)

raw_prompt = sys.argv[1]
workflow_steps = sys.argv[2]
result_output = sys.argv[3]
status = sys.argv[4]

# Resolve base_dir dynamically based on script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
webhook_file = os.path.join(base_dir, "config", "webhook.txt")
prompt_hist_file = os.path.join(base_dir, "knowledge", "prompt_history.md")
activity_hist_file = os.path.join(base_dir, "knowledge", "activity_history.md")

# Ensure directories exist
knowledge_dir = os.path.join(base_dir, "knowledge")
results_dir = os.path.join(base_dir, "results")
os.makedirs(knowledge_dir, exist_ok=True)
os.makedirs(results_dir, exist_ok=True)

# Ensure log files exist
if not os.path.exists(prompt_hist_file):
    with open(prompt_hist_file, "w", encoding="utf-8") as f:
        f.write("# Prompt History\n")

if not os.path.exists(activity_hist_file):
    with open(activity_hist_file, "w", encoding="utf-8") as f:
        f.write("# Activity History\n")

with open(webhook_file, "r", encoding="utf-8") as f:
    webhook_url = f.read().strip()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
prompt_author = get_prompt_author()

# Append to Prompt History
with open(prompt_hist_file, "a", encoding="utf-8") as f:
    f.write(f"\n## [{current_time}]\n**Prompt Author**: {prompt_author}\n**Prompt Content**: {raw_prompt}\n**Workflow Steps**: \n{workflow_steps}\n**Result / Output**: \n{result_output}\n")

# Append to Activity History
with open(activity_hist_file, "a", encoding="utf-8") as f:
    f.write(f"\n## [{current_time}]\n**Prompt Author**: {prompt_author}\n**Prompt Content**: {raw_prompt}\n**Workflow Steps**: \n{workflow_steps}\n**Result / Output**: \n{result_output}\n")

# Send to Google Chat only if completed or error/failed
# Always send to Google Chat
payload = {
    "text": f"🚀 *[AI TASK REPORT]*\n\nPrompt Author: {prompt_author}\nPrompt: {raw_prompt}\n\nStatus: {status}\n\nSummary/Output:\n{result_output}\n\nTimestamp: {current_time}"
}

req = urllib.request.Request(webhook_url, method="POST")
req.add_header('Content-Type', 'application/json')
data = json.dumps(payload).encode('utf-8')

try:
    with urllib.request.urlopen(req, data=data) as response:
        print("Success:", response.read().decode('utf-8'))
except Exception as e:
    print(f"Error sending to Google Chat: {e}")

