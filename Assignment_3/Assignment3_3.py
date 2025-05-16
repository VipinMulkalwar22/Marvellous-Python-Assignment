def Minimum(value):
    min = value[0]
    for i in range(len(value)):
        if(value[i] < min):
            min = value[i]

    return min

def main():
    Data= []
    print("Enter the number of element :")
    size = int(input())

    print("Enter each element :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    min = Minimum(Data) 

    print("Minimum is : ", min)

if __name__ == "__main__":
    main()   