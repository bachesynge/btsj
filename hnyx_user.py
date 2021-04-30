#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
#
# conn = pymysql.connect(host="rm-wz9d8tk9eclp24pdfgo.mysql.rds.aliyuncs.com", user="gdyx_root",
#                        password="*!xOKz%qekxQ", database="newgdyx", charset="utf8")

conn = pymysql.connect(host="rm-uf6b191832e7ckkvgoo.mysql.rds.aliyuncs.com", user="hnyxpro",
                       password="832e7ckf6b191C", database="hnyx", charset="utf8")
cursor = conn.cursor()

def sqlRun(sqlStr):
    return cursor.execute(sqlStr)

weituo = open('/Users/gaochao/Downloads/hnyx_users.csv')
for i in weituo.readlines():
    i = i.strip()
    strs = i.split(',')
    #print(strs[1])
    reqNumber = sqlRun("select * from hnyx_stu where idcard='%s' " % (strs[1]).strip())
    #print("select * from hnyx_stu where idcard='%s' " % (strs[1]).strip())
    if reqNumber > 0:
        #如果存在手机号 输出错误
        print ('ok', strs[1])
    else:
        print('err', strs[1])
    #将数据插入用户表
    #print (reqNumber)
    #add_user_sql = "insert into crm_tl2crm(owner_id,creater_id,phone1,create_time,owner_time,detail_address,crm_source)values(2384, 2384, '%s',1599702081,1615340480,'%s',9)" % (strs[1],strs[2])
    #print (add_user_sql)
    # reqNumber = sqlRun(add_user_sql)
    # conn.commit()
    #     gdyx_user_authorizations = sqlRun("select * from `gdyx_user_authorization` where `update_time`<'2020-05-20' and now_year=2020 and user_id='%s'" % (aut_num[0]))
    #     gdyx_user_authorization = cursor.fetchone()
    #     if gdyx_user_authorizations == 1:
    #         u_info = list(gdyx_user_authorization)
    #         #print((gdyx_user_authorization))
    #         update_sql = "update `gdyx_user_authorization` set company_idcard='"+str[2]+"', company_name='"+str[3]+"' where id=%d" % (gdyx_user_authorization[0])
    #         reqNumber = sqlRun(update_sql)
    #         conn.commit()
    #         #update_sql = "update `gdyx_user_authorization` set company_idcard='"+str[2]+"', company_name='"+str[3]+"' where id="+str(gdyx_user_authorization[0])
    #         print (update_sql)
    #         #update_sql = "update `gdyx_user_authorization` set company_idcard='"+str(gdyx_user_authorization[0])+"', company_name='"+str(gdyx_user_authorization[0])+"' where id="+str(gdyx_user_authorization[0])
    #
    #
    # else:
    #     print(str[0]+'暂无用户')

        #print("Error hnyx_user"%(i,reqNumber))
cursor.close()
conn.close()