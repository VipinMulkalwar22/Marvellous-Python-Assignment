class Student:
    school_name = "Marvellous Infosystems"
    def __init__(self,sname,sroll_no):
        self.name = sname
        self.roll_no = sroll_no

    def Display(self):
        print("Name : ",self.name)
        print("Roll no",self.roll_no)
        print("School Name",Student.school_name)

def main():
    sObj = Student("Rohit",10)
    sObj.Display()
   
    Student.school_name = "Train with Marvellous"
    print("School Name",Student.school_name)

if __name__ == "__main__":
    main()
