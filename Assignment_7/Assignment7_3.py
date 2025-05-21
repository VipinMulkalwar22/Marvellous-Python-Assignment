even = lambda no1 : (no1 % 2 == 0)

def main():
    Data = []
    print("Enter the number of element")
    size = int(input())

    print("Enter the each element")
    
    for i in range(size):
        no = int(input())
        Data.append(no)

    print(Data)
    result = list(filter(even,Data))
    print(result)
    

if __name__ == "__main__":
    main()