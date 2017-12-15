import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "zhuyunfei@beijingyongan.com"
receivers = ["57323330@qq.com","12603856@qq.com"]    #137232613

#第三方smtp服务
mail_host = "smtp.exmail.qq.com";
mail_user = "zhuyunfei@beijingyongan.com";
mail_pass = "z123456789~Z";

#message = MIMEText("宋亚娇，女士：我们正式的通知您，您已成功通过本公司算法工程师的面试，欢迎您加入Google中国研发中心。","plain","utf-8");
'''
#2.发送html页面
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
""";
message = MIMEText(mail_msg,"html","utf-8");
'''
#3.发送附件
message = MIMEMultipart();

#公用部分
message["From"] = Header("Google中国 HR","utf-8");
message["To"] = Header("宋亚娇","utf-8");
subject = "Google 中国研发部-算法工程师";
message["Subject"] = Header(subject,"utf-8");


#3.发送附件
message.attach(MIMEText("这是菜鸟教程Python 邮件发送测试……","plain","utf-8"));
#构造附件1
att1 = MIMEText(open('db_test.py', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="db_test.py"'
message.attach(att1)
#构造附件2
att1 = MIMEText(open('server.py', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="s.txt"'
message.attach(att1)

try:
    #本地smtp服务
    #smtpObj = smtplib.SMTP("localhost");
    #第三方smtp服务
    smtpObj = smtplib.SMTP();
    smtpObj.connect(mail_host,25);
    smtpObj.login(mail_user,mail_pass);
    #这里的receivers采用list的方式，遍历其就可以实现群发的效果了
    smtpObj.sendmail(sender,receivers,message.as_string());
    print("邮件发送成功!");
except smtplib.SMTPException:
    print("Error: 无法发送邮件");
