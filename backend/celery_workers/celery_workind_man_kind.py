from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


celery = Celery(
    'tasks',
    broker='pyamqp://admin:admin2017@localhost:5672//',  # Obratite pažnju na promene ovde
)

@celery.task
def add(user_email, sender_email, message):
    # Postavke za Gmail SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'petar.test.gecko@gmail.com'  # Unesite svoj Gmail email
    smtp_password = 'otnvdnanguixujpj'  # Unesite svoju Gmail lozinku

    # Postavljanje MIME objekta za email
    msg = MIMEMultipart()
    msg['From'] = 'petar.test.gecko@gmail.com'
    msg['To'] = 'petar.canic55@gmail.com'
    msg['Subject'] = "Testing"

    # Dodavanje teksta poruke
    msg.attach(MIMEText(message, 'plain'))

    # Povezivanje sa SMTP serverom
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Zaštita komunikacije TLS
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, 'petar.canic55@gmail.com', msg.as_string())
