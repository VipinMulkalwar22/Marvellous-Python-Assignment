# def chkPrime(value):

#     if (value <=1):
#         return False
    
#     for i in range(2,int(value ** 0.5)+1):
#         if (value % i == 0):
#             return False
#             break
#     return True

chkPrime = lambda no : no > 1 and all(no % i != 0 for i in range(2,int(no ** 0.5)+1))

def main():
    Data = []
    print("Enter the number of element")
    size = int(input())

    print("Enter the each element")
    
    for i in range(size):
        no = int(input())
        Data.append(no)

    print(Data)
    result = list(filter(chkPrime,Data))
    print(result)
    

if __name__ == "__main__":
    main()