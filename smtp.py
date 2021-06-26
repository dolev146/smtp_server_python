import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.mailgun.org', 587)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('postmaster@sandbox3fe2641695ac44f8887754cdc669e099.mailgun.org ', password)

msg = MIMEMultipart()
msg['From'] = 'brad@sandbox3fe2641695ac44f8887754cdc669e099.mailgun.org'
msg['To'] = 'dolev146@gmail.com'
msg['Subject'] = 'Just A Test'


message = 'Hello Word! This is a mail sent with Python! Kind regards! Dolev. '

msg.attach(MIMEText(message, 'plain'))

filename = 'technology-1283624_640.jpg'
# reading byte mode
attachment = open(filename, 'rb')

# payload object
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('brad@sandbox3fe2641695ac44f8887754cdc669e099.mailgun.org', 'dolev146@gmail.com', text)
server.quit()
