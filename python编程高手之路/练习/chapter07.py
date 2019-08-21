from functools import wraps
from datetime import datetime
import time

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


def small_example():
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


"""
-----------------------------------------------------------------------------
第七章作业
"""


"""
第一个作业
"""
user = {'username': ''
        }


def check_login_decorator(func):

    @wraps(func)
    def check_login(*args):
        if user['username'] == '':
            login()
        func(*args)
    return check_login


def login():
    username = input('请输入用户名:\n')
    password = input('请输入密码:\n')
    if username == 'bob' and password == '123':
        user['username'] = username
        print('登录成功')


@check_login_decorator
def shopping():
    print('正在购物中')


shopping()


"""
第二个作业
"""
user = {'login_time': datetime.today()
        }


def check_login_decorator(func):

    @wraps(func)
    def check_login(*args):
        time.sleep(6)
        if (user['login_time'] - datetime.today()).seconds > 5:
            login()
        func(*args)
    return check_login


def login():
    username = input('请输入用户名:\n')
    password = input('请输入密码:\n')
    if username == 'bob' and password == '123':
        user['login_time'] = datetime.today()
        print('登录成功')


@check_login_decorator
def shopping():
    print('正在购物中')


shopping()


"""
第三个作业
"""


def record_time_decorator(filename):
    def record_time_(func):
        @wraps(func)
        def record_the_time(*args):
            record_item = func.__name__ +" "+str(datetime.today())+"\n"
            with open(filename, mode='a', encoding='utf-8') as f:
                f.write(record_item)
            print('记录完成')
            func(*args)

        return record_the_time
    return record_time_


@record_time_decorator(filename='log.txt')
def function_test():
    print('装饰器函数测试')


@record_time_decorator(filename='log.txt')
def add_number(a, b):
    print(a+b)


add_number(100, 100)
function_test()
