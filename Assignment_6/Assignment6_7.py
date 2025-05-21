def FindLargest(value):
    max = value[0]
    for i in range(len(value)):
        if(max <= value[i]):
            max = value[i]        
    return max

def main():
    Data = []
    print("Enter a number of element:")
    size = int(input())
    
    print("Enter the each Element")
    for i in range(size):
        no = int(input())
        Data.append(no)

    max = FindLargest(Data)

    print("Maximum number is : ",max)
    
if __name__ == "__main__":
    main()