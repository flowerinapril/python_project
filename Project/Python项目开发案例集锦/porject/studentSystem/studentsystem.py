import re


def main():
    ctrl = True
    while (ctrl):
        menu()
        option = input("请选择：")
        option_str = re.sub("\D", "", option)
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option_str)
            if option_int == 0:
                print("已退出学生信息管理系统")
                ctrl = False
            elif option_int == 1:  # 录入学生成绩信息
                insert()
            elif option_int == 2:  # 查找学生成绩信息
                search()
            elif option_int == 3:  # 删除学生成绩信息
                delete()
            elif option_int == 4:  # 修改学生成绩信息
                modify()
            elif option_int == 5:  # 排序
                sort()
            elif option_int == 6:  # 统计学生总数
                total()
            elif option_int == 7:  # 显示所有学生信息
                show()


def menu():
    # 输出菜单
    print('''
    ╔———————学生信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                     │
    │   6 统计学生总人数                           │
    │   7 显示所有学生信息                         │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字或↑↓方向键选择菜单          │
    ╚———————————————————————╝
    ''')


def save(student):
    try:
        student_txt = open("studentinfo.txt", "a")
    except Exception as e:
        student_txt = open("studentinfo.txt", "w")
    for info in student:
        student_txt.write(str(info) + "\n")
    student_txt.close()


def insert():
    stdentList = []
    mark = True
    while mark:
        id = input("please input id(like 1001):")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("please input english point"))
            python = int(input("please input python point"))
            c = int(input("please input c point"))
        except Exception as e:
            print("invalid input, not int type, please input again")
            print(e)
            continue
        stdent = {"id": id, "name": name, "english": english, "python": python, "c": c}
        stdentList.append(stdent)
        inputMark = input("是否继续添加(y/n)")
        if inputMark == "y":
            mark = True
        else:
            mark = False
        save(stdentList)
        print("学生信息录入完成")


if __name__ == '__main__':
    main()
