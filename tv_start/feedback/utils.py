import smtplib
from email.mime.text import MIMEText
from django.conf import settings

def send_feedback_email(data):
    message = f'Name: {data["name"]}\nMessage: {data["message"]}\nPhone: {data["phone"]}\nEmail: {data["email"]}'
    msg = MIMEText(message)
    msg['Subject'] = 'New Feedback'
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = data['email']
    s = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    s.starttls()
    s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    s.send_message(msg)
    s.quit()