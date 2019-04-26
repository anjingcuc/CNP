import socket
import threading
import time


def clinet_handler(sock, addr):
  print(f'{threading.current_thread().name}: 已连接 {addr}.')

  data = sock.recv(1024)

  message = data.decode('utf8')

  print(f'{threading.current_thread().name}: 数据处理中: {message}')
  time.sleep(20)
  print(f'{threading.current_thread().name}: 数据处理完成。')

  reply_message = message * 3
  sock.send(reply_message.encode('utf8'))

  sock.close()


# 创建一个套接字
s = socket.socket()

# 绑定监听的 IP 和 端口
# '127.0.0.1' 只允许本机连接
# '0.0.0.0' 允许所有机器连接
s.bind(('127.0.0.1', 6666))

# 最大允许 5 个客户端连接，开始监听
s.listen(5)

thread_index = 0
while True:
  # 阻塞模式等待客户端连接
  # 如果函数返回，说明有客户端 connect
  # 返回两个结果
  # 与客户端通信用的 client_socket
  # 客户端的地址信息 address
  print(f'{threading.current_thread().name}: 开始等待连接...')

  client_socket, address = s.accept()

  t = threading.Thread(
      target=clinet_handler,
      args=(client_socket, address),
      name=f'ClientThread_{thread_index}')
  t.start()

  thread_index = thread_index + 1

s.close()