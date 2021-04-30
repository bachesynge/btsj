#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host="rm-wz9d8tk9eclp24pdfgo.mysql.rds.aliyuncs.com", user="gdyx_root",
                       password="*!xOKz%qekxQ", database="newgdyx", charset="utf8")
cursor = conn.cursor()

def sqlRun(sqlStr):
    return cursor.execute(sqlStr)

weituo = open('/Users/gaochao/Downloads/wts97.csv')
for i in weituo.readlines():
    i = i.strip()
    str = i.split(',')
    #print(str)
    reqNumber=sqlRun("select * from gdyx_user where idcard='%s'"%(str[0]))
    aut_num = cursor.fetchone()
    #print(aut_num[0])
    if reqNumber == 1:
        gdyx_user_authorizations = sqlRun("select * from `gdyx_user_authorization` where `update_time`<'2020-05-20' and now_year=2020 and user_id='%s'" % (aut_num[0]))
        gdyx_user_authorization = cursor.fetchone()
        if gdyx_user_authorizations == 1:
            u_info = list(gdyx_user_authorization)
            #print((gdyx_user_authorization))
            update_sql = "update `gdyx_user_authorization` set company_idcard='"+str[2]+"', company_name='"+str[3]+"' where id=%d" % (gdyx_user_authorization[0])
            reqNumber = sqlRun(update_sql)
            conn.commit()
            #update_sql = "update `gdyx_user_authorization` set company_idcard='"+str[2]+"', company_name='"+str[3]+"' where id="+str(gdyx_user_authorization[0])
            print (update_sql)
            #update_sql = "update `gdyx_user_authorization` set company_idcard='"+str(gdyx_user_authorization[0])+"', company_name='"+str(gdyx_user_authorization[0])+"' where id="+str(gdyx_user_authorization[0])


    else:
        print(str[0]+'暂无用户')

        #print("Error hnyx_user"%(i,reqNumber))
cursor.close()
conn.close()