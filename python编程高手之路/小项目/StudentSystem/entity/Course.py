class Course:
    """
        func: 完成课程类的操作，可以创建课程，设置老师姓名，设置听课学生姓名

    """
    def __init__(self, course_name, course_loc, course_price, course_time):
        self.course_name = course_name
        self.course_loc = course_loc
        self.course_price = course_price
        self.course_time = course_time
        self.course_teacher = None
        self.course_student = []

    def set_course_teacher(self):
        pass

    def add_course_student(self):
        pass

    def __str__(self):
        return '本门课程：{}，开课地点：{}，开课时间：{}，开课价格：{}'\
            .format(self.course_name, self.course_loc, self.course_time, self.course_price)

