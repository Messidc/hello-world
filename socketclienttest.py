import socket
import threading
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 19999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print('recv:',s.recv(1024).decode('utf-8'))
q=input('请输入:')
print(q,'sended')
while q and q!='exit':
    s.send(q.encode('utf-8'))
    print('recv:' , s.recv(1024).decode('utf-8'))
    q=input('请输入:')
    print(q,'sended')
s.send(b'exit')
s.close()