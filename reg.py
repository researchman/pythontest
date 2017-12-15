import re;

print(re.match("www","www.baidu.com").span());
print(re.match("www","www.baidu.com"));
print(re.match("com","www.baidu.com"));

line = "Cats are smarter than dogs";
'''
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I);

if matchObj:
    print("matchObj.group() : ",matchObj.group());
    print("matchObj.group(1) : ",matchObj.group(1));
    print("matchObj.group(2) : ",matchObj.group(2));
else:
    print("no match!");
'''
print(re.search("www","www.baidu.com").span());
print(re.search("com","www.baidu.com").span());

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
