import multiprocessing as mp

def job(x):
    return x*x

if __name__=='__main__':
    pool = mp.Pool()
    res = pool.map(job,range(10))
    print res
    res = pool.apply_async(job,(2,))
    print res.get()
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print [res.get() for res in multi_res]
