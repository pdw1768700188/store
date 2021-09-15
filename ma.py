import random
ran=random.randint(1,10)
print(ran)
while (True):
    num=int(input("请输入一个数"))
    if num>ran:
        print("猜大了")
    elif num<ran:
        print("猜小了")
    else:
        print("正确")
        break



