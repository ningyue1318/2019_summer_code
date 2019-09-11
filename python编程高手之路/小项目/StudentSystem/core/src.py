import sys
sys.path.append('..')
from entity.School import School
from entity.Course import Course
from entity.Teacher import Teacher
from db.Db import User
from core import teacher_core


def teacher():
    print("""
         1 登    录

         2 修改密码
    """)
    choice = input('请选择：\n')
    school = School()
    local_teacher = User.teacher_login(school.teacher_list)
    if choice == '1':
        if local_teacher:
            teacher_core.core()
    elif choice == '2':
        User.teacher_change_password(local_teacher,school.teacher_list)


def student():
    print('学生登录')


def operator():
    if User.login():
        school = School()
        while True:
            print("""
                1 增加教师
                2 增加课程
                3 退出登录
            """)
            choice = input('请选择:\n').strip()
            if choice == '1':
                school.add_teacher()
            elif choice == '2':
                school.add_course()
            elif choice == '3':
                print('退出管理员系统')
                break


func_dic = {
    '1': teacher,
    '2': student,
    '3': operator
}


def run():
    while True:
        print("""
        1 教师
        2 学生
        3 管理员
        """)
        choice = input('请输入你的选择：\n').strip()
        if choice in func_dic:
            func_dic[choice]()