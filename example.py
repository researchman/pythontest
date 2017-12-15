'''
#eg1:两数字求和
print("两数字求和.");
num1 = float(input("输入第一个数字："));
num2 = float(input("输入第二个数字："));

print("%.2f + %.2f = %.2f"%(num1,num2,num1+num2));
'''

#eg2:求平方根
'''
#无法求负数的
x = float(input("请输入待求平方根的数字："));
print("%.2f的平方根是：%.2f"%(x,x**0.5));
'''
'''
import cmath;
x = float(input("请输入待求平方根的数字："));
y = cmath.sqrt(x);
print("{0}的平方根是：{1:0.3f}+{2:0.3f}".format(x,y.real,y.imag));
'''

#eg3:二次方程
'''
import cmath;
a = float(input("输入二次系数："));
b = float(input("输入一次系数："));
c = float(input("输入常数："));

dt = b**2 - 4*a*c;
b1 = (-b+cmath.sqrt(dt))/(2*a);
b2 = (-b-cmath.sqrt(dt))/(2*a);

print("{0},{1}".format(b1,b2));
'''

'''
#eg4.求三角形面积
a = float(input("输入三角形的第一条边的边长："));
b = float(input("输入三角形的第二条边的边长："));
c = float(input("输入三角形的第三条边的边长："));

s = (a+b+c)/2;
area = (s*(s-a)*(s-b)*(s-c))**0.5;
print("三角形的面积是:%.3f"%area);
'''

'''
#eg5:随机数生成
import random;

i = 0;
while i < 10:
    print(random.randint(0,100));# 0<= N <=100
    i = i + 1;
'''

'''
#eg6:摄氏温度转华氏温度
celsius = float(input("请输入摄氏温度:"));

fahrenheit = celsius*1.8 + 32;
print("%.2f 摄氏温度对应的华氏温度为：%.2f"%(celsius,fahrenheit));
'''

'''
#eg7:交换变量
a = float(input("变量1:"));
b = float(input("变量2:"));

#使用零时变量
#temp = a;
#a = b;
#b = temp;
#不使用零时变量
a,b = b,a;

print("新变量1：%.2f,新变量2：%.2f"%(a,b));
'''

'''
#eg8:判断输入值是正数还是负数，或者是零
a = float(input("输入待检查的数字："));
if a > 0:
    print("%.2f是正数"%a);
elif a == 0:
    print("%.2f是零"%a);
else:
    print("%.2f是负数"%a);
'''
'''
#eg9:判断字符串是否为数字
def is_number(string):
    try:
        float(string);
        return True
        pass
    except ValueError:
        #return False;  #允许unicode检查
        pass
    
    try:
        import unicodedata;
        unicodedata.numeric(string);
        return True;
    except (TypeError,ValueError):
        return False;

    return False;
    pass

# 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
 
# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False
'''

'''
#eg10.判断输入数字是奇数或是偶数
a = int(input("输入整数："));

if a%2 == 0:
    print("%d是偶数。"%a);
else:
    print("%d是奇数。"%a);
'''

'''
#eg11:判断输入年份是不是闰年
year = int(input("请输入检查的年份："));
if (year%4) == 0:
    if (year%100) == 0:
        if (year%400) == 0:
            print("%d年是闰年."%year);
            pass
        else:
            print("%d年不是闰年."%year);
            pass
        pass
    else:
        print("%d年是闰年."%year);
        pass
else:
    print("%d年不是闰年."%year);
'''

'''
#eg12:最大数
# 最简单的
print(max(1, 2))
print(max('a', 'b'))
 
# 也可以对列表和元组使用
print(max([1,2]))
print(max((1,2)))

# 更多实例
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))
'''

'''
import math;
#eg13:求质数
a = int(input("请输入待检查的数："));

if a > 1:
    sqrt_num = math.floor(a**0.5) + 1;
    for i in range(2,sqrt_num):
        if a%2 == 0:
            print("%d不是质数."%a);
            break;
    else:
        print("%d是质数."%a);
else:
    print("%d既不是质数也不是合数。"%a);
'''

'''
#eg14:输出指定范围内的质数
lower = int(input("输入区间的最小值："));
upper = int(input("输入区间的最大值："));

if lower > upper:
    lower,upper = upper,lower;

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break;
        else:
            print(num);
'''

'''
#eg15:阶乘
n = int(input("阶乘数："));

multi = 1;
if n == 0:
    print(1);
elif n > 0:
    #multi = 1;
    for i in range(1,n+1):
        multi = multi * i;
        print(multi);
    print("%d! = %d"%(n,multi));
'''

#eg16:如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
num = int(input("请输入检查范围："));

sum = 0;
n = len(str(num));

# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")
    


