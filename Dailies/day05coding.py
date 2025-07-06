def everyOtherItemStr(aList):
    aNewList = []
    for item in aList:
        if isinstance(item, str) and aList.index(item)%2 ==0:
            aNewList.append(item)
    return aNewList



    
        
