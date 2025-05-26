import MarvellousNum

def ListPrime(List): 

    PrimeL = []
    sum = 0

    for value in List:
        retValue = MarvellousNum.ChkPrime(value)
        if(retValue == True):
            PrimeL.append(value)
    
    for value in PrimeL:
        sum += value
    
    return sum

def main():
    List = []
    Size = 0

    print("Enter the number of elements : ")
    Size = int(input())

    for i in range(Size):
        List.append(int(input("Enter Element : ")))

    retValue = ListPrime(List)
    print("Additon of prime is : ",retValue)

if __name__=="__main__":
    main()