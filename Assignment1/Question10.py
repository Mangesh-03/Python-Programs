def DisplayLength(strName):
    iCount = 0
    for ch in strName:
        iCount += 1
    print(iCount)

def main():

    print("Enter Name :  ")
    cValue =input()    
    DisplayLength(cValue)
    
if __name__ =="__main__":
    main()  


       
