#方法的定义

def checkname(username):
    """
    要求账号长度是5-8位,并且账号必须小写开头1
    """
    if len(username) >=5 and len(username) <=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
         print("ok")
        else:
            print("输入的首个账号必须为小写字母")
    else:
     print("输入的账号长度不符合规范")