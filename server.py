import socket
import sys

#创建socket对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

host = socket.gethostname();
print(host);

port = 8086;

#绑定端口
server.bind((host,port));

#设置最大连接数，超过后排队
server.listen(5);

while True:
    client_socket,addr = server.accept();

    print("连接地址：%s"%str(addr));

    msg = "欢迎访问菜鸟教程.\r\n";
    client_socket.send(msg.encode("utf-8"));
    client_socket.close();