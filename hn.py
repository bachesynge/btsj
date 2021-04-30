import csv
import os
import xlrd

def read_xlrd():

    # a = '312321312x'
    # b = '3213213C'
    # print(a.upper())
    # print(b.upper())
    # exit()
    file_path1 = '/Users/gaochao/btsj/python/h11.xls'
    file_path2 = '/Users/gaochao/btsj/python/h2.xlsx'
    data = xlrd.open_workbook(file_path1)
    data2 = xlrd.open_workbook(file_path2)
    table = data.sheet_by_index(0)
    table2 = data2.sheet_by_index(0)
    end_arr = {}
    for rowNum2 in range(table2.nrows):
        rowVale2 = table2.row_values(rowNum2)
        end_arr[str(rowVale2[3].lstrip())] = rowVale2[2]

    for rowNum in range(table.nrows):
        rowVale = table.row_values(rowNum)
        if rowVale[2].strip().upper() in end_arr:
            #pass
            print(rowVale[0], '--', rowVale[1], '--', rowVale[2], '--', rowVale[3])
        else:
            #pass
            print('1111111111111', rowVale[0], '--', rowVale[1], '--', rowVale[2], '--', rowVale[3])


    # for rowNum in range(table.nrows):
    #     rowVale = table.row_values(rowNum)
    #     end_arr[rowVale[2].lstrip()]= rowVale[0]

    # for rowNum2 in range(table2.nrows):
    #     rowVale2 = table2.row_values(rowNum2)
    #     if rowVale2[3] not in end_arr:
    #         print(str(int(rowVale2[0])),'--',str(int(rowVale2[1])),'--',rowVale2[2],'--',rowVale2[3])
    #     else:
    #         print(11111111)

        #end_arr[rowVale[2].lstrip()]= rowVale[0]

    #print (end_arr)

    #     rowVale = table.row_values(rowNum)
    #     for colNum in range(table.ncols):
    #         if rowNum > 0 and colNum == 0:
    #             print(int(rowVale[0]))
    #         else:
    #             print(rowVale[colNum])
    #     print("---------------")

    # if判断是将 id 进行格式化
    # print("未格式化Id的数据：")
    # print(table.cell(1, 0))
    # 结果：number:1001.0


if __name__ == '__main__':

    read_xlrd()