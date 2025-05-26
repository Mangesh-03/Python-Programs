def ChkPrime(No):
    bFlag = True
    iCnt = 0

    if( No <= 1):       # Filter
        return
    if( No == 2):       # corner case
        return True
    
    no = int(No/2)

    for iCnt in range(2,(no+1)):

        if((No % iCnt)==0):
            bFlag = False
            break
    
    
    return bFlag 

        