import multiprocessing

def Factorial(value):
    Fact = 1
    for i in range(1,value+1):
        Fact = Fact * i
    return Fact

def main():
    Data = []
    print("Enter the number of Element")
    size = int(input())

    print("Enter the each element")

    for i in range(size):
        no = int(input())
        Data.append(no)

    Ans = []

    p = multiprocessing.Pool()
    Ans = p.map(Factorial,Data)

    p.close()
    p.join()

    print(Ans)

if __name__ == "__main__":
    main()
