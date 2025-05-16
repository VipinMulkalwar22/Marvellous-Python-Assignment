def Maximum(value):
    max = value[0]
    for i in range(len(value)):
        if(value[i] > max):
            max = value[i]

    return max

def main():
    Data= []
    print("Enter the number of element :")
    size = int(input())

    print("Enter each element :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    max = Maximum(Data) 

    print("Maximum is : ", max)

if __name__ == "__main__":
    main()   