def everyOtherItemStr(aList):
    aNewList = []
    for item in aList:
        if isinstance(item, str) and aList.index(item)%2 ==0:
            aNewList.append(item)
    return aNewList

print(everyOtherItemStr([1,2,3,4,5,'bob','jerry']))


    
        
