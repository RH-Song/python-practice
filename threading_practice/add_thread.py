import threading

def thread_job():
    print('This is an added Thread the number of which is %s'
            % threading.current_thread())

def main():
    add_thread = threading.Thread(target=thread_job)
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())

if __name__=='__main__':
    main()
