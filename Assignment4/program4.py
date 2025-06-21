from functools import reduce
    
def EvenChk(value):
   
    flag  = False
    
    
    if((value % 2)==0):
        flag = True
        
    return flag

Square = lambda value : value ** 2

Addition = lambda No1,No2 : No1 + No2

def FMR(List):

    fData = list(filter(EvenChk,List))
    print(fData)

    mData = list(map(Square,fData))
    print(mData)

    rData = reduce(Addition,mData)

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