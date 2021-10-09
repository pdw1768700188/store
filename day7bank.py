'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random
import time
from sql_ff import update
from sql_ff import select

# 1.准备一个数据库 和 银行名称
bank_name = "中国工商银行支行"  # 银行名称写死的

# 2.入口程序
def welcome():
    print("*************************************")
    print("*         中国工商银行昌平支行         *")
    print("*************************************")
    print("*    1.开户                          *")
    print("*    2.存钱                          *")
    print("*    3.取钱                          *")
    print("*    4.转账                          *")
    print("*    5.查询                          *")
    print("*    6.Bye！                         *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    sql = "select count(*) from user "
    param = []
    data = select(sql, param)
    if data[0][0] >= 100:
        return 3

    # 2.判断用户是否存在
    sql2 = "select * from user where  username = %s"
    param2 = [username]
    data2 = select(sql2, param2)
    if len(data2) != 0:
        return 2

    # 3.正常开户
    sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [account, username, password, country, province, street, gate, money, bank_name]
    update(sql3, param3)
    return 1


def zz():
    status = bank_addUser(account, username, password, country, province, street, gate, money)
    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
                                    ----------个人信息------
                                    账号：%s
                                    姓名：%s
                                    密码：%s
                                    地址信息
                                        国家：%s
                                        省份：%s
                                        街道：%s
                                        门牌号: %s
                                    余额：%s
                                    开户行地址：%s
                                    ------------------------
                                '''
        print(info % (account, username, password, country, province, street, gate, money, bank_name))
    time.sleep(3)


def CQ():
    cqzz = input("请输入你要查询的账号")
    sql = "select * from user where account = %s"
    param = [cqzz]
    data = select(sql, param)
    if cqzz == data[0][0]:
        Ct = int(input("请输入你要存的钱数"))
        print("请放入您的钞票")
        print("...")
        sql3 = "update user set money = money + %s where account = %s"
        param3 = [Ct,cqzz]
        update(sql3, param3)
        print("存钱成功")
    else:
        print("存钱失败")


def QQ():
    qqh = input("请输入你要取钱的账号")
    sql = "select * from user where account = %s"
    param = [qqh]
    data = select(sql, param)
    if qqh in data[0][0]:
        qqmm= input("请输入你要取钱的密码")
        if qqmm == data[0][2]:
            qqq = input("请输入你要取钱的金额")
            if qqq < data[0][2]:
                sql3 = "update user set money = money - %s where account = %s"
                param3 = [qqq, qqh]
                update(sql3, param3)
                print("请稍等...")
                time.sleep(1.5)
                print("取钱成功")
            else:
                print("取钱失败，你没那么多钱穷鬼")
        else:
            print("您的密码输入错误")
    else:
        print("您输入的账户错误")


def ZZ():
    zzh = input("请输入你的账号")
    sql = "select * from user where account = %s"
    param = [zzh]
    data = select(sql, param)
    if zzh in data[0][0]:
        zzm = input("请输入你的密码")
        if zzm == data[0][2]:
            zzh1 = input("请输入你要转账的账号")
            sql1 = "select * from user where account = %s"
            param1 = [zzh1]
            data1 = select(sql1, param1)
            if zzh1 == data1[0][0]:
                zzq = input("请输入你要转账的金额")
                if zzq < data[0][2]:
                    sql3 = "update user set money = money - %s where account = %s"
                    param3 = [zzq, zzh]
                    update(sql3, param3)
                    sql2 = "update user set money = money + %s where account = %s"
                    param2 = [zzq, zzh1]
                    update(sql2, param2)
                    print("请稍等...")
                    time.sleep(1.5)
                    print("转账成功")
                else:
                    print("转账失败，你没那么多钱")
            else:
                print("无此账号")
        else:
            print("您的密码输入错误")
    else:
        print("您输入的账户错误")


def CX():
    cxzz = input("请输入你要查询的账号")
    sql = "select * from user where account = %s"
    param = [cxzz]
    data = select(sql, param)
    if cxzz in data[0][0]:
        cxmm = input("请输入你要查询的密码")
        if cxmm == data[0][2]:
            print("您当前余额为：",data[0][7])
        else:
            print("您的密码输入错误")
    else:
        print("您的账号输入错误")


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        account = random.randint(100000000, 999999999)
        username = input("请输入您的用户名：")
        password = int(input("请输入您的开户密码："))
        country = input("请输入您的国籍：")
        province = input("请输入您的居住省份：")
        street = input("请输入您的街道：")
        gate = input("请输入您的门牌号：")
        money = int(input("请输入您的存钱金额"))  # 将输入金额转换成int类型
        zz()
        # 随机产生8为数字
        time.sleep(3)
    elif chose == "2":
        CQ()
        time.sleep(3)
    elif chose == "3":
        QQ()
        time.sleep(3)
    elif chose == "4":
        ZZ()
        time.sleep(3)
    elif chose == "5":
        CX()
        time.sleep(3)
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")
