import math
def Addition(List):
    MinNum = math.inf
    
    for i in List:
        if(MinNum > i):
            MinNum = i
    
    return MinNum
    

def main():

    Nolist = []
    retValue = 0
    
    print("Enter the number of elements : ")
    Size = int(input())

    for i in range(Size):
        Nolist.append(int(input("Enter Element : ")))

    retValue = Addition(Nolist) 
    print("Minimum element is : ",retValue)

if __name__=="__main__":
    main()    
