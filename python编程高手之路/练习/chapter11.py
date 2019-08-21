"""
    定义学生类
    1.可以设置英语，数学，语文的成绩
    2.可以得到英语，数学，语文的成绩
"""


class Student:
    def __init__(self, name, English = 0, Math = 0, Chinese=0):
        self.name = name
        self.English = English
        self.Math = Math
        self.Chinese = Chinese

    def get_student_name(self):
        return self.name

    def setEnglish(self, grade):
        self.English = grade

    def setMath(self, grade):
        self.Math = grade

    def Chinese(self,grade):
        self.Chinese = grade

    def getEnglish(self):
        return self.English

    def getMath(self):
        return self.Math

    def getChinese(self):
        return self.Chinese


class StudentSystem:
    def __init__(self):
        self.all_student = []

    def add_student(self, student):
        self.all_student.append(student)

    def get_student_all_grade(self, name):
        for student in self.all_student:
            if student.get_student_name() == name:
                print('{}: 英语-{}，数学-{}，语文-{}'.format(
                    student.get_student_name(),
                    student.getEnglish(),
                    student.getMath(),
                    student.getChinese()))
                return
        print('您输入的姓名不在本系统中，请确认后重新输入')

    def get_student_one_sub_grade(self, name,subject):
        for student in self.all_student:
            if student.get_student_name() == name:
                if subject == '语文':
                    print('语文成绩为:'+str(student.getChinese()))
                elif subject == '数学':
                    print('数学成绩为:'+str(student.getMath()))
                elif subject == '英语':
                    print('英语成绩为:'+str(student.getEnglish()))
                else:
                    print('请正确输入科目')
                return
        print('您输入的姓名不在本系统中，请确认后重新输入')

    def get_all_student_one_subject(self, subject):
        print('所有人{}成绩为'.format(subject))
        for student in self.all_student:
            if subject == '语文':
                print(student.getChinese())
            elif subject == '数学':
                print(student.getMath())
            elif subject == '英语':
                print(student.getEnglish())
            else:
                print('请正确输入科目')

    def del_student(self, name):
        del_student = None
        for student in self.all_student:
            if student.get_student_name() == name:
                del_student = student
        self.all_student.remove(del_student)
        print('删除成功')


stu1 = Student('小王', 99, 98, 97)
stu2 = Student('小张', 96, 95, 99)
sys = StudentSystem()
sys.add_student(stu1)
sys.add_student(stu2)
sys.del_student('小张')