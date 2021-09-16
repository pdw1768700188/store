import random
ran=random.randint(1,10)
print(ran)
i=0
n=500
while (i<3):
    num=int(input("请输入一个数"))
    i=i+1
    if num>ran:
        n=n-100
        print("猜大了",n)
    elif num<ran:
        n-=n
        print("猜小了",n)
    else:
        n=500+10
        print("正确",n)
        break



