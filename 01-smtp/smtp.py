import smtplib
from email.mime.text import MIMEText

# 等待用户输入，用户名，密码，收件人
from_address = input('From: ')
to_address = input('To: ')
password = input('Password: ')

# 
server = smtplib.SMTP('smtp.qq.com', 25)  # SMTP协议默认端口是25
#
server.set_debuglevel(1)
#
server.login(from_address, password)

msg = MIMEText('你好，我在学 Python 网络编程...', 'plain', 'utf-8')

server.sendmail(from_address, [to_address], msg.as_string())

server.quit()