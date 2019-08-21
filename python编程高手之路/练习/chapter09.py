"""
    将names = ['albert, 'james', 'kobe', ' kd']中的名字都变成大写
"""
names = ['albert', 'james', 'kobe', 'kd']
print(list(map(lambda x: x.upper(), names)))


"""
    将names = ['albert','jr_shenjing', 'kobe', 'kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
"""
names = ['albert','jr_shenjing', 'kobe', 'kd']
print(list(map(lambda x: x if 'shenjing' not in x else x.replace('_shenjing', ''), names)))


"""
    求shopping.txt中最长的行的长度
"""

with open('shopping.txt', encoding='utf-8') as f:
    print(max(f, key=lambda x: len(x)))


"""
    mac,20000,3
    lenovo,3000,10
    bmw,1000000,10
    chicken,200,1
    (1)总共花了多少钱
    (2)打印出所有的商品信息，格式为[{'name':'xxx','price':333,'count':3}]
    (3)求单价大于10000的商品信息，格式同上
"""
with open('shopping.txt', encoding='utf-8') as f:
    sum = 0
    for i in f:
        # 按照格式输出
        print('name:{name}, price:{price}, count:{count}'.format(name=i.split(',')[0],
                                                                 price=i.split(',')[1],
                                                                 count=i.split(',')[2].replace('\n', '')))
        # 统计所有物品的价格并输出
        sum += int(i.split(',')[1])*int(i.split(',')[2])
    print('商品总价格为：'+str(sum))
    # 文件已经读到末尾，需要重新定位定位到开始
    # 将价格大于1000的物品按照格式输出
    f.seek(0)
    for y in [i for i in f if int(i.split(',')[1]) > 1000]:
        print('name:{name}, price:{price}, count:{count}'.format(name=y.split(',')[0],
                                                                 price=y.split(',')[1],
                                                                 count=y.split(',')[2].replace('\n', '')))

