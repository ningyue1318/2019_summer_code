import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8082))
while True:
    msg = input('输入1获取服务器时间，输入2获取字符串>>:\n').strip()
    client.send(msg.encode('utf-8'))
    receive_data = client.recv(1024)
    print(receive_data.decode('utf-8'))
client.close()