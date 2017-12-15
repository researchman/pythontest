'''
    本模块实现统计丢失ct数及详细丢失的ct号
'''
import io
import deal_file

#打开源文件
fd_read = open("D:\\log\\10.log", "r")
#打开保存结果的文件
fd_write = open("D:\log\\result.log", "w")

#读取文件中一行的内容
line_content = fd_read.readline()

ct = 0
#循环读取文件内容
while line_content:
    #读取ct值
    ct_value = deal_file.get_value_from_file(line_content, deal_file.Numbers.NINE.value) #deal_file.Numbers.ONE.value
    #去掉字符串中的空格
    ct_value = ct_value.strip()
    #将字符串数字转为整数
    cur_ct = int(ct_value)
    #如果相邻ct中缺失了ct数，则记录并写入文件中
    if (cur_ct - ct > 1) and (ct != 0):
        for i in range(ct + 1, cur_ct, 1):
            #print(i);
            sv = str(i) + "\r\n"
            fd_write.write(sv)
            fd_write.flush()
        pass
    #更新最新的ct值
    ct = cur_ct
    #读取下一行内容
    line_content = fd_read.readline()
#关闭源文件
fd_read.close()
#关闭结果保存文件
fd_write.close()