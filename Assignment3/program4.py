import math
def Addition(List,No):
    
    Count = 0
    for i in List:
        if(No == i):
            Count += 1
    
    return Count
    

def main():

    Nolist = []
    retValue = 0
    
    print("Enter the number of elements : ")
    Size = int(input())

    for i in range(Size):
        Nolist.append(int(input("Enter Element : ")))

    Value = int(input("Enter element to find its Frequency : "))
    
    retValue = Addition(Nolist,Value) 
    print("Frequency of given element is : ",retValue)

if __name__=="__main__":
    main()    
