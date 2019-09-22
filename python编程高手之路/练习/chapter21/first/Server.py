from multiprocessing import Process,Lock,Queue
import socket
import random


def service(connection,address,ticket,lock_):
    # 想客户端发送车票信息
    connection.send(str(ticket.qsize()).encode('utf-8'))

    # 接收客户端的消息
    client_choice = connection.recv(1024).decode('utf-8')
    if client_choice == '1':
        lock_.acquire()
        response = ''
        if ticket.qsize() > 0:
            client_ticket = ticket.get()
            response = "您购买了"+str(client_ticket)+"号车票"
        else:
            response = '车票已经销售完毕'
        lock_.release()
        connection.send(response.encode('utf-8'))
    else:
        connection.send('欢迎下次购买车票'.encode('utf-8'))


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8081))
    server.listen(100)
    print('----------------服务器启动------------------')

    tickets = Queue()
    lock = Lock()
    for i in range(10):
        tickets.put(i)

    while True:
        conn, client_address = server.accept()
        print(str(client_address[0])+"连接服务器:\n")
        p = Process(target=service, args=(conn, client_address,tickets,lock))
        p.start()
    server.close()