import multiprocessing
import os

def Squre(value):
    print('process id:', os.getpid())
    print(multiprocessing.current_process().name)
    Ans = value * value
    print('Sqaure of {0} is {1}'.format(value,Ans))

def main():
    Data = []
    print("Enter the number of element")
    size = int(input())

    print("Enter the each element")

    for i in range(size):
        no = int(input())
        Data.append(no)

    Process = []
    for i in range(0,len(Data)):
        print(i,"=",Data[i])
        Proc = multiprocessing.Process(target=Squre,args=(Data[i],))
        Process.append(Proc)
    
    for P in Process:
        P.start()

    for P in Process:
        P.join()

   
if __name__ == "__main__":
    main()