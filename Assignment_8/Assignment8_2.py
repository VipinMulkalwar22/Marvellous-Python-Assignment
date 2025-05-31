import threading

def EvenFactors(value):
    sum = 0
    for i in range(1,int(value/2)+1):
        if (value % i == 0):
            if(i % 2 == 0):
                sum = sum + i
    print("Sum of Even Factors of Number is ",sum)

def OddFactors(value):
    sum = 0
    for i in range(1,int(value/2)+1):
        if (value % i == 0):
            if(i % 2 != 0):
                sum = sum + i
    print("Sum of odd Factors of Number is ",sum)

def main():
    print("Enter the number")
    no = int(input())

    T1 = threading.Thread(target=EvenFactors,args=(no,))
    T2 = threading.Thread(target=OddFactors,args=(no,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()