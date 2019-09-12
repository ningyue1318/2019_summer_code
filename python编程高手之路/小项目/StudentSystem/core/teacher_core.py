import sys
sys.path.append('..')
from db.Db import UserDb


def choose_class(teacher, teacher_list):
    course_list = UserDb.load_from_memory('Course')
    for c in course_list:
        if not c.course_teacher:
            print(c)
    choice = input('请选择要教授的课程:\n')
    if choice in set([c.course_name for c in course_list]):
        index = -1
        for t in course_list:
            index += 1
            if t.course_name == choice:
                break
        course_list[index].course_teacher = teacher.name
        UserDb.write_to_memory('Course', course_list)
        choose_course = course_list[index]
        index = -1
        for t in teacher_list:
            index += 1
            if t.name == teacher.name:
                break
        teacher_list[index].course_list.append(choose_course)
        UserDb.write_to_memory('Teacher', teacher_list)


def scoring(teacher):
    course_list = UserDb.load_from_memory('Course')
    c_index = -1
    for c in course_list:
        c_index += 1
        if c.course_teacher == teacher.name:
            print('请给学生打分:\n')
            s_index = 0
            for sc in c.course_student:
                score = input(sc.student_name+":的分数为\n")
                course_list[c_index].course_student[s_index].score = score
                print(sc.student_name+":分数为"+score)
    UserDb.write_to_memory('Course', course_list)


def see_course(teacher):
    print('您教授的课程列表如下:\n')
    course_list = UserDb.load_from_memory('Course')
    for c in course_list:
        if c.course_teacher == teacher.name:
            print(c)


def core(teacher, teacher_list):
    while True:
        print("""
        1 选择课程
        2 查看课程
        3 登记成绩
        4 退出系统
        """)
        choice = input("请选择：\n")
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                choose_class(teacher,teacher_list)
            elif choice == '2':
                see_course(teacher)
            elif choice == '3':
                scoring(teacher)
            elif choice == '4':
                print('退出系统')
                break
