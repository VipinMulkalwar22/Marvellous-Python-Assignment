from functools import reduce

chkNo = lambda no : no >= 70 and no <= 90
increaseNo = lambda no : no + 10
prodNo = lambda no1,no2 : no1 * no2

def main():
    Data = []
    print("Enter the number of element :")
    size = int(input())

    print("Enter the each element :")
    
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)
    filteredOutput = list(filter(chkNo,Data))
    print("List After Filter : ", filteredOutput)
    mapOutput = list(map(increaseNo,filteredOutput))
    print("List After Map :",mapOutput)
    reduceOutput = reduce(prodNo,mapOutput)
    print("Output of Reduce : ",reduceOutput)

if __name__ == "__main__":
    main()