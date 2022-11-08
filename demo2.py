import requests from dbtools import query  #测试登录是否成功
u="http://192.144.148.91:2333/login"
d={"username":"liuyun","password":"a1234567"}  #post 类型 
res=requests.post(url=u.jason=d) #json 传输的文件格式必须是字典

assert res.status_code==200
assert res.json()["status"]==200
sql=="select * from t_user where username='{}'".format(d["username"])
assert len(query(sql))==1
 #查出用户信息只有一人)
 print("登录测试用例成功")