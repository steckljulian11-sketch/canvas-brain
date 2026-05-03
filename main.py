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
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

tasks_text = ""

for item in data:
    assignment = item.get("assignment", {})
    name = assignment.get("name")
    due = assignment.get("due_at")

    tasks_text += f"- {name} (due {due})\n"

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": f"""
You are a student planner AI.

Organize these tasks into:
1. Today priorities
2. This week plan
3. What is urgent
4. Simple schedule

Tasks:
{tasks_text}
"""
        }
    ]
)

print("\n🧠 AI PLAN:\n")
print(message.content[0].text)
