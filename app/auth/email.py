# email.py
# se charge des envois par courriel et de la réinitialisation du mot de passe
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template
from app import app
from flask_babel import _

smtp_server = "smtp.gmail.com"
port = 587
sender = app.config['ADMINS']['email']
password = app.config['SECRET_KEY']

# Envoie un courriel
def send_email(subject, recipients, html_body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    msg.attach(MIMEText(html_body, 'html'))
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string().encode('utf-8'))
        server.quit()

# Envoie un courriel de réinitialisation de mot de passe
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(subject=_('[SDF] Réinitialisez votre mot de passe'), recipients=[user.email], html_body=render_template('auth/reset_password.html', title=_('Réinitialiser un mot de passe'), user=user, token=token))
