count = 0
def CountZero(value):
    global count 
    if(value > 0):
        rem = value % 10
        if(rem == 0):
            count +=1
        CountZero(int(value / 10))
    
    return count

def main():
    print("Enter the number")
    no = int(input())    

    Ans = CountZero(no)

    print(Ans)

if __name__ == "__main__":
    main()