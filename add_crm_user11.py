#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
#
# conn = pymysql.connect(host="rm-wz9d8tk9eclp24pdfgo.mysql.rds.aliyuncs.com", user="gdyx_root",
#                        password="*!xOKz%qekxQ", database="newgdyx", charset="utf8")

conn = pymysql.connect(host="ff6z2surq5623kdae994-rw4rm.rwlb.rds.aliyuncs.com", user="newcrm",
                       password="J4EyE9qnd9Mti9AV", database="ocrm", charset="utf8")
cursor = conn.cursor()

def sqlRun(sqlStr):
    return cursor.execute(sqlStr)

weituo = open('/Users/gaochao/Downloads/21class.csv')
for i in weituo.readlines():
    print(i)
    # i = i.strip()
    # strs = i.split(',')
    # #print(strs[2])
    # reqNumber = sqlRun("select * from 5kcrm_user where user_id='%s' " % (str(i)))
    # userinfo = cursor.fetchone()
    # print(userinfo[4])
    # if reqNumber > 0:
    #     #如果存在手机号 输出错误
    #     #print ('存在', strs[2])
    #     print(userinfo[1])
    #     continue
    # else:
    #     print('1')
    #将数据插入用户表
    #print (reqNumber)
    #
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