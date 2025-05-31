import threading 

def Small(name):
    count = 0
    for chr in name:
        if chr.islower():
            count +=1
    print("Thread Id :",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("No of Small Letter in String is", count)

def Capital(name):
    count = 0
    for chr in name:
        if chr.isupper():
            count +=1
    print("Thread Id :",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("No of Capital Letter in String is", count)

def Digit(name):
    count = 0
    for no in name:
        if no.isdigit():
            count +=1
    print("Thread Id :",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("No of Digit in String is", count)

def main():
    print("Enter the String")
    sname = input()
    
    print("Inside Main Thread Id :",threading.get_ident())
    print("Inside Main Thread Name:",threading.current_thread().name)
    T1 = threading.Thread(target=Small,args=(sname,))
    T2 = threading.Thread(target=Capital,args=(sname,),name="Capital")
    T3 = threading.Thread(target=Digit,args=(sname,),name="Digit")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Exit from Main")    

if __name__ == "__main__":
    main()