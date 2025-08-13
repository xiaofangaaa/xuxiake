#判断
"""
a=20
b=25
if a ==20:
    print("正确")   

if a>b:
    print("a比b大")
else:
    print("b比a大")
"""
"""
age= int(input("请输入你的年龄："))
if age > 60:
    print("j")
elif age > 30:
    print("k")
elif age > 20:
    print("l")
else:
    print("m")
#if age > 20 and age < 30:  (第一句也可这么写)
#    print("l")
"""
"""
a = "证券"
if a in ["交易类","证券"]:     #if a in "交易类,证券":
    print("1")
else:
    print("2")
"""
"""
a = input("请输入年龄：")
if a == "":
    print("输入不能为空！")
    exit()
if a in "0123456789":
    a = int(a)
else:
    print("请正确输入格式！")
    exit()
if a > 5:
    print("大")
else:
    print("小")
    """
"""
a = 1
if  type(a) is int:
    print("a是整数")
elif type(a) is str:
    print("a是字符串")
else:
    print("其他")
"""

#循环
#1.while 循环
"""
a = 1
while a <10:
    print("a小于10",a)
    a = a +2
"""
"""
利用判断和循环练习：
现有11个学生的成绩,需要录入系统中
分别是,A,B,C,D,E,F,G,H,I,J,k
并且名字和成绩要对应上
而且大于60和小于60的需要分开存放
"""

"""highscore = {}  #定义一个空字典，用来存储大于60分的信息
lowscore = {}   #定义一个空字典，用来存储小于60分的信息
studentlist = ["A","B","C","D","E","F","G","H","I","J","k"]
a = 0            #定义了一个变量，用来控制数组的下标变化
while a < len(studentlist):
    score = int(input("请输入"+studentlist[a]+"的成绩:"))
    if score < 60:
        lowscore[studentlist[a]]=score    #存到字典中
    else:
        highscore[studentlist[a]]=score
    a = a + 1
print("小于60的分数:",lowscore)
print("大于60的分数:",highscore)"""
 
"""
#2.for 循环
#遍历

#a = "资本"
a=['朱元璋','陈友谅','张士诚','徐达','常有遇']
for i in a:
    print(i,end=" ")

b = range(0,100,2)          #range(100)自动生成一个数列，list(range(100))转化为数组
for i in range(0,100,2) :   #步进/步长(0,100,2)后面的2，执行后就是 0,2,4，...,98
  print(i)

#练习打出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="  ")   #end 不换行
    print()  #起换行作用
"""
"""
练习1:
通过print打印,模拟一个红绿灯的功能，注意:红灯30次,绿灯35次,黄灯3次.
练习2:
使用代码,实现一个注册的功能.
用户输入账号和密码,要求账号长度是5-8位,密码6-12位,并且账号必须小写开头。
存储到字典中，{username:passward}

linght ={"红灯":30,"绿灯":35,"黄灯":3}
while True:
  for i in linght:
      for j in range(linght[i]):
          print(i,"倒计时还有",linght[i]-j,"秒")

          """
"""
username = input("请输入账号:")
passward = input("请输入密码：")
if len(username) >=5 and len(username) <=8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(passward) >=8 and len(passward) <=12:
            print("注册成功",{username:passward})
        else:
            print("密码长度不符合规范")
    else:
        print("输入的首个账号必须为小写字母")
else:
    print("输入的账号长度不符合规范")
"""







