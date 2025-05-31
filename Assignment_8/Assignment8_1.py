import threading

def Even(no):
    for i in range(2,no,2):
        print("Even=",i)

def Odd(no):
    for i in range(1,no,2):
        print("Odd=",i)

def main():

    T1=threading.Thread(target=Even,args=(20,))
    T2=threading.Thread(target=Odd,args=(20,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()