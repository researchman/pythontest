import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "zhuyunfei@beijingyongan.com"
receivers = ["57323330@qq.com","12603856@qq.com"]    #137232613

#第三方smtp服务
mail_host = "smtp.exmail.qq.com";
mail_user = "zhuyunfei@beijingyongan.com";
mail_pass = "z123456789~Z";

message = MIMEMultipart("related");
#公用部分
message["From"] = Header("Google中国 HR","utf-8");
message["To"] = Header("宋亚娇","utf-8");
subject = "Google 中国研发部-算法工程师";
message["Subject"] = Header(subject,"utf-8");

msgAlt = MIMEMultipart("alternative");
message.attach(msgAlt);
#2.发送带图片的html页面
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
""";
message.attach(MIMEText(mail_msg,"html","utf-8"));

#指定图片为当前目录
fp = open("1371.gif","rb");
msgImage = MIMEImage(fp.read());
fp.close();
msgImage.add_header("Content-ID","image1");
message.attach(msgImage);

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
