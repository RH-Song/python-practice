import multiprocessing as mp

def job(a,b):
    print a,b

if __name__=='__main__':
    # create start And join
    p1 = mp.Process(target=job,args=('Hello','MultiProcessing'))
    p1.start()
    p1.join()
