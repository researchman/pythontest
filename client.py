import socket
import sys

#建立客户端socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

#获得主机名
host = socket.gethostname();

#获得端口号
port = 8086;

#连接服务器
client.connect((host,port));

#接收消息
msg = client.recv(1024);

#关闭连接
client.close();

#输出接收到的消息
print(msg.decode("utf-8"));