# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 15:03

from selenium import webdriver
import xlrd

def getchrome():
    options=webdriver.ChromeOptions()
    options.add_argument('disabled-inforbars')
    driver=webdriver.Chrome(options=options)
    return driver

def get_table(tablename,Sheetname):
    data=xlrd.open_workbook('../data/'+tablename+'.xlsx')
    table=data.sheet_by_name(Sheetname)
    lis=[]
    #去表头
    for row in range(1,table.nrows):
        lis.append(table.row_values(row))
    return lis


if __name__ == '__main__':
    print(get_table('user','Sheet1'))
