import abc


class Course:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return '课程名称为：'+self.name+' 课程价格为:'+str(self.price)


class People:
    def __init__(self, name):
        self.name = name
        self.course_list = []

    def add_course(self,course):
        self.course_list.append(course)


class Teacher(People):
    def show_list(self):
        print(self.name+'老师教授课程为：')
        for c in self.course_list:
            print(c)


class Student(People):
    def show_list(self):
        print(self.name+'学生学习课程为：')
        for c in self.course_list:
            print(c)


"""
    以下是作业2
"""


class Pet(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @abc.abstractclassmethod
    def eat(self):
        pass


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print('猫吃东西')


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print('狗吃东西')


class Pig(Pet):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print('猪吃东西')


class Master:
    def __init__(self, name, pet):
        self.__name = name
        self.__pet = pet

    def feed(self):
        print(self.__pet.name+"主人准备好宠物粮食")
        self.__pet.eat()


if __name__ == '__main__':
    select = 1
    if select == 2:
        c = Cat('小猫')
        d = Dog('小狗')
        p = Pig('小猪')
        master = Master('小张', d)
        master.feed()
    else:
        math = Course('数学', 800)
        English = Course('英语', 500)
        Chinese = Course('语文', 600)
        tea1 = Teacher('小张')
        tea1.add_course(math)
        stu1 = Student('小李')
        stu1.add_course(math)
        stu1.add_course(English)
        stu1.add_course(Chinese)
        stu1.show_list()
        tea1.show_list()

