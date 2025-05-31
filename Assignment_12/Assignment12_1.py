class Demo:

    Value = 0
    def __init__(self,value1,value2):
        self.no1 = value1
        self.no2 = value2
    
    def Fun(self):
        print("Fun",self.no1)
        print("Fun",self.no2)
    
    def Gun(self):
        print("Gun",self.no1)
        print("Gun",self.no2)
    
def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()