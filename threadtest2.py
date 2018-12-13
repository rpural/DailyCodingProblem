#! /usr/bin/python

import threading,time
x_lock = threading.Lock() # A lock for synchronizing access to x
     
COUNT = 10

def foo():
    global x
    global y
    global z
    x=0
    y=0
    z=0
    for i in xrange(COUNT):
        x_lock.acquire()
        #x += 1
        y += 1
        z += 1
        print x,y,z
        time.sleep(0.00001)
        x_lock.release()
        time.sleep(0.01)
     
def bar():
    global x
    global y
    global z
    for i in xrange(COUNT):
        x_lock.acquire()
        #x -= 1
        if( y==2 & z==2):
            print "h"
        elif(y==5):
            print "i"
     
     
        time.sleep(1)
        print x
        x_lock.release()
        time.sleep(0.01)
     
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)
t1.start()
t2.start()
t1.join()
t2.join()
