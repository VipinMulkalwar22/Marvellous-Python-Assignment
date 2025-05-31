import threading

def Evenlist(value):
    sum = 0
    for i in range(0,len(value)):
        if(value[i] % 2 == 0):
            print("Even =", value[i])
            sum += value[i]
    print("Sum of Even Numbers is ", sum)

def Oddlist(value):
    sum = 0
    for i in range(0,len(value)):
        if(value[i] % 2 != 0):
            print("Odd =", value[i])
            sum += value[i]
    print("Sum of Odd Numbers is ", sum)

def main():
    print("Enter the number of Element")
    size = int(input())

    Data = []

    print("Enter each element")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print(Data)

    T1 = threading.Thread(target=Evenlist, args=(Data,))
    T2 = threading.Thread(target=Oddlist, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()