import threading
import time

def thread1_job():
    print('T1 start!\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 done!\n')

def thread2_job():
    print('T2 start!\n')
    print('T2 Done!\n')

def main():
    thread1 = threading.Thread(target=thread1_job,name='T1')
    thread2 = threading.Thread(target=thread2_job,name='T2')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('main done!');

if __name__=='__main__':
    main()
