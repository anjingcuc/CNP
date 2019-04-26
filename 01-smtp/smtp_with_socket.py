import socket

s = socket.socket()

s.connect(('smtp.qq.com', 25))

message = s.recv(1024)

print(message.decode('utf8'))

s.send('EHLO qq.com\r\n'.encode('utf8'))

message = s.recv(1024)

print(message.decode('utf8'))