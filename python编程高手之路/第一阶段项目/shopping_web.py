def show_head():
    print('-------------欢迎来到宁悦购物网站------------------------')
    print('                                                       ')
    print('      1   登录                    2  注册               ')
    print('                                                       ')
    print('-------------------------------------------------------')


"""
    功能：验证用户是否登录成功
    :returns 如果用户登录成功，返回用户名和密码组成的字符串，账户余额
             如果登录失败，返回-1,-1
"""


def login():
    with open('password.txt', encoding='utf-8') as f:
        user_dict = {}
        for item in f:
            data = item.split('|')
            user_dict[data[0] + "|" + data[1]] = data[2].replace('\n','')
        num_log = 0
        while num_log < 3:
            username = input('请输入用户名:\n')
            password = input('请输入密码:\n')
            input_user_info = username+"|"+password
            if input_user_info in user_dict.keys():
                return input_user_info, user_dict[input_user_info]
            num_log += 1
    return -1, -1


"""
    功能：完成用户信息的注册，当两次输入的密码相同时允许注册
"""


def register():
    username = input('请输入要注册的用户名:\n')
    first_password = 'first'
    second_password = 'second'
    while first_password != second_password:
        first_password = input('请输入密码:\n')
        second_password = input('请再次确认密码\n')
    r_balance = input('请输入充值金额:\n')
    with open('password.txt', mode='a', encoding='utf-8') as f:
        f.write(username+"|"+first_password+"|"+str(r_balance)+'\n')
    print('注册成功')


"""
    功能：完成用户购物，一次只能购买一件物品
         如果余额充足，直接扣款，打印购物清单，并退出系统
         余额不足，提醒用户后，退出系统
"""


def shopping():
    print('--------------请选择要购买的商品-----------------')
    print('           1 iphone   2000                      ')
    print('           2 macbook  12000                     ')
    print('           3 bike     200                       ')
    print('------------------------------------------------')
    goods = {'1': 2000,
             '2': 12000,
             '3': 200}
    goods_name = {
        '1': 'iphone',
        '2': 'macbook',
        '3': 'bike'
    }
    select_goods = input("请选择要购买的商品:\n")
    if select_goods.isnumeric() and int(select_goods) in [1, 2, 3]:
        need_money = goods[select_goods]
        if need_money < int(balance):
            print('购物成功:')
            print('您购买了：'+goods_name[select_goods]+"  花费了："+str(goods[select_goods]))
            print('您的账户余额为：'+str(int(balance) - need_money))
            user_dict = {}
            with open('password.txt', encoding='utf-8') as f:
                for item in f:
                    data = item.split('|')
                    user_dict[data[0] + "|" + data[1]] = data[2]
                user_dict[user_info] = int(balance)-need_money
            # 将数据写回到文件
            with open('password.txt', mode='w', encoding='utf-8') as f:
               f.writelines([u + "|" + str(v) + '\n' for u, v in user_dict.items()])
            return True
        else:
            print('账户余额不足，退出系统')
            return False


"""
    主程序
"""
user_info = ''
balance = ''
while True:
    show_head()
    if_login_in = input()
    # 防止非数字转化造成的异常
    if if_login_in.isnumeric():
        # 用户选择1 表示登录
        if int(if_login_in) == 1:
            (user_info, balance) = login()
            if user_info == -1:
                print('三次登录失败，退出系统')
                break
            else:
                print('登录成功')
                shopping()
                print('退出系统')
                break
        # 用户选择2, 表示注册
        elif int(if_login_in) == 2:
            register()