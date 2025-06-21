from functools import reduce
    
def Prime(value):

    
    iCnt = 2
    while(iCnt <= int(value/2)):

        if((value % iCnt)==0):
            break
            
        iCnt += 1

    return(iCnt > int(value/2))    


Increment = lambda value : value * 2

Maximum = lambda No1,No2 : No1 if (No1 > No2) else No2

def FMR(List):

    fData = list(filter(Prime,List))
    print(fData)

    mData = list(map(Increment,fData))
    print(mData)

    rData = reduce(Maximum,mData)

    return rData

def main():
    List = []

    print("Enter the number elements in list : ")
    size = int(input())

    for i in range(size):
        List.append(int(input("Enter the element : ")))
    ret = FMR(List)
    print(ret)    

if(__name__=="__main__"):
    main() 