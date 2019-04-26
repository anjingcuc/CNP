import socket
import threading

import tkinter
from tkinter import ttk
from tkinter import scrolledtext

client_socket = None


def server(ip, port):
  global client_socket

  # 创建一个套接字
  s = socket.socket()

  # 绑定监听的 IP 和 端口
  # '127.0.0.1' 只允许本机连接
  # '0.0.0.0' 允许所有机器连接
  s.bind((ip, port))

  # 最大允许 5 个客户端连接，开始监听
  s.listen(5)

  thread_index = 0
  while True:
    # 阻塞模式等待客户端连接
    # 如果函数返回，说明有客户端 connect
    # 返回两个结果
    # 与客户端通信用的 client_socket
    # 客户端的地址信息 address
    print(f'{threading.current_thread().name}: 等待客户端连接...')

    client_socket, address = s.accept()

    t = threading.Thread(
        target=recv,
        name="ClientThread" + str(thread_index))
    t.start()

    thread_index = thread_index + 1

  s.close()


window = tkinter.Tk()

window.title('OO聊天')
window.resizable(False, False)

# 配置通信接口
config_frame = ttk.LabelFrame(window, text='通信配置')
config_frame.grid(column=0, row=0)

ip_label = ttk.Label(config_frame, text='IP:')
ip_label.grid(column=0, row=0)

ip = tkinter.StringVar()
ip_input = ttk.Entry(config_frame, textvariable=ip)
ip_input.grid(column=1, row=0)
ip.set('127.0.0.1')

port_label = ttk.Label(config_frame, text='Port:')
port_label.grid(column=0, row=1)

port = tkinter.IntVar()
port_input = ttk.Entry(config_frame, textvariable=port)
port_input.grid(column=1, row=1)
port.set(6666)

listen_thread = threading.Thread(
    target=server, args=(ip.get(), port.get()), name="ListenThread")

start_button = ttk.Button(
    config_frame, text='开始通信', command=listen_thread.start)
start_button.grid(column=0, row=2)

# 接受发送消息
message_frame = ttk.LabelFrame(window, text='消息窗口')
message_frame.grid(column=0, row=1)

recv_label = ttk.Label(message_frame, text='接受消息:')
recv_label.grid(column=0, row=0)

recv_message_show = scrolledtext.ScrolledText(message_frame)
recv_message_show.grid(column=0, row=1)


def recv():
  global client_socket
  global recv_message_show

  while True:
    if client_socket is None:
      import time
      time.sleep(1)
      continue

    message = client_socket.recv(1024)
    m = message.decode()
    if m == 'exit':
      break

    recv_message_show.insert(tkinter.INSERT, message.decode())


recv_thread = threading.Thread(target=recv, name="RecvThread")
recv_thread.start()

send_label = ttk.Label(message_frame, text='发送消息:')
send_label.grid(column=0, row=2)

send_message = tkinter.StringVar()
send_message_input = ttk.Entry(message_frame, textvariable=send_message)
send_message_input.grid(column=0, row=3)


def send():
  global send_message
  global client_socket

  m = send_message.get()
  if client_socket is not None and len(m) != 0:
    client_socket.send(m.encode())


send_button = ttk.Button(message_frame, text='发送消息', command=send)
send_button.grid(column=0, row=4)

window.mainloop()
