import requests      #固定
from dbtools import query

url=“http://192.144.148.91:2333/get_title_img?num=3”  #存信息要用字符串 
res=resquest.get(url)  #requests.get(url) 调用get方法请求当前的接口地址  get类型
print(res.text)             #res.text接口返回值

#判断状态码
assert res.status_code=200 
assert res.json()["status"]==200  #res.jason()把结果编程字典格式


#查数据库
id=res.json()[0]["id"]
sql="select * from t_title_image where id='{}'".format(id)
res=query(sql)
assert len(res)==1
print("测试用例执行成功")