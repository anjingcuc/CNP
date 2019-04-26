import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address = input('From: ')
to_address = input('To: ')
password = input('Password: ')

server = smtplib.SMTP('smtp.qq.com', 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_address, password)

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = 'Hello, world.'

# 邮件正文是MIMEText:
msg.attach(MIMEText('你好，请查收附件...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.jpg', 'rb') as f:
  # 设置附件的MIME和文件名，这里是png类型:
  mime = MIMEBase('image', 'jpg', filename='test.jpg')
  # 加上必要的头信息:
  mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
  # 把附件的内容读进来:
  mime.set_payload(f.read())

  # 用Base64编码:
  encoders.encode_base64(mime)

  # 添加到MIMEMultipart:
  msg.attach(mime)

server.sendmail(from_address, [to_address], msg.as_string())

server.quit()