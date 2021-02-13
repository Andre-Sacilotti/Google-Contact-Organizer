import requests

a = requests.get(
    "http://127.0.0.1:5000/api/contact/",
    headers={
        "authorization-code": """ya29.a0AfH6SMA-6tQNjPGY2uPMIylvq4zv79mN4C4GQD-AFoZma3zxHVAgYyN-_NZjhM-jeetsuDMeHByT23S9tzlEKC4f4HWIbOIPFJt0AnvH3faIAQzRnJCgApdyD81yNshRz5nqa2ZxR9tLyz1nEoh3s2UtZPTqI8ZJU1IccZu1dqki"""
    },
)

print(a.text)
