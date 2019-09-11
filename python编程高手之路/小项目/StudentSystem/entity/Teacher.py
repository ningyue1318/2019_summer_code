class Teacher:
    def __init__(self, teacher_name):
        self.name = teacher_name
        self.password = '123456'
        self.course_list = []

    def add_course(self, course):
        self.course_list.append(course)

