from functools import reduce
    
chk  = lambda value : value >= 70

Increment = lambda value : value + 10

def FMR(List):

    fData = list(filter(chk,List))
    print(fData)

    mData = list(map(Increment,fData))
    print(mData)

    rData = (reduce(lambda No1,No2 : No1*No2,mData))

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