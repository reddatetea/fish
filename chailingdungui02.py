import re
import easygui

title = '湖北双佳纸品有限公司'
choice = True
while choice :
    msg = '是否计算纸张的吨数、令数、吨价、令价、克重、长、宽？'
    choice = easygui.ynbox(msg, title = title,choices=('Yes', 'No'), cancel_choice='No')
    if choice == True:
        msg = '请点选“计算吨数令数" 或 "计算吨价令价"'
        print(msg)
        choice = easygui.buttonbox(msg, title=title, choices=['计算吨数令数', '计算吨价令价', '退出程序'])
        if choice == '计算吨数令数':
            msg = '请点选要查询的按钮'
            choices = ['克重', '长', '宽', '令数', '吨数']
            choice = easygui.buttonbox(msg, title=title, choices=choices)
            order = ['01', '02', '03', '04', '05']
            choices_order = dict(zip(choices, order))
            order_choices = dict(zip(order, choices))
            values = dict(zip(choices, ['ke', 'chang', 'kuan', 'ling', 'dun']))
            choices_x = list(set(choices) - set([choice]))
            choices_x.sort()
            _ = [choices_order[j] for j in choices_x]
            _.sort()
            choices_x_order = [order_choices[k] for k in _]
            msg = ' 为计算"{}"请填写相关数据,长、宽的单位是cm'.format(choice)
            value0 = '{}'.format(values[choices_x_order[0]])  # 'ke'
            value1 = '{}'.format(values[choices_x_order[1]])
            value2 = '{}'.format(values[choices_x_order[2]])
            value3 = '{}'.format(values[choices_x_order[3]])
            values = [value0, value1, value2, value3]
            v0, v1, v2, v3 = easygui.multenterbox(msg, title = title,fields=choices_x_order)
            vs = [v0, v1, v2, v3]
            for i in range(len(values)):  # 将字符串名作为变量
                m = values[i]
                n = vs[i]
                exec("{} = n".format(m))
            if choice == '吨数':
                dun = float(ke) / 1000 / 1000 * float(chang) / 1000 * float(kuan) / 1000 * 500 * float(ling)
                msg = '经计算，{}是：{} 吨'.format(choice,round(dun, 4))
                easygui.msgbox(msg,title = title)
            elif choice == '令数':
                ling = float(dun) / float(ke) * 1000 * 1000 / float(chang) * 1000 / float(kuan) * 1000 / 500
                msg = '经计算，{}是：{} 令'.format(choice, round(ling, 2))
                easygui.msgbox(msg,title = title)
            elif choice == '克重':
                ke = float(dun) / float(ling) / 500 * 1000 / float(chang) * 1000 / float(kuan) * 1000 * 1000
                msg = '经计算，{}是：{} 克'.format(choice, int(round(ke, 0)))
                easygui.msgbox(msg,title = title)
            elif choice == '长':
                chang = float(dun) * float(ling) / float(ke) * 1000 * 1000 / float(kuan) * 1000 / 500 / 1000
                msg = '经计算，{}是：{} cm'.format(choice, int(round(chang, 0)))
                easygui.msgbox(msg,title = title)
            else:
                kuan = float(dun) * float(ling) / float(ke) * 1000 * 1000 / float(chang) * 1000 / 500 / 1000
                msg = '经计算，{}是：{} cm'.format(choice, int(round(kuan, 0)))
                easygui.msgbox(msg,title = title)

        elif choice == '计算吨价令价':
            msg = '请点选要查询的按钮'
            choices = ['克重', '长', '宽', '吨价', '令价']
            choice = easygui.buttonbox(msg, title=title, choices=choices)
            order = ['01', '02', '03', '04', '05']
            choices_order = dict(zip(choices, order))
            order_choices = dict(zip(order, choices))
            values = dict(zip(choices, ['ke', 'chang', 'kuan', 'dunjia', 'lingjia']))
            choices_x = list(set(choices) - set([choice]))
            choices_x.sort()
            _ = [choices_order[j] for j in choices_x]
            _.sort()
            choices_x_order = [order_choices[k] for k in _]
            msg = ' 为计算"{}"请填写相关数据,长、宽的单位是cm'.format(choice)
            value0 = '{}'.format(values[choices_x_order[0]])  # 'ke'
            value1 = '{}'.format(values[choices_x_order[1]])
            value2 = '{}'.format(values[choices_x_order[2]])
            value3 = '{}'.format(values[choices_x_order[3]])
            values = [value0, value1, value2, value3]
            v0, v1, v2, v3 = easygui.multenterbox(msg, title = title,fields=choices_x_order)
            vs = [v0, v1, v2, v3]
            for i in range(len(values)):  # 将字符串名作为变量
                m = values[i]
                n = vs[i]
                exec("{} = n".format(m))
            if choice == '吨价':
                dunjia = float(lingjia) / float(ke) * 1000 * 1000 / float(chang) * 1000 / float(kuan) * 1000 / 500
                msg = '经计算，{}是：{} 元/吨'.format(choice, int(round(dunjia, 0)))
                easygui.msgbox(msg,title = title)
            elif choice == '令价':
                lingjia = float(ke) / 1000 /1000 *float(chang) /1000 *float(kuan) /1000 * 500*float(dunjia)
                msg = '经计算，{}是：{} 元/令'.format(choice, round(lingjia, 2))
                easygui.msgbox(msg,title = title)
            elif choice == '克重':
                ke = float(lingjia) / float(dunjia) / 500 * 1000 * 1000 / float(chang) * 1000 / float(kuan) * 1000
                msg = '经计算，{}是：{} 克'.format(choice, int(round(ke, 0)))
                easygui.msgbox(msg,title = title)
            elif choice == '长':
                chang = float(lingjia) / float(dunjia) / 500 * 1000 * 1000 / float(ke) * 1000 / float(kuan) * 1000
                msg = '经计算，{}是：{} cm'.format(choice, int(round(chang, 0)))
                easygui.msgbox(msg,title = title)
            else:
                kuan = float(lingjia) / float(dunjia) / 500 * 1000 * 1000 / float(ke) * 1000 / float(chang) * 1000
                msg = '经计算，{}是：{} cm'.format(choice, int(round(kuan, 0)))
                easygui.msgbox(msg,title = title)

        else:
            print('退出程序')

    else :
        print('退出查询程序')
        break
