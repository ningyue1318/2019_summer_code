import sys
sys.path.append('..')
from db.Db import UserDb


def choose_class():
    course_list = UserDb.load_from_memory('Course')
    print(course_list)


def scoring():
    print('打分')


func_dic = {
    '1': choose_class,
    '2': scoring
}


def core():
    while True:
        print("""
        1 选择课程
        
        2 登记成绩
        """)
        choice = input("请选择：\n")
        if choice in ['1', '2']:
            func_dic[choice]()

core()
