class Arithmatic:
    
    def __init__(self,uValue):
        self.Value = uValue

    def ChkPrime(self):

        if (self.Value <= 1):
            return False

        for no in range(2,int(self.Value ** 0.5)+1):
            if (self.Value % no == 0):
                return False
                break

        return True

    def chkPerfect(self):
        Sum = 0
        for no in range(1,int(self.Value/2)+1):
            if (self.Value % no == 0):
                Sum = Sum + no

        if (Sum == self.Value):
            return True
        else:
            return False
    
    def SumFactors(self):
        Sum = 0
        for no in range(1,int(self.Value/2)+1):
            if (self.Value % no == 0):
                Sum = Sum + no
                
        print("Sum Factors of {} is {}".format(self.Value,Sum))
    
    def Factors(self):
        Data = []
        for no in range(1,int(self.Value/2)+1):
            if (self.Value % no == 0):
                Data.append(no)

        print("Factors of {} are {}".format(self.Value,Data))

def main():
    
    print("Enter the number")
    no = int(input())

    Obj1 =Arithmatic(no)

    Ret1 = Obj1.ChkPrime()
    print("Is Prime :", Ret1)

    Ret2 = Obj1.chkPerfect()
    print("Is Perfect :", Ret2)
    Obj1.SumFactors()
    Obj1.Factors()


if __name__ == "__main__":
    main()