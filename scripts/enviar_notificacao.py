import os
import smtplib
from email.mime.text import MIMEText

def enviar_email():
    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")

    msg = MIMEText("Pipeline finalizado com sucesso!")
    msg['Subject'] = 'CI/CD Status'
    msg['From'] = email
    msg['To'] = email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email, senha)
        server.send_message(msg)

if __name__ == "__main__":
    enviar_email()