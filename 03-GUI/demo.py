import socket
import threading


def client_handler(sock, addr):
  print(f'{threading.current_thread().name}: 已连接 {addr}')

  data = sock.recv(1024)

  message = data.decode('utf8')
  print(message)

  reply_message = message * 3
  sock.send(reply_message.encode('utf8'))

  sock.close()


def server():
  s = socket.socket()

  s.bind(('127.0.0.1', 6666))

  s.listen(5)

  thread_index = 0
  while True:
    print(f'{threading.current_thread().name}: 等待客户端连接...')

    client_socket, address = s.accept()

    t = threading.Thread(
        target=client_handler,
        args=(client_socket, address),
        name="ClientThread" + str(thread_index))
    t.start()

    thread_index = thread_index + 1

  s.close()


import tkinter as tk
from tkinter import ttk


window = tk.Tk()

ip_label = ttk.Label(window, text='IP:')
ip_label.grid(column=0, row=0)

port_label = ttk.Label(window, text='Port:')
port_label.grid(column=0, row=1)

send_label = ttk.Label(window, text='IP:')
send_label.grid(column=0, row=3)

window.mainloop()