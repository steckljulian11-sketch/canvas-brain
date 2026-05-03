import os
import requests

print("🚀 Canvas bot running in cloud...")

CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")

headers = {
    "Authorization": f"Bearer {CANVAS_TOKEN}"
}

res = requests.get(
    "https://sycamoreschools.instructure.com/api/v1/users/self/courses",
    headers=headers
)

print("Canvas status:", res.status_code)

data = res.json()

print("Number of courses:", len(data))
