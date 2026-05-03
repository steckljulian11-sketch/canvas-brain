import requests

print("🚀 Canvas bot starting...")

BASE_URL = "https://sycamoreschools.instructure.com"

# TEMP TEST (no tokens yet)
r = requests.get("https://api.github.com")

print("GitHub test status:", r.status_code)
