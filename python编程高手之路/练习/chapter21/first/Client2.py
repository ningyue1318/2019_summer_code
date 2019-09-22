import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8081))

# 查询车票信息
ticket_num = client.recv(1024)
ticket_num = ticket_num.decode('utf-8')

print('现在还有{}张车票'.format(ticket_num))
if int(ticket_num)>0:
    choice = input('请选择是否购买车票：1 购买，2 不购买:\n')
    if choice in ['1', '2']:
        client.send(choice.encode('utf-8'))
    server_response = client.recv(1024).decode('utf-8')
    print(server_response)