from multiprocessing import Process,Queue
import socket
import random


def service(connection, address):
    while True:
        try:
            check_code = ''
            for i in range(4):
                check_code += str(random.randint(1, 26))
            connection.send(check_code.encode('utf-8'))
            rec = connection.recv(1024)
            print('从'+str(address[1])+"收到的验证码："+rec.decode('utf-8'))
            if rec.decode('utf-8') == check_code:
                connection.send('注册成功'.encode('utf-8'))
            else:
                connection.send('验证码不正确'.encode('utf-8'))
            connection.close()
        except Exception:
            break


if __name__ == '__main__':
    print('----------服务器端启动------------')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8086))
    server.listen(5)
    while True:
        conn, client_address = server.accept()
        print(str(client_address[1]) + "请求发送验证码")
        p = Process(target=service, args=(conn, client_address))
        p.start()
    server.close()