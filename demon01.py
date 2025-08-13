"""
# print('你好')  
a=['朱元璋','陈友谅','张士诚','徐达','常有遇']
b=['舰船','渔船']
#a.extend(b)
#b.clear()
#print(a+b)
a.remove('常有遇')
print(a)
"""

#字典
a={'name':"小房",0:'sad','age':25}
#取值
print(a["name"])
#新增
a['height']='185'
print(a)
#修改
a[0]='sss'
print(a)

b=a.get("name")
print(b)
print(a)

a.update(asd=145)
print(a)

print("----------------")

#print(a.get('name1'))
#print(a['name1'])

#数组和字典的删除
del a['name']
print(a)

"""
练习:获取用户输入的个人信息，并且储存到字典中
     信息包括name,age,sex
     """

a=input("请输入姓名：")
b=input("请输入性别：")
c=input("请输入年龄：")
d={}

#d={"name":a,"gender":b,"age":c}
#d.update(name=a,sex=b,age=c)
d["name:"]=a
d["age:"]=b
d["sex:"]=c
print(d)