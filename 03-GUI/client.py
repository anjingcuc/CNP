import socket
import sys
import time

# 创建一个套接字
s = socket.socket()

# 尝试连接 127.0.0.1 的 6666 端口
s.connect(('127.0.0.1', 6666))

print('已连接 127.0.0.1')

message = '消息: ' + sys.argv[1]

sleep_seconds = int(sys.argv[2])
time.sleep(sleep_seconds)

# 发送消息
s.send(message.encode('utf8'))

# 接受返回消息
reply_message = s.recv(1024)

print(reply_message.decode('utf8'))

# 关闭连接
s.close()
