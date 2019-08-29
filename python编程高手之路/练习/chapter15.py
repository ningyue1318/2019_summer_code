# 超过MAX爆出异常，现在MAX值为2147483648
MAX = 2**31


class SlopOverError(BaseException):
    def __init__(self, number, message):
        self.number = number
        self.message = message

    def __str__(self):
        return '%s:%s-越界'%(self.message, self.number)


class MyInteger:

    @staticmethod
    def get_input(number):
        if type(number) == str:
            raise TypeError('invalid literal for int() with base 10:'+number)
        if abs(number) > MAX:
            raise SlopOverError(number, 'ErrrorMsg')
        return number


MyInteger.get_input(20)

