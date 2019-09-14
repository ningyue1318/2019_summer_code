import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('请输入发送给(127.0.0.1:8080的消息:)>>>:\n').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
    res, server_addr = client.recvfrom(1024)
    print('{}:{}回复消息:\n{}'.format(server_addr[0], server_addr[1], res.decode('utf-8')))