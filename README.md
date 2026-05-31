📧 Email Sender
A simple Python script that sends emails via Gmail SMTP. Supports sending multiple emails at once with secure credential management using environment variables.
---
📁 Project Structure
```
email/
├── email_sender.py   # Main script
├── .env              # Your credentials (never share this)
└── README.md         # This file
```
---
⚙️ Requirements
Python 3.6+
A Gmail account with 2-Step Verification enabled
A Gmail App Password
Install Dependencies
```bash
pip install python-dotenv
```
---
🔐 Setup
Step 1 — Enable 2-Step Verification
Go to myaccount.google.com/security
Under "How you sign in to Google", click 2-Step Verification
Follow the steps to turn it ON
Step 2 — Generate a Gmail App Password
Go to myaccount.google.com/apppasswords
Under "App name", type `Email Sender` and click Create
Copy the 16-character password shown (e.g. `abcdefghijklmnop`)
Step 3 — Create a `.env` File
Create a `.env` file in the same folder as the script:
```
EMAIL_ADDRESS=you@gmail.com
EMAIL_PASSWORD=abcdefghijklmnop
```
> ⚠️ Remove all spaces from the App Password before pasting it.
---
🚀 Usage
Run the script:
```bash
python email_sender.py
```
You will be prompted:
```
Enter the number of emails to send (1–10):
```
Enter a number between 1 and 10 and press Enter.
---
🛠️ Configuration
To change the recipient, subject, or body, edit these lines at the bottom of `email_sender.py`:
```python
send_email(
    subject="Test Subject",
    body="This is a test email body.",
    to_email="recipient@example.com",  # ← change this
    count=num
)
```
---
🔒 Security Notes
Never hardcode your email or password directly in the script
Never commit your `.env` file to Git — add it to `.gitignore`:
```
  .env
  ```
Your App Password gives access to your Gmail — keep it private
Sending bulk/repeated emails may trigger Gmail's spam filters
---
❌ Common Errors
Error	Cause	Fix
`OSError: EMAIL_ADDRESS and EMAIL_PASSWORD must be set`	`.env` file not found or not loaded	Make sure `.env` is in the same folder as the script
`Authentication failed: 534 5.7.9`	Using regular Gmail password instead of App Password	Generate an App Password at myaccount.google.com/apppasswords
`Authentication failed: 535 5.7.8`	Wrong App Password	Re-generate and update your `.env` file
`Invalid input. Please enter a number.`	Typed a non-number when prompted	Enter a whole number like `1`, `2`, etc.
`Email count must be a positive integer between 1 and 10`	Number entered is out of range	Enter a number between 1 and 10
---
📌 Notes
Maximum emails per run is capped at 10 to prevent accidental spam
Gmail SMTP uses port 587 with TLS encryption
IMAP must be enabled in Gmail settings: Settings → Forwarding and POP/IMAP → Enable IMAP
---
📄 License
This project is for educational purposes only. Use responsibly.
