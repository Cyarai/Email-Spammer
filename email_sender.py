
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()

def send_email(subject, body, to_email, count=1):
    from_email = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')

    if not from_email or not password:
        raise EnvironmentError(
            "EMAIL_ADDRESS and EMAIL_PASSWORD must be set in your .env file.\n"
            "Create a .env file in the same folder with:\n"
            "  EMAIL_ADDRESS=you@gmail.com\n"
            "  EMAIL_PASSWORD=your_16_char_app_password"
        )

    if not isinstance(count, int) or count < 1 or count > 10:
        raise ValueError("Email count must be a positive integer between 1 and 10.")

    msg = EmailMessage()
    msg['From'] = f'Sample Account <{from_email}>'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            for _ in range(count):
                server.send_message(msg)
        print(f"{count} email(s) sent successfully to {to_email}.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed: {e.smtp_code} - {e.smtp_error}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        num = int(input("Enter the number of emails to send (1–10): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)

    send_email(
        subject="Test Subject",
        body="This is a test email body.",
        to_email="recipient@example.com",
        count=num
    )