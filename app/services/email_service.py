def send_email(
        to: str,
        subject: str,
        body: str
):

    return {
        "success": True,

        "recipient": to,

        "subject": subject,

        "message": "Email sent successfully."
    }