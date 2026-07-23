import os
import requests


BREVO_URL = "https://api.brevo.com/v3/smtp/email"


def send_brevo_email(to_email, subject, html):

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

    response = requests.post(
        BREVO_URL,
        json=payload,
        headers=headers,
        timeout=20
    )

    print(response.status_code)
    print(response.text)

    response.raise_for_status()