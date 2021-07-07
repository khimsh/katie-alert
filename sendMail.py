
import smtplib


def send_mail(email_address: str, email_password: str):

    with smtplib.SMTP('smtp.gmail.com:587') as smtp:
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_address, email_password)

        subject = 'Katie\'s IMDB Credits Update'
        body = 'There\'s been changes!'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email_address, email_address, msg)
