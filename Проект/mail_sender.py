import os
import smtplib
from email.mime.text import MIMEText
from random import randrange


def send_mail(email, rec):
    addr_from = os.getenv("FROM")
    password = os.getenv('PASSWORD')
    code = randrange(100000, 1000000)

    body = f"Здравствуйте! Код подтверждения регистрации {email} - {code}."
    if rec:
        body = f"Здравствуйте! Код восстановления пароля {email} - {code}."
    msg = MIMEText(body)
    msg['Subject'] = 'Код активации'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(addr_from, password)
    server.sendmail(addr_from, email, msg.as_string())