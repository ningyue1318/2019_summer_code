def auth():
    print('登录。。。。。')


def register():
    print('注册。。。。。')


def check():
    print('查看。。。。。')


def transfer():
    print('转账。。。。。。')


def pay():
    print('支付。。。。。。')


func_dict = {
    '1': auth,
    '2': register,
    '3': check,
    '4': transfer,
    '5': pay
}

choice = input('>>:').strip()
if choice in func_dict:
    func_dict[choice]()
else:
    print('非法操作')