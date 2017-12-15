'''
from urllib import request;

response = request.urlopen("http://www.baidu.com/");    #打开网站
fi = open("project.txt","w");
page = fi.write(str(response.read()));
fi.close();
'''

import os;
import os.path;

ls = [];

def get_appoint_file(path,ls):
    file_list = os.listdir(path);
    try:
        for tmp in file_list:
            path_tmp = os.path.join(path,tmp);
            if True == os.path.isdir(path_tmp):
                get_appoint_file(path_tmp,ls);
            elif path_tmp[path_tmp.rfind('.')+1:].upper() == 'PY':
                ls.append(path_tmp);
    except PermissionError:
        pass

def main():
    while True:
        path = input("请输入路径：").strip();
        if os.path.isdir(path) == True:
            break;
    
    get_appoint_file(path,ls);
    print(ls);
    print(len(ls));

main();

