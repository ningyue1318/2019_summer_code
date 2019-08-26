"""
    实现单例模式的几种方式
"""
# 1使用装饰器


def Singleton(cls):
    __instance = {}

    def _sigleton(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return _sigleton


@Singleton
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x

#
# a1 = A(2)
# a2 = A(3)
# print(a1.x)
# print(a2.x)


# 2 模块方式，python中的模块是天然的单例模式，所有的模块只加载一次

"""
    第二个作业
"""


class CarMeta(type):
    def __init__(self,class_name, class_bases, class_dic):
        super(CarMeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        if not hasattr(obj, 'capacity'):
            raise TypeError('没有capacity属性')
        if not hasattr(obj, 'engine_number'):
            raise TypeError('没有engine_number属性')
        if not hasattr(obj, 'production_date'):
            raise TypeError('没有production_date属性')
        return obj


class Car(object, metaclass=CarMeta):
    def __init__(self, production_date, engine_number, capacity):
        self.production_date = production_date
        self.engine_number = engine_number
        self.capacity = capacity


c = Car('2012-2-2', '12323', '123123')