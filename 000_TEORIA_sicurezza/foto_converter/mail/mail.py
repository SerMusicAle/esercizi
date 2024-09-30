import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, body, password):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
sender_email = "fullstack2324@gmail.com"  # Replace with your email
receiver_email = "francorcr@hotmail.it"  # Replace with the recipient's email
subject = "Test Email"
body = "a professo, le è arrivata la mail?"
password = "Full.stack@2324"  # Replace with your app-specific password

send_email(sender_email, receiver_email, subject, body, password)