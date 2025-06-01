import time
import random
import requests

from pywebio import start_server
from pywebio.input import input, file_upload
from pywebio.output import put_text, put_image, put_markdown, clear

API_URL = "http://backend:7000/moderate"

def image_moderation_ui():
    put_markdown("## Image Moderation Interface")

    # Step 1: Get token from user
    token = input("Enter your bearer token:")

    # Step 2: Upload image
    image_file = file_upload("Upload an image", accept="image/*")

    if image_file is None:
        put_text("No file uploaded.")
        return

    put_text("Analyzing image for safety...")
    time.sleep(1)

    # The backend call.
    try:
        files = {'file': (image_file['filename'], image_file['content'])}
        headers = {"Authorization": f"Bearer {token}"}

        response = requests.post(API_URL, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            put_markdown("### Moderation Result")
            for category, items in data.items():
                put_markdown(f"**{category}:**")
                for item in items:
                    label = item.get("label", "unknown")
                    score = item.get("score", 0)
                    put_text(f"- {label}: {score:.2%}")


        else:
            put_text(f"API Error {response.status_code}: {response.text}")

    except Exception as e:
        put_text(f"Request failed: {str(e)}")

if __name__ == '__main__':
    start_server(image_moderation_ui, port=8080)
