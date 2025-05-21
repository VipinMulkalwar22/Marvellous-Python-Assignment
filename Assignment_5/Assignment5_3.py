def Vote(value):  
    if(value >= 18):
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

def main():
    
    print("Enter the person Age")
    no = int(input())

    Vote(no)
    
if __name__ == "__main__":
    main()