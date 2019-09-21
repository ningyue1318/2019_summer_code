import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8086))
check_code = client.recv(1024)
print('服务器发送的验证码为:'+check_code.decode('utf-8'))
input_check_code = input('请输入验证码：\n').strip()
client.send(input_check_code.encode('utf-8'))
rec = client.recv(1024)
print(rec.decode('utf-8'))