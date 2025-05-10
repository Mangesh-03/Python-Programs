def CheckDivisible(iNo):
    
    if((iNo % 5)==0):
        return True

    else:
        return False

def main():

    print("Enter Number : ")
    iValue = int(input())

    isRet = CheckDivisible(iValue)

    if(isRet == True):
        print(iValue,"Number is divisible by 5")        
    elif(isRet == False):
        print(iValue,"Number is not divisible by 5")     

if __name__ =="__main__":
    main()                    