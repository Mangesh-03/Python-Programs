def Add(iNo1,iNo2):

    iAns = 0
    iAns = iNo1 + iNo2
    return iAns

def main():

    print("Enter first Number : ")
    iValue1 = int(input())

    print("Enter Second Number : ")
    iValue2 = int(input())

    iRet = 0

    iRet = Add(iValue1,iValue2)    
    print("Addition of two Number is : ",iRet)

if __name__ =="__main__":
    main()    