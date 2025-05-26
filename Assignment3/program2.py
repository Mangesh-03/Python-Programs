import math
def Addition(List):
    MaxNum = -math.inf
    
    for i in List:
        if(MaxNum < i):
            MaxNum = i
    
    return MaxNum
    

def main():

    Nolist = []
    retValue = 0
    
    print("Enter the number of elements : ")
    Size = int(input())

    for i in range(Size):
        Nolist.append(int(input("Enter Element : ")))

    retValue = Addition(Nolist) 
    print("Maximum element is : ",retValue)

if __name__=="__main__":
    main()    
