import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))

while True:
    client_data, client_addr = server.recvfrom(1024)
    print("{}:{}给您您发送信息：".format(client_addr[0],client_addr[1]))
    print(client_data.decode('utf-8'))
    msg = input('回复%s:%s>>>:\n'%(client_addr[0], client_addr[1]))
    server.sendto(msg.encode('utf-8'), client_addr)