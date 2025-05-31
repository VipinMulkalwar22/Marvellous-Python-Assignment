import threading

def Display(no):
    for i in range(1,no+1,1):
        print(i)

def DisplayRev(no):
    for i in range(no,0,-1):
        print(i)

def main():

    T1 = threading.Thread(target=Display,args=(50,))
    T2 = threading.Thread(target=DisplayRev,args=(50,))

    T1.start()
    T1.join()
    T2.start()
    T2.join()

    print("Exit of Main Thread")

if __name__ == "__main__":
    main()  