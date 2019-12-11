# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 20:11

from BeautifulReport import BeautifulReport
import unittest
import time

discover=unittest.defaultTestLoader.discover('../case',pattern='*_case.py')
times=time.strftime('%Y%m%d%H%M%S')
filename=times+'result.html'
BeautifulReport(discover).report('测试报告',filename=filename,report_dir='.')