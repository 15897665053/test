import collections

import pymssql
import json

conn=pymssql.connect(host='192.168.1.143',user='sa',password='redf@2021',database='D1_2012')
#游标
cur=conn.cursor()
cur.execute("select id,EmpNO from AttOverTime    where EmpNo='A001334' order by YYMMDD desc")

rows = cur.fetchall()

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["EmpNO"] = row[1]

    objects_list.append(d)


j = json.dumps(objects_list)
#如果是插入、删除、更新语句切记要写提交命令con.commit()
print (j)
cur.close()
conn.close()