class Teacher:
    def __init__(self, teacher_name):
        self.name = teacher_name
        self.__password = '123456'
        self.course_list = []

    def add_course(self, course):
        pass