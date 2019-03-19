import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
_user = "1021593619@qq.com"
_pwd = "nnofbzungdqwbbdd"
_to = ["769975825@qq.com", " 731135871@qq.com", " 846266153@qq.com"]

#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "周报"
msg["From"] = _user
msg["To"] = _to

#---这是文字部分---

# part = MIMEText("")
# msg.attach(part)

#---这是附件部分---

#txt类型附件
part = MIMEApplication(open('D:\Download\软件部周报.docx', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="软件部周报.docx")
msg.attach(part)

#xlsx类型附件
#part = MIMEApplication(open('foo.xlsx','rb').read())
#part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
#msg.attach(part)
#
##jpg类型附件
#part = MIMEApplication(open('foo.jpg','rb').read())
#part.add_header('Content-Disposition', 'attachment', filename="foo.jpg")
#msg.attach(part)
#
##pdf类型附件
#part = MIMEApplication(open('foo.pdf','rb').read())
#part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
#msg.attach(part)
#
##mp3类型附件
#part = MIMEApplication(open('foo.mp3','rb').read())
#part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
#msg.attach(part)
for to in _to:
    s = smtplib.SMTP("smtp.qq.com", timeout=30)  #连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)  #登陆服务器
    s.sendmail(_user, to, msg.as_string())  #发送邮件
    s.close()