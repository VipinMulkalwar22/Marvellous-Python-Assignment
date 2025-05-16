def frequency(value,no):
    count = 0
    for i in range(len(value)):
        if(value[i] == no):
            count = count + 1
    return count

def main():
    Data= []
    print("Enter the number of element :")
    size = int(input())

    print("Enter each element :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Enter the Element to Search :")
    item = int(input()) 
    Result = frequency(Data,item) 

    print("Frequecy of the no is : ", Result)

if __name__ == "__main__":
    main()   