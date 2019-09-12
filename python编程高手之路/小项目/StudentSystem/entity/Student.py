class Student:
    def __init__(self, student_name, password):
        self.name = student_name
        self.password = password
        self.course_list = []

    def add_course(self,course):
        self.course_list.append(course)
