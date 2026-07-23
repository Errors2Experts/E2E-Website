import os
import base64
import mimetypes
import requests

BREVO_URL = "https://api.brevo.com/v3/smtp/email"


def send_brevo_email(to_email, subject, html, attachment_path=None):
    api_key = os.getenv("BREVO_API_KEY")

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json",
    }

    payload = {
        "sender": {
            "name": "Errors2Experts",
            "email": "errors2experts.official@gmail.com"
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "htmlContent": html,
    }

    # -------------------------------
    # Attach file if provided
    # -------------------------------
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        mime_type = mimetypes.guess_type(attachment_path)[0]

        payload["attachment"] = [
            {
                "content": encoded,
                "name": os.path.basename(attachment_path),
                "type": mime_type or "application/octet-stream",
            }
        ]

    response = requests.post(
        BREVO_URL,
        json=payload,
        headers=headers,
        timeout=20,
    )

    print(response.status_code)
    print(response.text)

    response.raise_for_status()