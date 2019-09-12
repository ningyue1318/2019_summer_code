import sys
sys.path.append('..')
from entity.Course import Course
from entity.Teacher import Teacher
from db.Db import UserDb

"""
    学校类，拥有teacher列表，course列表，student列表，在初始化的时候在内存中加载
"""


class School:
    def __init__(self):
        self.teacher_list = UserDb.load_from_memory('Teacher')
        self.course_list = UserDb.load_from_memory('Course')
        self.student_list = UserDb.load_from_memory('Student')

    def load_data(self):
        pass

    def add_teacher(self):
        teacher_name = input('请输入老师的名称:\n').strip()
        t = Teacher(teacher_name)
        self.teacher_list.append(t)
        UserDb.write_to_memory('Teacher', self.teacher_list)
        print('增加教师：' + t.name)

    def add_course(self):
        course_name = input('请输入课程名称:\n').strip()
        course_loc = input('请输入课程位置:\n').strip()
        course_price = input('请输入课程价格:\n').strip()
        course_time = input('请输入课程时间:\n').strip()
        c = Course(course_name, course_loc, course_price, course_time)
        self.course_list.append(c)
        UserDb.write_to_memory('Course', self.course_list)
        print(c)

    def add_student(self, student):
        pass
