import threading
import time

def Display():
    for i in range(1,6,1):
        print(i)

def main():

    T1 = threading.Thread(target=Display)
    T2 = threading.Thread(target=Display)
    T3 = threading.Thread(target=Display)
    T1.start()
    time.sleep(10)
    T2.start()
    time.sleep(10)
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()