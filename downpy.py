import csv
import urllib
from urllib.request import urlretrieve

#import requests
import os

file_path = '/Users/gaochao/btsj/python/h_order/'

f = csv.reader(open('/Users/gaochao/btsj/python/h_order/111query_result.csv','r'))


def down(_save_path, _url):
    try:
        print(_url)
        print(_save_path)
        urllib.urlretrieve(_url, _save_path)
    except:
        print
        '\nError when retrieving the URL:', _save_path


for i in f:
    url = i[13]
    print(i[4])
    file_path_h = file_path+str(i[7])+str(i[8])
    if not os.path.exists(file_path_h):
        os.mkdir(file_path_h)


    d_img1 = file_path_h+'/'+i[13][-17:]
    d_img2 = file_path_h+'/'+i[14][-17:]
    d_img3 = file_path_h+'/'+i[16][-17:]
    d_img4 = file_path_h+'/'+i[17][-17:]
    d_img5 = file_path_h+'/'+i[18][-17:]
    d_img6 = file_path_h+'/'+i[19][-17:]
    d_img7 = file_path_h+'/'+i[21][-17:]
    d_img8 = file_path_h+'/'+i[22][-17:]
    print(i[7])
    print(i[13])


    if i[13] and i[13]!='NULL':
        urlretrieve(i[13],d_img1)
    if i[14] and i[14]!='NULL':
        urlretrieve(i[14],d_img2)
    if i[16] and i[16]!='NULL':
        urlretrieve(i[16],d_img3)
    if i[17] and i[17]!='NULL':
        urlretrieve(i[17],d_img4)
    if i[18] and i[18]!='NULL':
        urlretrieve(i[18],d_img5)
    if i[19] and i[19]!='NULL':
        urlretrieve(i[19],d_img6)
    if i[21] and i[21]!='NULL':
        urlretrieve(i[21],d_img7)
    if i[22] and i[22]!='NULL':
        urlretrieve(i[22],d_img8)
    '''
    down(d_img2,i[14])
    down(d_img3,i[16])
    down(d_img4,i[17])
    down(d_img5,i[18])
    down(d_img6,i[19])
    down(d_img7,i[21])
    down(d_img7,i[22])
    '''
