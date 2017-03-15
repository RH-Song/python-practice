import multiprocessing as mp
import threading as mt
import time

def job(q):
    res = 0
    for i in range(1000000):
        res = i + i**2 + i**3
    q.put(res)

def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res = i + i**2 + i**3
    print 'normal', res

def mul_thread():
    t = mp.Queue()
    t1 = mt.Thread(target=job,args=(t,))
    t2 = mt.Thread(target=job,args=(t,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    res1 = t.get()
    res2 = t.get()
    print 'multithreading', res1+res2

def mul_process():
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    res1 = q.get()
    res2 = q.get()
    print 'mutltiprocessing', res1+res2

if __name__=='__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print 'normal time', st1-st
    mul_thread()
    st2 = time.time()
    print 'multithreading', st2-st1
    mul_process()
    st3 = time.time()
    print 'mutlprocesing', st3-st2
