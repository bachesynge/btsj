#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
#
# conn = pymysql.connect(host="rm-wz9d8tk9eclp24pdfgo.mysql.rds.aliyuncs.com", user="gdyx_root",
#                        password="*!xOKz%qekxQ", database="newgdyx", charset="utf8")

conn = pymysql.connect(host="172.17.248.96", user="root",
                       password="root@123", database="test", charset="utf8")
cursor = conn.cursor()

def sqlRun(sqlStr):
    return cursor.execute(sqlStr)

reqNumber = sqlRun("select * from crm_tl2crm where student_id < 50000  ")
user = cursor.fetchall()

for i in user:
    customer_id         = str(i[0] if i[0] is not None and i[0] is not '' else '')
    name                = str(i[5] if i[5] is not None and i[5] is not '' else '')
    is_lock             = str(i[35] if i[35] is not None and i[35] is not '' else '')
    deal_status         = str(i[16] if i[16] is not None and i[16] is not '' else '')
    deal_time           = str(i[39] if i[39] is not None and i[39] is not '' else '')
    level               = str(i[27] if i[27] is not None and i[27] is not '' else '')
    source              = str(i[12] if i[12] is not None and i[12] is not '' else '')
    create_user_id      = str(i[2] if i[2] is not None and i[2] is not '' else '')
    owner_user_id       = str(i[1] if i[1] is not None and i[1] is not '' else '')
    address             = str(i[24] if i[24] is not None and i[24] is not '' else '')
    detail_address      = str(i[25] if i[25] is not None and i[25] is not '' else '')
    follow              = str(i[46] if i[46] is not None and i[46] is not '' else '')
    create_time         = str(i[18] if i[18] is not None and i[18] is not '' else '')
    update_time         = str(i[19] if i[19] is not None and i[19] is not '' else '')
    source_level_one    = str(i[43] if i[43] is not None and i[43] is not '' else '')
    source_level_two    = str(i[42] if i[42] is not None and i[42] is not '' else '')
    sex                 = str(i[6] if i[6] is not None and i[6] is not '' else '')
    consult_project     = str(i[28] if i[28] is not None and i[28] is not '' else '')
    consult_specialty   = str(i[29] if i[29] is not None and i[29] is not '' else '')
    last_active_project = str(i[15] if i[15] is not None and i[15] is not '' else '')
    education           = str(i[11] if i[11] is not None and i[11] is not '' else '')
    clue_type           = str(i[40] if i[40] is not None and i[40] is not '' else '')
    follow_up_count     = str(i[48] if i[48] is not None and i[48] is not '' else '')
    last_active_time    = str(i[44] if i[44] is not None and i[44] is not '' else '')
    active_count        = str(i[48] if i[48] is not None and i[48] is not '' else '')
    wechat_number       = str(i[9] if i[9] is not None and i[9] is not '' else '')
    id_card             = str(i[22] if i[22] is not None and i[22] is not '' else '')
    nation              = str(i[20] if i[20] is not None and i[20] is not '' else '')
    mail                = str(i[23] if i[23] is not None and i[23] is not '' else '')
    introducer_phone    = str(i[37] if i[37] is not None and i[37] is not '' else '')
    qq_number           = str(i[10] if i[10] is not None and i[10] is not '' else '')
    phone_1              = str(i[7] if i[7] is not None and i[7] is not '' else '')
    phone_2             = str(i[8] if i[8] is not None and i[8] is not '' else '')

    if phone_1== 'NULL':
        continue
    add_user_sql = "insert into hd_crm_customer(customer_id,name,is_lock,deal_status,deal_time,level,source,create_user_id,owner_user_id,address,detail_address,follow,create_time,update_time,source_level_one,source_level_two,sex,consult_project,consult_specialty,last_active_project,education,clue_type,follow_up_count,wechat_number,id_card,nation,mail,qq_number,phone_1,phone_2)values('"+customer_id + "','" + name + "','" + is_lock + "','" + deal_status + "','" + deal_time + "','" + level + "','" + source + "','" + create_user_id + "','" + owner_user_id + "','" + address + "','" + detail_address + "','" + follow + "','" + create_time + "','" + update_time + "','" + source_level_one + "','" + source_level_two + "','" + sex + "','" + consult_project + "','" + consult_specialty + "','" + last_active_project + "','" + education + "','" + clue_type + "','" + follow_up_count + "','" + wechat_number + "','" + id_card + "','" + nation + "','" + mail + "','" + qq_number + "','" + phone_1 + "','" + phone_2 + "')"
    try:
        print ('ok'+add_user_sql)
        # reqNumber = sqlRun(add_user_sql)
        # conn.commit()
    except:
        print('err'+customer_id)


cursor.close()
conn.close()