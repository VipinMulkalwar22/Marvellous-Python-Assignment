from functools import reduce

# def chkPrime(value):

#     if (value <= 1):
#         return False
#     else:
#         for i in range(2,int(value ** 0.5)+1):
#             if(value % i == 0):
#                 return False
#                 break
#         return True

chkPrime = lambda value : value > 1 and all(value % i for i in range(2, int(value ** 0.5)+1))

Mult = lambda no : no * 2

Max = lambda value1,value2: value1 if value1 > value2 else value2

# def Max(value1,value2):
#     max = value1
#     if (value1 > value2):
#         max = value1
#     else:
#         max = value2

#     return max

def main():
    Data = []
    print("Enter the number of element :")
    size = int(input())

    if (size > 0):
        print("Enter the each element :")

        for i in range(size):
            no = int(input())
            Data.append(no)

        print("Input List :", Data)
        filteredOutput = list(filter(chkPrime,Data))
        print("List After Filter : ", filteredOutput)
        mapOutput = list(map(Mult,filteredOutput))
        print("List After Map :",mapOutput)
        reduceOutput = reduce(Max,mapOutput)
        print("Output of Reduce : ",reduceOutput)

if __name__ == "__main__":
    main()