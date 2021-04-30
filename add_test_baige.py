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

#reqNumber = sqlRun("select FROM_UNIXTIME(u.create_time,'%Y') as addtime, u.customer_id,u.creator_role_id,u.name,u.classId,u.crm_cfbtmg,u.uniqueCode,u.crm_kzpedx,u.crm_aknsea FROM 5kcrm_customer as u INNER JOIN 5kcrm_receivables as o on u.customer_id = o.customer_id where  u.classId in (138,745,790,872,942,979,998,1001,1131,1137,1195,1196,1197,1676,1878,1891,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1914,1915,1922,1923,1924,2005,2054,2215,2269,2270,2271,2278,2279,2281,2282,2283,2284,2705,2706,2717,4042,4205,4250,4251,4252,4253,4254,4255,4256,4257,4258,4259,4260,4261,4262,4263,4264,4265,4266,4267,4268,4269,4270,4271,4272,4273,4274,4291,4292,4332) ")
reqNumber = sqlRun("select FROM_UNIXTIME(u.create_time,'%Y') as addtime, u.customer_id FROM 5kcrm_customer as u INNER JOIN 5kcrm_receivables as o on u.customer_id = o.customer_id where  u.classId in (95,96,97,98,99,100,101,102,103,104,108,110,111,141,142,213,214,226,227,228,229,242,254,255,262,263,266,267,303,304,305,306,310,311,312,323,324,327,357,358,376,377,428,447,448,474,475,479,480,481,482,483,494,495,498,499,516,517,618,619,620,621,623,624,630,631,635,636,637,638,641,642,645,646,720,721,722,723,746,747,748,749,750,751,753,754,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,780,793,794,795,796,867,869,870,907,908,910,928,933,934,935,936,954,955,956,957,994,995,1002,1003,1006,1007,1023,1135,1136,1186,1187,1534,1535,1651,1652,1653,1654,1662,1663,1664,1665,1666,1667,1671,1672,1674,1677,1686,1696,1697,1698,1699,1701,1808,1809,1811,1812,1813,1814,1815,1819,1820,1821,1822,1831,1832,1833,1834,1835,1836,1838,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1879,1880,1881,1882,1885,1886,1889,1929,1937,1974,1975,1976,1977,1985,1986,1987,1988,1989,1990,1991,1992,2001,2002,2003,2006,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2043,2044,2063,2064,2092,2093,2172,2173,2226,2227,2229,2230,2286,2287,2288,2289,2469,2470,2471,2520,2521,2561,2562,2703,2704,2708,2709,2711,2712,2719,2720,2727,2728,2729,2730,2754,2755,2806,2807,2852,2853,2854,2855,2866,2868,2869,2977,2978,2979,2980,3649,3650,3651,3652,3733,3734,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3822,3823,3848,3849,3850,3851,3852,3853,3970,3971,3972,3973,3974,3975,3976,3977,3979,3981,3984,3985,3987,3989,3992,3996,4022,4070,4071,4074,4075,4076,4079,4081,4083,4084,4088,4089,4090,4092,4097,4098,4099,4100,4101,4102,4103,4104,4125,4126,4249,4289,4290,4333,4334,4335,4336,4337,4338,4368,4369,4370,4371,4372,4373,4424,4440,4441,4458,4459)")
user = cursor.fetchall()

for i in user:
    customer_id         = str(i[1] if i[1] is not None and i[1] is not '' else '')
    industry            = str(i[0] if i[0] is not None and i[0] is not '' else '')


    #print(i)
    add_user_sql = "update `5kcrm_customer` set industry='"+industry+"', crm_lnjwgg='药师' where customer_id="+customer_id
    #add_user_sql = "insert into 5kcrm_customer_yypczd(customer_id,name,industry,creator_role_id,classId,crm_cfbtmg,crm_kzpedx,owner_role_id,uniqueCode,crm_aknsea,crm_lnjwgg)values('"+customer_id + "','" + name + "','" + industry + "','" + creator_role_id + "','" + classId + "','" + crm_cfbtmg + "','" + crm_kzpedx + "','" + creator_role_id + "','" + uniqueCode+ "','" + crm_aknsea + "','健康管理师')"


    # if phone_1== 'NULL':
    #     continue
    # add_user_sql = "insert into hd_crm_customer(customer_id,name,is_lock,deal_status,deal_time,level,source,create_user_id,owner_user_id,address,detail_address,follow,create_time,update_time,source_level_one,source_level_two,sex,consult_project,consult_specialty,last_active_project,education,clue_type,follow_up_count,wechat_number,id_card,nation,mail,qq_number,phone_1,phone_2)values('"+customer_id + "','" + name + "','" + is_lock + "','" + deal_status + "','" + deal_time + "','" + level + "','" + source + "','" + create_user_id + "','" + owner_user_id + "','" + address + "','" + detail_address + "','" + follow + "','" + create_time + "','" + update_time + "','" + source_level_one + "','" + source_level_two + "','" + sex + "','" + consult_project + "','" + consult_specialty + "','" + last_active_project + "','" + education + "','" + clue_type + "','" + follow_up_count + "','" + wechat_number + "','" + id_card + "','" + nation + "','" + mail + "','" + qq_number + "','" + phone_1 + "','" + phone_2 + "')"
    try:
        #print('ok|')
        reqNumber = sqlRun(add_user_sql)
        conn.commit()
    except:
        print('err|'+add_user_sql)


cursor.close()
conn.close()