def Addition(value):
    sum = 0
    for i in range(len(value)):
        sum = sum + value[i]

    return sum

def main():
    Data = []
    print("Enter the number of Element")
    size = int(input())

    print("Enter the each element")
    for i in range(size):
        no = int(input())
        Data.append(no)

    Result = Addition(Data)

    print("Addition is :", Result)

if __name__ == "__main__":
    main()