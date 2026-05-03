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
    "https://sycamoreschools.instructure.com/api/v1/users/self/courses",
    headers=headers
)

print("Canvas status:", res.status_code)

try:
    data = res.json()
    print("Number of courses:", len(data))
except Exception as e:
    print("JSON error:", e)
    print("Raw response:", res.text)
