def Display(iNo):

    if(iNo <= 0):
        print("invalid input !!")
        return
      

    for i in range(iNo):
        print("*")

def main():

    print("Enter Frequency :")
    iValue = int(input())

    Display(iValue)

if __name__ =="__main__":
    main()   