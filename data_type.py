'''
a = 1;
b = 10.0;
c = "test";
'''

#a = b = c = 1;
#a,b,c,d,e= 1,10.0,"test",True,1+2j;

'''
print(a);
print(b);
print(c);
'''
'''
print(type(a),type(b),type(c),type(d),type(e));

print(isinstance(a,int));

#isinstance 和 type 的区别
print("compare isinstance&type");

class A:
    pass

class B(A):
    pass


print(isinstance(A(),A));
print(type(A()) == A);
print(isinstance(B(),A));
print(type(B()) == A);
'''

'''
#字符串
str = "zhuyunfei";

print(str);
print(str[4]);
print(str[0:-1]);
print(str[2:])
print(str*3);
print(str + "brandon");
'''

'''
#list
list1 = ["abc",123,4.5,"brandon",8.09];
add_list = [1234,"efg",5.6];

print(list1[0]);
print(list1[-1]);
print(list1[-2]);
print(list1[1:4])
print(list1[2:]);
print(list1*3);
print(list1 + add_list);
'''

'''
#tuple 元祖
tuple = ("abc",123,4.5,"brandon",6.7);
add_tuple = ("zhuyf",4.6);

print(tuple[0]);
print(tuple[-1]);
print(tuple[2:]);
print(tuple[2:4]);
print(tuple*2);
print(tuple + add_tuple);
'''
'''
#set
student = {"Tom","Jim","Mary","Tom","Jack","Rose"};
print(student);

#成员测试
if "Rose" in student:
    print("Rose在集合中");
else:
    print("Rose不在集合中");

#set可以进行集合元算
a = set("abracadabra");
b = set("alacazam");

print(a);
print(a-b); #a和b的差集
print(a|b); #a和b的并集
print(a&b); #a和b的交集
print(a^b); #a和b中不同时存在的元素
'''

'''
#dictionary
dict = {};
dict["one"] = "1 - 菜鸟教程";
dict[2] = "2 - 菜鸟工具";

print(dict);

tinydict = {"name":"brandon","code":1,"site":"www.163.com"};
print(dict["one"]);
print(dict[2]);
print(tinydict);
print(tinydict.keys());
print(tinydict.values());
'''

'''
#数据类型转换
x = "2017-11-26 12:34:40.223";
print(repr(x));
'''
'''
a = 20;
b = 20;

print(id(a));
print(id(b));

if a is b:
    print("a和b有相同的标识");
else:
    print("a和b有不同的标识");

if id(a) == id(b):
    print("a和b有相同的标识");
else:
    print("a和b有不同的标识");

b = 30;
if a is b:
    print("a和b有相同的标识");
else:
    print("a和b有不同的标识");

if a is not b:
    print("a和b有不同的标识");
else:
    print("a和b有相同的标识");
'''
'''
a = 60;
print(bin(a));
print(oct(a));
print(hex(a));
'''

'''
a = 10;
b = 10;

c = complex(2,3);
del b;
print(a);
#print(b);
print(c**2);
'''
'''
#数学公式
import math;
a = 10.1;
math.modf(a);

#随机数
import random;
'''

#print('\a');   #响铃
#print("test");

str = "abc,def,ghi";
print(str.split(","));

