import sys
sys.path.append('..')
from entity.School import School
from entity.Course import Course
from entity.Teacher import Teacher
from db.Db import User
from core import teacher_core
from core import student_core


def teacher():
    """
        教师模块分为登录和修改密码
        教师账号由管理员创建，创建完成后在这里更改密码
    :return: 空
    """
    print("""
         1 登    录

         2 修改密码
    """)
    choice = input('请选择：\n')
    school = School()
    local_teacher = User.teacher_login(school.teacher_list)
    if choice == '1':
        if local_teacher:
            teacher_core.core(local_teacher, school.teacher_list)
    elif choice == '2':
        User.teacher_change_password(local_teacher, school.teacher_list)


def student():
    """
        学生模块分为1登录，2注册
        登录成功后，进入学生模块
    :return:空
    """
    print("""
            1 登    录

            2 注    册
       """)
    choice = input('请选择:\n')
    school = School()
    if choice in ['1', '2']:
        if choice == '1':
            local_student = User.student_login(school.student_list)
            if local_student:
                student_core.core(local_student)
        elif choice == '2':
            User.register()


def operator():
    """
        func：管理员模块的功能分为1增加教师，2增加课程，3退出系统
             其中，管理员登录密码固定，用户名：Alice,密码：123456
    :return: 空
    """
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
    """
        func： 整个系统的主函数，分为三个模块，
                1进入教师模块，2进入学生模块，3进入管理员模块
    :return:空
    """
    while True:
        print("""
        1 教师
        2 学生
        3 管理员
        """)
        choice = input('请输入你的选择：\n').strip()
        if choice in func_dic:
            func_dic[choice]()