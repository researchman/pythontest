'''
def fab(n):
    if n < 1:
        print("input error.");
    elif n == 1 or n == 2:
        return 1;
    else:
        return fab(n-2) + fab(n-1);

i = 1;
while i < 10:
    print(fab(i)); 
    i = i + 1;
'''

'''
age = int(input("please enter dog's age:"));
if age < 0:
    print("are you kidding me?");
elif age == 1:
    print("it is equal to 14.");
elif age == 2:
    print("it is equal to 22.");
elif age > 2:
    human = 22 + (age - 2)*5;
    print("it is equal to %d."%human);

#退出
input("点击enter键退出.")
'''

'''
#猜数字
number = 0;
guess = -1;

while number != guess:
    number = int(input("请输入预估的数字："));
    if number > guess:
        print("猜的数字大了.");
    elif number == guess:
        print("bingo.");
    elif number < guess:
        print("猜的数字小了.");
'''

'''
#9*9乘法表
i = 1;
while i<=9:
    j = 1;
    while j<=i:
        mul = i*j;
        if j == i:
            print("%d*%d = %d"%(j,i,mul));
        else:
            print("%d*%d = %d"%(j,i,mul),end=",");
        j =j + 1;
    i = i + 1;
'''

list = [1,2,3,4];
it = iter(list);

for x in it:
    print(x);
'''
i = 0;
while i<len(list):
    print(next(it));
    i = i + 1;
'''




