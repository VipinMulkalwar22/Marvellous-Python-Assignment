import time
import threading
import multiprocessing

def Addition(value):
    sum = 0
    for i in range(1,value+1):
        sum =sum + i
    print("Addition is",sum)

def main():
    start_time = time.time()
    Addition(10000000)
    end_time = time.time()
    print("Total Time for normal fuctions is {0}".format(end_time-start_time))
    
    start_time = time.time()
    T1 = threading.Thread(target=Addition,args=(10000000,))
    T1.start()
    T1.join()
    end_time = time.time()
    print("Total Time for Threading is {0}".format(end_time-start_time))

    start_time = time.time()
    P1 = multiprocessing.Process(target=Addition,args=(10000000,))
    P1.start()
    P1.join()
    end_time = time.time()
    print("Total Time for Multiprocessing is {0}".format(end_time-start_time))


if __name__ == "__main__":
    main()