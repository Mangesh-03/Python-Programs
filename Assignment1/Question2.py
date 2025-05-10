def ChkNum(iNo):
    if(iNo <= 0):
        iNo = -iNo
        if((iNo % 2)==0):
            print("Even Number")

        else:
            print("Odd Number") 

def main():

    print("Enter Number")
    iValue= int(input())
    
    ChkNum(iValue)           

if __name__ =="__main__":
    main()    