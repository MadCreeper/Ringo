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


def sendMail(reveiver, validation):
    mimeMulti = MIMEMultipart('related')
    mimeMulti["From"] = f"sender_name<{mail_sender}>"
    mimeMulti["To"] = f"receiver_1_name<{reveiver}>"
    subjectContent = "SJTU Lingo —— 交大林檎验证码"
    mimeMulti["Subject"] = Header(subjectContent, 'utf-8')
    bodyContent = f"您好，这里是交大林檎\n您收到的验证码为：{validation}\n请在注册页面输入验证码，完成账号的注册"
    messageText = MIMEText(bodyContent, "plain", "utf-8")
    mimeMulti.attach(messageText)

    stp = smtplib.SMTP()
    stp.connect(mail_host, 25)
    stp.set_debuglevel(1)
    stp.login(mail_sender, mail_token)
    stp.sendmail(mail_sender, reveiver, mimeMulti.as_string())
    stp.quit()
