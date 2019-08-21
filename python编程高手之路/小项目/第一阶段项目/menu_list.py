menu = {
    '汽车': {
        '轿车': {
            '宝马': {
                '宝马760': {},
                '宝马M5': {},
                '宝马M3': {}
            },
            '奔驰': {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {}
            },
            '奥迪': {
                '奥迪A4L':{}
            }
        },
        '越野车': {
            '路虎': {},
            '英菲尼迪':{}
        },
        '卡车': {

        }
    },
    '飞机': {
        '直升机': {
            '武直-11直升机':{}
        },
        '轰炸机': {
            'B-29轰炸机': {}
        },
        '战斗机': {
            'F-18战斗机':{}
        }
    },
    '大炮': {

    }
}


def show_the_first():
    print('------------欢迎来到宁悦图片系统:------------')
    for index, categories in enumerate(menu.keys(), 1):
        print(" "*18+str(index)+" "+categories)


def show_the_second(index):
    if len(menu[index]) == 0:
        print('暂时未收录图片，请等待更新')
    for index, categories in enumerate(menu[index], 1):
        print(" " * 18 + str(index) + " " + categories)


def show_the_third(first_index, index):
    if len(menu[first_index][index]) == 0:
        print('暂时未收录图片，请等待更新')
    for index, categories in enumerate(menu[first_index][index], 1):
        print(" " * 18 + str(index) + " " + categories)


# 判断当前菜单在第几级，第一级为0，第二级为1，第三级为2
flag = 0
# 记录第一级菜单选项
flag_first_menu = ''
# 记录第二季菜单选项
show_the_first()
while True:
    select_id = input('请选择要查看的种类(q退出系统,b返回上一层系统):\n')
    if select_id == 'q':
        print('退出系统成功')
        break
    elif select_id == 'b':
        if flag == 2:
            flag = 1
            show_the_second(flag_first_menu)
        elif flag == 1:
            flag = 0
            show_the_first()
    elif select_id.isnumeric():
        if flag == 0:
            get_index = list(menu.keys())[int(select_id)-1]
            show_the_second(get_index)
            flag = 1
            flag_first_menu = get_index
        elif flag == 1:
            get_index = list(menu[flag_first_menu].keys())[int(select_id) - 1]
            show_the_third(flag_first_menu, get_index)
            flag = 2









