import re

mail_regex = r"^\S+@\S+\.\S+$"
sjtu_regex = r"^\S+@sjtu.edu.cn"

def check_SJTU_mail(email:str):
    if not re.match(sjtu_regex, email):
        return False
    return True

def check_mail_regex(email:str):
    if not re.match(mail_regex, email):
        return False
    return True
