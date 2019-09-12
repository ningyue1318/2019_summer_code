import pickle
import os
import sys
sys.path.append('..')
from entity.Course import Course
from entity.Student import Student
from conf.settings import *


class User:
    @staticmethod
    def login():
        flag = 3
        while flag > 0:
            username = input('请输入用户名:\n')
            password = input('请输入密码：\n')
            if username == 'alice' and password == '123456':
                print('登陆成功')
                return True
            else:
                flag -= 1
                print('登录失败,还剩{}次机会'.format(str(flag)))
                return False

    @staticmethod
    def register():
        username = input('请输入需要注册的用户名:\n')
        first_password = 'first'
        second_password = 'second'
        while first_password != second_password:
            first_password = input('请输入需要注册的密码:\n')
            second_password = input('请再次确认密码:\n')
        s = Student(username, first_password)
        student_list = UserDb.load_from_memory('Student')
        student_list.append(s)
        UserDb.write_to_memory('Student', student_list)
        print('注册成功')

    @staticmethod
    def teacher_login(teacher_list):
        flag = 3
        while flag > 0:
            username = input('请输入用户名:\n')
            password = input('请输入密码：\n')
            for t in teacher_list:
                if t.name == username and t.password == password:
                    return t
            else:
                flag -= 1
                print('登录失败,还剩{}次机会'.format(str(flag)))
        return None

    @staticmethod
    def teacher_change_password(local_teacher, teacher_list):
        first_password = 'first'
        second_password = 'second'
        while first_password != second_password:
            first_password = input('请输入新的密码:\n')
            second_password = input('请再次确认密码:\n')
        index = -1
        for t in teacher_list:
            index += 1
            if t.name == local_teacher.name:
                break
        teacher_list[index].password = first_password
        UserDb.write_to_memory('Teacher',teacher_list)

    @staticmethod
    def student_login(student_list):
        flag = 3
        while flag > 0:
            username = input('请输入用户名:\n')
            password = input('请输入密码：\n')
            for s in student_list:
                if s.name == username and s.password == password:
                    return s
            else:
                flag -= 1
                print('登录失败,还剩{}次机会'.format(str(flag)))
        return None


class UserDb:
    @staticmethod
    def write_to_memory(user_type, data):
        if user_type == 'Operator':
            with open(OPERATOR_DIR, mode='wb') as f:
                pickle.dump(data, f)
        elif user_type == 'Student':
            with open(STUDENT_DIR, mode='wb') as f:
                pickle.dump(data, f)
        elif user_type == 'Teacher':
            with open(TEACHER_DIR, mode='wb') as f:
                pickle.dump(data, f)
        elif user_type == 'Course':
            with open(COURSE_DIR, mode='wb') as f:
                pickle.dump(data, f)

    @staticmethod
    def load_from_memory(load_type):
        if load_type == 'Student':
            if os.path.exists(STUDENT_DIR):
                with open(STUDENT_DIR, mode='rb') as f:
                    data = pickle.load(f)
                    return data
            else:
                return []
        elif load_type == 'Teacher':
            if os.path.exists(TEACHER_DIR):
                with open(TEACHER_DIR, mode='rb') as f:
                    data = pickle.load(f)
                    return data
            else:
                return []
        elif load_type == 'Course':
            if os.path.exists(COURSE_DIR):
                with open(COURSE_DIR, mode='rb') as f:
                    data = pickle.load(f)
                    return data
            else:
                return []

