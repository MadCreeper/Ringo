import smtplib
import email

from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = "smtp.qq.com"

mail_sender = "lingo_sjtu@qq.com"

mail_token = "muwnanuvchkpdfcd"


def sendMail(receiver, validation, username):
    mimeMulti = MIMEMultipart('related')
    mimeMulti["From"] = f"SJTU Ringo 交大林擒<{mail_sender}>"
    mimeMulti["To"] = f"{username}<{receiver}>"
    subjectContent = "SJTU Lingo —— 交大林檎验证码"
    mimeMulti["Subject"] = Header(subjectContent, 'utf-8')
    bodyContent = f"{username}先生/小姐，您好。\n这里是交大林檎线上互助平台。\n\n请对您的账户{receiver}使用如下验证码\n验证码：{validation}\n\n若验证码的申请非您本人操作，可忽略这篇邮件，其他人可能错误地键入了您的电子邮箱地址。"

    messageText = MIMEText(bodyContent, "plain", "utf-8")
    mimeMulti.attach(messageText)

    stp = smtplib.SMTP()
    stp.connect(mail_host, 25)
    stp.set_debuglevel(0)
    stp.login(mail_sender, mail_token)
    stp.sendmail(mail_sender, receiver, mimeMulti.as_string())
    stp.quit()
