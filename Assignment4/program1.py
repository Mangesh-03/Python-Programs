Square = lambda No: No ** 2

def main():
    print("Enter the Number : ")
    value = int(input())

    ret = Square(value)
    print(f"Square of number {value} is : ",ret)

if(__name__=="__main__"):
    main()     