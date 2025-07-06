"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: workout()
Parameters: exerciseName (str), interestedFriends (int), totalFriends (int)
Returns: None (NoneType)
"""
def workout(exerciseName, interestedFriends,totalFriends):
    if interestedFriends/totalFriends < 0.2:
        print("Let's try a different workout.")
    elif interestedFriends/totalFriends >= 0.2 and interestedFriends/totalFriends<0.7:
        print(f"We will try to {exerciseName} for 30 minutes.")
    else: print(f"We are so excited to {exerciseName}!")
    
    

#########################################

"""
Function Name: iceCream()
Parameters: rating (float), distance (float)
Returns: choice (str)
"""
def iceCream(rating, distance):
    database = [["Jeni's", 4.5, 7.5],["Cold Stone", 4.5, 3.6], ["Morelli's", 4.5,4.2], ["Bruster's", 4.0, 1.3], ["Sweet Stack", 4.0, 6.4],["Baskin Robbins",3.5,2.8]]

    ans = []
    for combo in database:
        
        if combo[1]==rating and combo[2]==distance:
            ans = combo[0]
    if ans == []:
        return "Try again tomorrow."
    else:
        return ans

print(iceCream(4.5, 4.2))    
#########################################

"""
Function Name: restaurantDecider()
Parameters: veganFriendly (bool), yelpStars (int), milesAway (int)
Returns: decisionStr (str)
"""
def restaurantDecider(veganFriendly, yelpStar, milesAway):
    if veganFriendly == False:
        return "Not tonight."
    elif yelpStar < 3:
        return "Not good enough food."
    elif milesAway > 5:
        return "Too far!"
    else: return "Perfect restaurant!"
    

#########################################

"""
Function Name: dinnerTip()
Parameters: numFriends (int), dinnerCost (float)
Returns: tipAmount (float)
"""
def dinnerTip(numFriends, dinnerCost):
    
    if numFriends <= 3:
        tip = dinnerCost * 0.15
    elif numFriends <= 7 and numFriends > 3:
        tip = dinnerCost * 0.2
    else: tip = dinnerCost * 0.25

    return round(tip, 2)
    
            
        
    

#########################################

"""
Function Name: planMaker()
Parameters: timeA (float), costA (int), timeB (float), costB (int)
Returns: planDecision (str)
"""
def planMaker(timeA, costA, timeB, costB):
    if costA < costB:
        return "planA"
    elif costA>costB:
        return "planB"
    else:
        if timeA < timeB:
            return "planA"
        elif timeA>timeB:
            return "planB"
        else:
            return "No plans this weekend."
    
    
    





