#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from multiprocessing import Pool
import time, threading
import os

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance -n 

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('threading %s ended.' % threading.current_thread().name)

def run_proc(name):
    print('Run child process %s (%s) ...' % (name, os.getpid()) )

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool(6)
#    for i in range(7):
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join()
#    print('All subprocesses done.')
#
#    print('thread %s is running...' % threading.current_thread().name)
#    t = threading.Thread(target=loop, name='LoopThread')
#    t.start()
#    t.join()
#    print('thread %s ended.' % threading.current_thread().name)
#
#    print('Parent process %s.' % os.getpid())
#    p = Pool(6)
#    for i in range(7):
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join()
#    print('All subprocesses done.')
#
#    print('Process (%s) start ...', os.getpid())
#    pid = os.fork()
#    if pid == 0:
#        print('I am child process (%s) and my parent is %s.', os.getpid(), os.getppid())
#    else:
#        print('I (%s) just created a child process (%s)', os.getpid(), pid)
#
#    print('Parent process %s .' % os.getpid())
#    p = Process(target=run_proc, args=('test',))
#    print('Child process will start.')
#    p.start()
#    p.join()
#    print('Child process end.')
#
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

