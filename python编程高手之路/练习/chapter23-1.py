from threading import Thread
from multiprocessing import Process
import time


def countdown():
    """
    计算密集型运行结果：
    多进程执行时间：10.129732847213745
    多线程执行时间:29.21283221244812
    """
    s = 0
    for i in range(100000000):
        s += i


def countdown1():
    """
    I/O密集型执行的时间：
    多进程执行时间：5.178117752075195
    多线程执行时间:5.0029191970825195
    :return:
    """
    x = 1+2
    time.sleep(5)


if __name__ == '__main__':
    t_list = []
    start = time.time()
    for i in range(4):
        t = Process(target=countdown1)
        t_list.append(t)
        t.start()
    for i in t_list:
        t.join()
    end = time.time()
    print('多进程执行时间：'+str(end-start))

    t_list = []
    start = time.time()
    for i in range(4):
        t = Thread(target=countdown1)
        t_list.append(t)
        t.start()
    for i in t_list:
        t.join()
    end = time.time()
    print('多线程执行时间:'+str(end - start))