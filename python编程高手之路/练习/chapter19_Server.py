import socket
import datetime


def show_data_time():
    return str(datetime.datetime.now())


def show_scatter():
    return '你好'


command_list = {
    '1': show_data_time,
    '2': show_scatter
}

# 定义socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8082))
server.listen(5)
print('开始监听客户端')

while True:
    conn, client_address = server.accept()
    print('客户端:', client_address)
    while True:
        try:
            receive_msg = conn.recv(1024)
            receive_msg = receive_msg.decode('utf-8')
            if receive_msg in ['1', '2']:
                send_message = command_list[receive_msg]()
                print(send_message)
            else:
                send_message = '输入命令不存在，请重新输入：\n'
            conn.send(send_message.encode('utf-8'))
        except Exception:
            break
    conn.close()
server.close()