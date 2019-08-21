import random
import hashlib

data = []
with open('file.txt',encoding='utf-8') as f:
    for i in f:
        tmp = {}
        tmp['name'] = i.split(' ')[0]
        tmp['sex'] = i.split(' ')[1]
        tmp['age'] = i.split(' ')[2]
        tmp['salary'] = i.split(' ')[3].replace('\n','')
        data.append(tmp)

print(data)

# 得到薪资最高人的信息
print(max(data, key=lambda x: x['salary']))

# 得到最年轻人的信息
print(min(data, key=lambda x: x['age']))

# 输出名字映射成大写字母的形式
print(list(map(lambda x: x['name'].capitalize(), data)))

# 过滤掉名字以a开头人的信息
for i in data:
    if not i['name'].startswith('a'):
        print(i)


# 打印斐波那契数列
def fibonacci(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    return fibonacci(num-1)+fibonacci(num-2)


print(fibonacci(7))

# 随机输出验证码
char_pool = []
for i in range(10):
    char_pool.append(str(i))
for i in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
    char_pool.append(i)
print(char_pool)
check_num = ''
for i in range(8):
    check_num += random.choice(char_pool)

print(check_num)


# 对hash进行撞库分析
password = '123'
m = hashlib.md5()
password_has = m.update(password.encode('utf-8'))
password_hex = m.hexdigest()
try_password = ['123456', '123456789', '123']
for i in try_password:
    m = hashlib.md5()
    tmp = m.update(i.encode('utf-8'))
    if password_hex == m.hexdigest():
        print(i)


