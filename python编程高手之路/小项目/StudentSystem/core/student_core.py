import sys
sys.path.append('..')
from db.Db import UserDb
from entity.StudentScore import StudentScore


def choose_class(local_student):
    # 加载课程列表，输出所有没有老师上课的课程
    course_list = UserDb.load_from_memory('Course')
    for c in course_list:
        if c.course_teacher:
            print(c)
    choice = input('请选择要教授的课程:\n')
    if choice in set([c.course_name for c in course_list]):
        student_list = UserDb.load_from_memory('Student')
        # 找到当前学生在学生列表中的位置，并增加选课信息
        index = -1
        for t in student_list:
            index += 1
            if t.name == local_student.name:
                break
        student_list[index].add_course(choice)
        # 找到当前课程在课程列表中的位置，并增加学生信息
        index = -1
        for t in course_list:
            index += 1
            if t.course_name == choice:
                break
        course_list[index].course_student.append(StudentScore(local_student.name, '-1'))
        # 将Course和Student列表存入到文件中
        UserDb.write_to_memory('Course', course_list)
        UserDb.write_to_memory('Student', student_list)


def see_score(local_student):
    """
    学生查看成绩的时候流程
    遍历学生course_list,得到所选的每一个课程：
        遍历所有课程列表course_list,得到学生选课的course类：
            遍历课程中所有学生的列表：
                如果当前学生生姓名与分数姓名一样，输入学生成绩
    :param local_student:
    :return:
    """
    course_list = UserDb.load_from_memory('Course')
    for select_course in local_student.course_list:
        for course in course_list:
            if course.course_name == select_course:
                for sc in course.course_student:
                    if sc.student_name == local_student.name:
                        print('学生姓名：{}，所选课程：{},学生成绩：{}'.format(local_student.name, course.course_name, sc.score))


def core(local_student):
    """
    学生模块的核心，主要功能为选择课程，查看成绩
    :param local_student: 当前登录的学生信息
    :return:空
    """
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