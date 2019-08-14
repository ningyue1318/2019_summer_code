import sys
sys.path.append('..')
from lib.common import User
from conf.settings import goods

""""
    信用卡管理程序的主程序
"""


def start_view():
    print('-----------欢迎来到宁悦信用卡管理程序---------------')
    print('                                                  ')
    print('                   1  登录                        ')
    print('                                                  ')
    print('                   2  注册                        ')
    print('                                                  ')
    print('--------------------------------------------------')


def first_menu():
    print('--------------------------------------------------')
    print('                                                  ')
    print('                   1 充值                         ')
    print('                                                  ')
    print('                   2 购物                         ')
    print('                                                  ')
    print('                   3 退出                         ')
    print('                                                  ')
    print('--------------------------------------------------')


def show_goods():
    print(format('商品名', '<20') + format('价钱', '<20'))
    print('-----------------------------')
    for name, money in goods.items():
        print(format(name, '<20') + format(money, '<20'))


if __name__ == '__main__':
    if_quit = True
    current_user = User()
    while if_quit:
        """
            首次登录流程，登录界面->充值界面
            完成一次充值或者登录后，显示一级菜单
        """
        if current_user.username == '':
            start_view()
            choice = input('请选择：\n')
            # 1代表登录，2代表注册
            if choice == '1':
                current_user.login()
                first_menu()
                choice = input('请选择:\n')

                # 1代表充值 2代表购物 3表示退出
                if choice == '1':
                    recharge_money = input('请输入充值金额:\n')
                    current_user.change_balance('recharge', int(recharge_money))
                elif choice == '2':
                    show_goods()
                    choice_good = input('请选择要购买的货物：\n')
                    current_user.change_balance('consumption', goods[choice_good])
                elif choice == '3':
                    if_quit = False

            elif choice == '2':
                User.register()
        else:
            first_menu()
            choice = input('请选择:\n')
            # 1代表充值 2代表购物
            if choice == '1':
                recharge_money = input('请输入充值金额:\n')
                current_user.change_balance('recharge', int(recharge_money))
            elif choice == '2':
                show_goods()
                choice_good = input('请选择要购买的货物：\n')
                current_user.change_balance('consumption', goods[choice_good])
            elif choice == '3':
                if_quit = False
