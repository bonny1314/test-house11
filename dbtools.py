#pymysql
#select method
import pymysql #guding sentence
def query(sq1): #sql  str
    db=pymysql.connect(host="192.144.148.91",user="root",password="Pan331214",db="zhangli")
    cur=db.cursor()
    cur.execute(sql)
    res=cur.fetchall()  #get all results
    db.close()
    return res

#insert  delete  update
def commit(sql)
    db=pymysql.connect(host="192.144.148.91",user="root",password="Pan331214",db="zhangli")
    cur=db.cursor()
    cur.execute(sql)
    res=cur.fetchall()  #get all results
    db.commit() # changed word  to be saved
    db.close()
    
if _name_ == "_mian_" :               # zhijie yunxingde py wenjian, cai tiaojian chengli
    xiugai_sql = "update t_user set username='9527' when id=123"
    commit(xiugai_sql)

    s = "select * from t_user where id=2" #sql transfer str type
    r = query(s)
    print(r)


