import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class EmailService:
    @staticmethod
    def send_email(email, pdf_content):
        """Sends an email with a PDF attachment to the specified email address.

        Args:
            email (str): The recipient's email address.
            pdf_content (bytes): The content of the PDF file as bytes.

        Returns:
            None
        """

        # Step 1: Connect to the Google SMTP server
        smtp_server = "smtp.google.com"
        smtp_port = 587
        smtp_username = "smtp_username"
        smtp_password = "smtp_password"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Step 2: Compose the email message with the PDF attachment
        message = MIMEMultipart()
        message["From"] = smtp_username
        message["To"] = email
        message["Subject"] = "PDF Attachment"

        # Attach PDF
        pdf_attachment = MIMEApplication(pdf_content, _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename="document.pdf")
        message.attach(pdf_attachment)

        # Step 3: Send the email
        server.sendmail(smtp_username, email, message.as_string())

        # Step 4: Handle exceptions and log any errors
        server.quit()

# Example usage:
# email_service = EmailService()
# email_service.send_email("recipient@example.com", b'PDF_CONTENT_AS_BYTES')