class Rectangle:

    def __init__(self,rlength,rwidth):
        self.length = rlength
        self.width = rwidth

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return (self.length + self.width)*2

def main():
    Obj = Rectangle(10,5)
    print("Area : {} , Perimeter : {}".format(Obj.Area(),Obj.Perimeter()))

if __name__ == "__main__":
    main()
