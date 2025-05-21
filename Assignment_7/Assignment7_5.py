def Palindrome(svalue):
    stemp = ""
    for i in range(len(svalue)-1,-1,-1):
        stemp = stemp + svalue[i]
    
    return stemp

def main():
    print("Enter the String")
    sname = input()
    stemp = Palindrome(sname)
    
    if(sname == stemp):
        print(sname,"is Palindrome")
    else:
        print(sname,"is not Palindrome")
    
if __name__ == "__main__":
    main()