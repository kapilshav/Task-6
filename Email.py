import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='kundan is logging in'
msg['From']='kundan Laptop'
msg['To']='gurjarkundan12345@gmail.com'
msg.set_content('kundan is logging in..!')
server=smtplib.SMTP_SSL("kp.gmail.com",465)
server.login('gurjarkundan12345@gmail.com','**********')
server.send_message(msg)
server.quit()
