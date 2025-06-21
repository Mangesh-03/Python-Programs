Multiplication = lambda No1,No2 : No1 * No2

def main():
    
    print("Enter the First number : ")
    value1 = int(input())
    print("Enter the Second number : ")
    value2 = int(input())

    ret = Multiplication(value1,value2)
    print(f"Multiplication of {value1} and {value2} is : ",ret)

if(__name__=="__main__"):
    main()     