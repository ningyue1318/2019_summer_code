import sys
sys.path.append('..')
from db.Db import UserDb
from entity.StudentScore import StudentScore


def choose_class(local_student):
    course_list = UserDb.load_from_memory('Course')
    for c in course_list:
        if c.course_teacher:
            print(c)
    choice = input('请选择要教授的课程:\n')
    if choice in set([c.course_name for c in course_list]):
        student_list = UserDb.load_from_memory('Student')
        index = -1
        for t in student_list:
            index += 1
            if t.name == local_student.name:
                break
        student_list[index].add_course(choice)

        index = -1
        for t in course_list:
            index += 1
            if t.course_name == choice:
                break
        course_list[index].course_student.append(StudentScore(local_student.name, '-1'))

        UserDb.write_to_memory('Course', course_list)
        UserDb.write_to_memory('Student', student_list)


def see_score(local_student):
    course_list = UserDb.load_from_memory('Course')
    for select_course in local_student.course_list:
        for course in course_list:
            if course.course_name == select_course:
                for sc in course.course_student:
                    if sc.student_name == local_student.name:
                        print('学生姓名：{}，所选课程：{},学生成绩：{}'.format(local_student.name, course.course_name, sc.score))


def core(local_student):
    while True:
        print("""
        1 选择课程
        2 查看成绩
        3 退出登录
        """)
        choice = input('请选择：\n')
        if choice in ['1', '2', '3']:
            if choice == '1':
                choose_class(local_student)
            elif choice == '2':
                see_score(local_student)
            elif choice == '3':
                print('退出登录')
                break