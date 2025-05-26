def Addition(List):
    sum = 0

    for i in range(len(List)):
        sum +=List[i]
    
    return sum
    

def main():

    Nolist = []
    retValue = 0
    
    print("Enter the number of elements : ")
    Size = int(input())

    for i in range(Size):
        Nolist.append(int(input("Enter Element : ")))

    retValue = Addition(Nolist) 
    print("Addition of elements are : ",retValue)

if __name__=="__main__":
    main()    
