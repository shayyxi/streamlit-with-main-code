import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self, app_password, email_to, email_from='inbox@shazitechdev.com', smtp_server='mail.privateemail.com', smtp_port=587):
        """
        Initialize the email sender with the login credentials.

        :param email_from: Your email address (e.g., 'your_email@gmail.com')
        :param password: Your email password (or App Password if 2FA is enabled)
        :param smtp_server: SMTP server address (default is Gmail's server)
        :param smtp_port: SMTP port (default is 587 for TLS)
        """
        self.email_from = email_from
        self.email_to = email_to
        self.app_password = app_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject, body, pdf_path):
        """
        Sends an email with a PDF attachment.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body text of the email (plain text or HTML)
        :param pdf_path: Path to the PDF file to be attached
        """
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = self.email_from
        msg['To'] = self.email_to
        msg['Subject'] = subject

        # Convert the body to MIMEText
        msg.attach(MIMEText(body, 'plain'))  # 'plain' for plain text, 'html' for HTML emails

        # Open the PDF file in binary mode and attach it
        with open(pdf_path, 'rb') as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
        #
        # # Add header with the filename of the attachment
        attach.add_header('Content-Disposition', 'attachment', filename=str(pdf_path))
        #
        # # Attach the part to the message
        msg.attach(attach)

        # Try sending the email
        try:
            # Connect to the SMTP server and send the email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure connection
            server.login(self.email_from, self.app_password)  # Use app password for login
            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")