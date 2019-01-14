#客户端代码
#客户端首先发起请求连接服务器
import socket
import time
host = '127.0.0.1'#设置ip
port = 8089 #端口
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))#连接服务端，三次握手触发
time.sleep(0.5)
s.close()