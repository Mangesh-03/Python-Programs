def PrintEven(iNo):
    iCnt = 1
    num = 2

    while(iCnt<=iNo):
       
        print(num)
        num +=2   
        iCnt = iCnt+ 1       

def main():
    print("Enter Number : ")
    iValue = int(input())
    PrintEven(iValue)
   
if __name__ =="__main__":
    main()    