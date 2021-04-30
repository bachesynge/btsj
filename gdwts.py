#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host="rm-wz9d8tk9eclp24pdfgo.mysql.rds.aliyuncs.com", user="gdyx_root",
                       password="*!xOKz%qekxQ", database="newgdyx", charset="utf8")
cursor = conn.cursor()

def sqlRun(sqlStr):
    return cursor.execute(sqlStr)

logObj=open("log.txt","w")

weituo = open('/Users/gaochao/Downloads/weituoshu.csv')
for i in weituo.readlines():
    i = i.strip()
    str = i.split(',')
    reqNumber=sqlRun("select * from gdyx_user where idcard='%s'"%(str[0]))
    if reqNumber == 1:
        u_id = cursor.fetchone()[0]
        if u_id:
            aut_Number = sqlRun("select * from gdyx_user_authorization where now_year=2020 and user_id='%s'"%(u_id))
            aut_num = cursor.fetchone()
            # print (aut_num)
            # print(aut_num[8])
            # print(str[2])
            # print(aut_num[9])
            # print(str[1])
            if aut_Number <1:
                logObj.write(str[0]+',没有\n')
                logObj.flush()
                print (str[0]+'没有')
                continue

            if aut_num[8]==str[2] and aut_num[9]==str[1]:
                #print (str[0] + '-' + str[1] + '-' + str[2])
                logObj.write(str[0]+',相同\n')
                logObj.flush()
                print (str[0]+'相同')
            else:

                # print (aut_num[9])
                # print (str[1])
                # print (aut_num[8])
                # print (str[2])
                # print (str[0] + '-' + str[1] + '-' + str[2])
                # logObj.write(str[0]+',不同,'+aut_num[8]+','+aut_num[9]+','+str[1]+','+str[2]+'\n')
                # logObj.flush()
                print (str[0]+',不同,'+aut_num[8]+','+aut_num[9]+','+str[1]+','+str[2]+'\n')
                exit()
        #reqNumber_2 = sqlRun("select * from gdyx_user_authorization where u_id='"+str(u_id)+"' and `check_pass_time` = '2020-12-31 23:59:59'  ")

    else:
        logObj.write(str[0]+',暂无用户\n')
        logObj.flush()
        print(str[0]+'暂无用户')
        #print("Error hnyx_user"%(i,reqNumber))
logObj.close()
cursor.close()
conn.close()