#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
#
# conn = pymysql.connect(host="rm-wz9d8tk9eclp24pdfgo.mysql.rds.aliyuncs.com", user="gdyx_root",
#                        password="*!xOKz%qekxQ", database="newgdyx", charset="utf8")

conn = pymysql.connect(host="ff6z2surq5623kdae994-rw4rm.rwlb.rds.aliyuncs.com", user="newcrm",
                       password="J4EyE9qnd9Mti9AV", database="crm", charset="utf8")
cursor = conn.cursor()

def sqlRun(sqlStr):
    return cursor.execute(sqlStr)

weituo = open('/Users/gaochao/Downloads/1118.csv')
for i in weituo.readlines():
    #print(i)
    i = i.strip()
    strs = i.split(',')
    #print(strs[3])
    reqNumber = sqlRun("select * from crm_tl2crm where phone1=%s " % (strs[3][1:12]))
    if reqNumber > 0:
        #如果存在手机号 输出错误
        print ('存在', strs[3][1:12])
        continue
    else:
        print(strs[3][1:12])
    #将数据插入用户表
    #print (reqNumber)
    add_user_sql = "insert into crm_tl2crm(owner_id,creater_id,phone1,create_time,owner_time)values(2475, 2475, '%s',1605066858,1762833258)" % (strs[3][1:12])
    reqNumber = sqlRun(add_user_sql)
    conn.commit()
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

"(" + str(i[0]) + "," + str(i[5]) + "," + str(i[35]) + "," + str(i[16]) + "," + str(i[39]) + "," + str(
    i[27]) + "," + str(i[12]) + "," + str(i[2]) + "," + str(i[1]) + "," + str(i[24]) + "," + str(i[25]) + "," + str(
    i[46]) + "," + str(i[18]) + "," + str(i[19]) + "," + str(i[43]) + "," + str(i[42]) + "," + str(i[6]) + "," + str(
    i[28]) + "," + str(i[29]) + "," + str(i[15]) + "," + str(i[11]) + "," + str(i[40]) + "," + str(i[48]) + "," + str(
    i[44]) + "," + str(i[48]) + "," + str(i[9]) + "," + str(i[22]) + "," + str(i[20]) + "," + str(i[23]) + "," + str(
    i[37]) + "," + str(i[10]) + "," + str(i[7]) + "," + str(i[8]) + ")"