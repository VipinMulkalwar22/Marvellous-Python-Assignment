from functools import reduce

prod = lambda no1,no2 : no1 * no2

def main():
    Data = []
    print("Enter the number of element")
    size = int(input())

    print("Enter the each element")
    
    for i in range(size):
        no = int(input())
        Data.append(no)

    print(Data)
    result = reduce(prod,Data)
    print(result)
    

if __name__ == "__main__":
    main()