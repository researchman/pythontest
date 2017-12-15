from enum import Enum
# 从content中获取位置为index的ct值
def get_value_from_file(content, index):
    value = 0
    split_content = content.split(",")
    meta = split_content[index]
    vs = meta.split(":")
    value = vs[1]

    return str(value)

#枚举的定义
Numbers = Enum('Numbers',('ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN'))
#枚举的使用
#print(Numbers.ONE.value);

'''
def write_to_file(fd,value):
    fd.write(value);

    pass;
'''