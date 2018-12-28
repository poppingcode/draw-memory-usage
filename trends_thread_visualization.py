#  _*_ coding:utf-8 _*_ 
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from visdom import Visdom
import numpy as np
import math
import os.path
import getpass
from sys import platform as _platform
from six.moves import urllib
import numpy as np
import psutil
import datetime
import os
import sys
import argparse
import time
def now_time_produce():
    now_time = str(datetime.datetime.now()).split('.')[0]
    #now_time_YMD =  now_time.split(' ')[0].split('-')[0]+now_time.split(' ')[0].split('-')[1]+now_time.split(' ')[0].split('-')[2]
    now_time_YMD =  now_time.split(' ')[0].split('-')[2]
    now_time_HMS =  now_time.split(' ')[1].split(':')[0]+now_time.split(' ')[1].split(':')[1]+now_time.split(' ')[1].split(':')[2]
    time_merge= int(now_time_YMD+now_time_HMS)
    return time_merge

#输入参数
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--thread', type=int, default = None)
args = parser.parse_args()
print("the thread is ")
print(args.thread)

#准备数据及数据处理

a = now_time_produce()

def thread_info():
    p = psutil.Process(args.thread)
    #print u'test',p.memory_info()
    #str1 =str("test pmem(rss=7533547520, vms=10033706373120, shared=4788461568, text=12247040, lib=0, data=3159523328, dirty=0)")
    str1 = str(p.memory_info())
    thread_info = str1.split('(')[1].split(')')[0].split(', ')
    rss = int(thread_info[0].split("rss=")[1])/1000000
    shared = int(thread_info[2].split("shared=")[1])/1000000
    return rss,shared

rss,shared = thread_info()
#draw
viz = Visdom(env=u'test')
assert viz.check_connection()
viz.close()
win = viz.line(X = np.array([a]), Y = np.array([rss]) , name='1')
viz.line(X = np.array([a]), Y = np.array([shared]) ,win=win,update="new", name='2')


while(1):
    rss,shared = thread_info()
    time_merge = now_time_produce()
    print(time_merge)
    viz.line(
        X= np.array([time_merge]),
        Y= np.array([rss]),
        win=win,
        name="1",
        update = 'append'
    )
    viz.line(
        X= np.array([time_merge]),
        Y= np.array([shared]),
        win=win,
        name="2",
        update = 'append'
    )
    time.sleep(1)
