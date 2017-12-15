#def hello():
#    print("hello");

'''
def calc_area(width,height):
    return width*height;

def hello(name):
    print("hello," + name);

print(calc_area(5,4));
#print(hello());
print(hello("brandon"));#
'''

'''
def print_info(name,age):
    print("姓名：" + name);
    print("年龄：",age);

name = "brandon";
age = 34;
#print_info(age,name);   #error
#print_info(name,age);
print_info(age = 50,name = "baidu");
'''

'''
#可变参数
def print_info(arg,*var_tuple):
    print("参数：");
    print(arg);
    for var in var_tuple:
        print(var);

print_info(60);
print_info(60,50,40,30);
'''

'''
#lambda表达式
sum = lambda arg1,arg2:arg1+arg2;

print(sum(10,20));
print(sum(20,30));
'''

'''
import support;
support.print_func("brandon");  #需要加模块名

print(__name__);
print(dir());
'''

import pprint,pickle;

pkl_file = open("data.pkl","rb");
data1 = pickle.load(pkl_file);
pprint.pprint(data1);

data2 = pickle.load(pkl_file);
pprint.pprint(data2);

pkl_file.close();
