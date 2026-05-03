import os
import requests

print("🚀 Canvas bot running in cloud...")

CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")

# 🧠 DEBUG (important)
print("TOKEN LOADED:", CANVAS_TOKEN is not None)

if not CANVAS_TOKEN:
    raise Exception("❌ CANVAS_TOKEN is missing from GitHub Secrets")

headers = {
    "Authorization": f"Bearer {CANVAS_TOKEN.strip()}"
}

res = requests.get(
    "https://sycamoreschools.instructure.com/api/v1/users/self/todo",
    headers=headers
)

print("Canvas status:", res.status_code)

data = res.json()

for item in data:
    assignment = item.get("assignment", {})
    
    name = assignment.get("name")
    due = assignment.get("due_at")

    print("Task:", name)
    print("Due:", due)
    print("---")
