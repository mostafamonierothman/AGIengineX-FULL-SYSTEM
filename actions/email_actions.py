# actions/email_actions.py

from debug.debug_logger import log_info

# In real system → use actual email API (ex: SMTP, SendGrid, Mailgun, etc)
# This is placeholder to show where ACTION happens!

def send_email(recipient_email, subject, body):
    log_info(f"📧 ACTION: Sending email to {recipient_email} | Subject: {subject} | Body: {body}")

    # Simulate success
    result = {
        "recipient": recipient_email,
        "subject": subject,
        "status": "sent",
        "timestamp": "now()"
    }

    return result
