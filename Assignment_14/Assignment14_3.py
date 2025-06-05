class Book:
    def __init__(self,bprice):
        self.__price=bprice

    def setPrice(self):
        print("Enter the price of Book")
        self.__price = int(input())

    def getPrice(self):
        print("Price : {}".format(self.__price))

def main():
    bObj = Book("10")
    bObj.setPrice()
    bObj.getPrice()

if __name__ == "__main__":
    main()