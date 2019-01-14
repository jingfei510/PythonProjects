#服务器端代码
import socket
host = '127.0.0.1'#设置ip
port = 8088 #端口
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务端
s.bind((host,port))
s.listen(5)
print("服务端已开启,等待客户端连接...")
conn, addr = s.accept()#连接
print("客户端已连接...\n")