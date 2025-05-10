def ChkNum(iNo):

    if(iNo > 0):
        print("Positive Number ")

    elif(iNo < 0):
        print("Negative Number ")
    elif(iNo == 0):
        print("Zero")

def main():
    print("Enter Number : ")
    iValue = int(input())
    ChkNum(iValue)        

if __name__ =="__main__":
    main()