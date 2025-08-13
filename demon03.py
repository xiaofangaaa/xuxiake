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

a="7hjolk"
checkname(a)     

#def 方法的声明
#checkname 方法的名字
#username 方法的参数
#"""方法的说明"""
#4-8行是方法的逻辑代码

    
def sum(a,b):
    """
    这个方法的作用为两个数字的相加
    """
    if type(a) is int and type(b) is int:
     print(a+b)
    else:
        print("输入数据的类型不正确")

sum("5",58)

#用return返回值写
#作用：返回值，返回后可以对这个值进行其他的操作，而print不能
def sum(a,b):
    """
    这个方法的作用为两个数字的相加
    """
    if type(a) is int and type(b) is int:
        return a+b
    else:
         return "输入数据的类型不正确"
print(sum(2,3))


def checkname(username):
  if len(username) >=5 and len(username) <=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
         return True
        else:
            return"输入的首个账号必须为小写字母"
  else:
     return "输入的账号长度不符合规范"
  
username = input("请输入你的账号：")
password = input("请输入你的密码：")
if checkname(username) == True:
  if len(password) >=8 and len(password) <=12:
     print("注册成功！",{username:password})
  else:
     print("密码必须是8-12位!")   
else:
   print(checkname(username))