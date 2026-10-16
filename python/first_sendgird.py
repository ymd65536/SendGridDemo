
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

# 環境変数から設定を取得
api_key = os.environ["SENDGRID_API_KEY"]
from_email = os.environ["SENDGRID_FROM_EMAIL"]
to_email = os.environ["SENDGRID_TO_EMAIL"]

message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject="SendGrid SDK Test",
    plain_text_content="こちらスネーク。SendGridからの通信に成功した。"
)

try:
    sg = SendGridAPIClient(api_key=api_key)
    response = sg.send(message)

    print(f"Status: {response.status_code}")
    print(f"Message ID: {response.headers.get('X-Message-Id')}")

except HTTPError as e:
    print(f"HTTP Error: {e.status_code}")
    print(f"Details: {e.body}")
