#/usr/bin/python3
#Python关键字
#import keyword;
#print(keyword.kwlist);
import sys;
#注释
#注释2

'''
#缩进
s = False;
if s:
    print("add");
else:
    print("sub");      

#字符串
one = 'single quote';
two = "double quote";
three = """this is 
triple quote""";
output = "this " "is " "string";
print(one + "\n" + two + "\n" + three + "\n" + output);  
'''

"""
多行注释
"""        
#ip = input("\n\n按下enter键后退出。");
#print(ip);

#单行多条语句,使用分号分割
#x = 'runoob'; sys.stdout.write(x+'\n');

'''
#print输出
for i in [1,2,3,4,5,6,7,8,9,10]:
    if i < 5:
        print(i);
    elif i>=5 and i < 8:
        print(i,end='');
    else:
        print(i);           
    #print(i);
    pass
'''
#导入模块
print("===========================Python import mode==============================");
print("命令行参数");
for arg in sys.argv:
    print(arg);
print("\n Python路径为：",sys.path);

from sys import argv,path;
print("python path: ",path);