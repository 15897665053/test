import collections

from fastapi import FastAPI
from pydantic import BaseModel
import pymssql
import json
import uvicorn as uvicorn

app = FastAPI()


class People(BaseModel):
    EmpNo: str


@app.post('/api/insert')
def insert(people: People):
    empno = people.EmpNo

    conn = pymssql.connect(host='192.168.1.143', user='sa', password='redf@2021', database='D1_2012')
    # 游标
    cur = conn.cursor()

    cur.execute("select id,EmpNO from AttOverTime    where EmpNo='" + empno + "' order by YYMMDD desc")
    rows = cur.fetchall()

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["id"] = row[0]
        d["EmpNO"] = row[1]

        objects_list.append(d)

    Jsonstring = json.loads(json.dumps(objects_list))
    # 如果是插入、删除、更新语句切记要写提交命令con.commit()

    ren = {'msg': '请求成功', 'msg_code': 0, 'JsonData': Jsonstring}
    cur.close()
    conn.close()
    return ren
