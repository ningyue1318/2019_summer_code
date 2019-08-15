import sys
import json
import os
sys.path.append("..")
from conf.settings import DB_DIR
from log.log import log_wrapper


class DbUtils(object):
    @staticmethod
    def register(username, password):
        user_json = {
            'password': password,
            'balance': 0
        }
        # 首次注册需要检查文件是否为空，若为空则执行写操作，若不为空则先读，后写
        if os.path.getsize(DB_DIR) == 0:
            with open(DB_DIR, mode='w', encoding='utf-8') as f:
                all_user = {}
                all_user[username] = user_json
                json.dump(all_user, f)
        else:
            with open(DB_DIR, encoding='utf-8') as f:
                all_user = json.load(f)
                all_user[username] = user_json
            with open(DB_DIR, mode='w', encoding='utf-8') as f:
                json.dump(all_user, f)
        print('注册成功')

    @staticmethod
    def login(username, password):
        with open(DB_DIR, encoding='utf-8') as f:
            user_data = json.load(f)
        if user_data[username]['password'] == password:
            return user_data[username]['balance']
        else:
            return False

    @staticmethod
    def change_balance(username, balance):
        with open(DB_DIR, encoding='utf-8') as f:
            user_data = json.load(f)
            user_data[username]['balance'] = balance
        with open(DB_DIR, mode='w', encoding='utf-8') as f:
            json.dump(user_data, f)


"""
    完成用户的登录，注册，消费，充值等功能
"""


class User(object):
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password
        self.balance = 0

    """
        设置当前用户
    """
    def set_user(self, username, password):
        self.username = username
        self.password = password

    """
        完成用户的注册
        用户信息存储的json形式为 {'用户名':{'password':'密码,'balance':'余额}}
    """
    @staticmethod
    @log_wrapper
    def register():
        username = input('请输入用户名：\n')
        first_password = 'first'
        second_password = 'second'
        while first_password != second_password:
            first_password = input('请输入密码:\n')
            second_password = input('请再次输入密码\n')
            if first_password != second_password:
                print('两次密码不一致，请重新输入密码')
        DbUtils.register(username, first_password)

    """
        完成用户登录
    """
    @log_wrapper
    def login(self):
        num = 0
        while num < 3:
            username = input('请输入用户名:\n')
            password = input('请输入密码:\n')
            balance = DbUtils.login(username, password)
            if balance:
                self.username = username
                self.password = password
                self.balance = balance
                print('登录成功')
                return
            print('用户名或者账号错误，请重新输入')
            num += 1
        print('三次密码都错误，登录失败')

    """
        完成账户余额的更改，如果mode为 recharge则为充值，如果mode是consumption则为消费
    """
    @log_wrapper
    def change_balance(self, mode, money):
        if mode == 'recharge':
            self.balance = self.balance + money
            print('您充值了:' + str(money))
        elif mode == 'consumption':
            if self.balance > money:
                self.balance = self.balance - money
                print('您消费了:'+str(money))
            else:
                print('您的账户余额不足，请先充值')

        DbUtils.change_balance(self.username, self.balance)
        print('您的余额一共有:' + str(self.balance))
