"""
Georgia Institute of Technology - CS1301
HW03 - Iterations
"""

#########################################

"""
Function Name: avgTotal()
Parameters: numString(str)
Returns: average(float)
"""
def avgTotal(num_str):
    num_list = []
    for num in num_str:
        num_list.append(int(num))
    total = 0
    for num in num_list:
        total += num
    if num_str == "":
        return 0
     
    return total/len(num_list)


        

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: safeDecoder()
Parameters: characterString(str)
Returns: passcodeString(str)
"""

def safeDecoder(mix_str):
    
    index_list = []
    final = ""
    for num in mix_str:
        if num in "1234567890":         
            index_list.append(mix_str.index(num))
            mix_str = mix_str[0:mix_str.index(num)] + "!" + mix_str[mix_str.index(num)+1:]   
    for num in index_list:
        final += str(num)

    return final




        
        
        
        
    

#########################################
########## WRITE FUNCTION HERE ##########
#########################################




"""
Function Name: testScore()
Parameters: test1(str), test2(str)
Returns: maxPercentage(float)
"""

def testScore(test1, test2):
    test_total = [test1, test2]
    total_score = 0
    perc_list = []
    for tests in test_total:
        for num in tests.split("_"):
            total_score += float(num)
        perc_list.append(total_score/5/5*100)
        total_score = 0
    if perc_list[0]>perc_list[1]:
        return perc_list[0]
    elif perc_list[0] < perc_list[1]:
        return perc_list[1]
    else: return "Same Percentage"
        
        
        
    

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: trip()
Parameters: tripTotalCost(float), bankBalance(float), interestRate(float)
Returns: months(int)
"""

def trip(tripTotalCost, bankBalance, interestRate):
    i = 0
    while bankBalance < tripTotalCost:
        bankBalance *= (interestRate+100)/100
        i +=1
    return(i)


    
    

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: rightTriangles()
Parameters: numRows(int), character(str)
Returns: None
"""

def rightTriangles(numRows, character):
    if numRows < 2 or numRows == 0 or character == '' or numRows == None or character == None:
        print('No Triangle')
    else:
        for i in range(1, numRows+1):
           print(character*i)
        
rightTriangles(1, "Bob ")


    

#########################################
########## WRITE FUNCTION HERE ##########
#########################################










