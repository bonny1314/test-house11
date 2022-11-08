import requests
from filetools import write_file, read_file


u="http://192.144.148.91:2333/login"
d={"username":"liuyun1","password":"a123456"} #jason的参数，数据格式必须字典
res=requests.post(url=u,jason=d)
print(res.text)

#保存token到文件夹
token=res.json()["data"]["token"]
write_file("token.txt",token)

#退出
t=read_file("token.txt")
u1="http://192.144.148.91:2333/logout"
h1={"Content-Type":"application/json","token":t} 
res1=requests.get(url=u1.headers=h1)
print(res1.text)
#提示先登录在退出，因为token无效

#可将token 取出再传到退出时的token中
#获取token res.json()["data"]["token"] 并用文件保存起来
