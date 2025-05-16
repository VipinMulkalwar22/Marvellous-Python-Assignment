from functools import reduce

chkEven = lambda no : no % 2 == 0
squareNo = lambda no : no * no
additionNo = lambda no1,no2 : no1 + no2

def main():
    Data = []
    print("Enter the number of element :")
    size = int(input())

    print("Enter the each element :")
    
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)
    filteredOutput = list(filter(chkEven,Data))
    print("List After Filter : ", filteredOutput)
    mapOutput = list(map(squareNo,filteredOutput))
    print("List After Map :",mapOutput)
    reduceOutput = reduce(additionNo,mapOutput)
    print("Output of Reduce : ",reduceOutput)

if __name__ == "__main__":
    main()