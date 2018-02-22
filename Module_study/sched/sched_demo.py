#-*- coding:utf-8 -*-

"""
sched模块实现了一个时间调度程序，改调度程序可以通过单线程执行来处理按照时间尺度进行调度事件
通过调用scheduler.enter(delay, priority, func, args)函数，可以将一个任务添加到任务队列里，当指定的时间到了，就会执行任务（func函数）。
delay: 任务的间隔时间
priority:如果几个任务被调度到相同的时间执行，按照priority的增序执行这几个任务。
func: 要执行的函数
args: func的参数，如果是一个则（a,)，必须是元组形式

"""

import time, sched

s = sched.scheduler(time.time, time.sleep)

def event_func1():
   print 'func1 Time:', time.time()

def perform1(inc):
   s.enter(inc, 0, perform1, (inc,))
   event_func1()

def event_func2():
    print 'func2 Time', time.time()

def perform2(inc):
    s.enter(inc, 0, perform2, (inc,))
    event_func2()

def mymain(func, inc=2):
    if func == '1':
        s.enter(0, 0, perform1, (10,))
    if func == '2':
        s.enter(0, 0, perform2, (20,))

if __name__ == '__main__':
    mymain('1')
    mymain('2')
    s.run()






