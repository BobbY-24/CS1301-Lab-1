def techLibs():
    name = input("Enter your name: ")
    bf_name = input("Enter your best friend's name: ")
    fav_spot = input("Enter your favorite study spot: ")
    print(f"The other day, I saw {name} and {bf_name} up to no good.")
    print(f"They were loudly gossiping at {fav_spot} instead of studying.")
    
def diningDollars():
    dd = float(input("How many dining dollars do you currently have?"))
    ddpw = float(input("How many dining dollars do you spend per week?"))
    wl = float(input("How many weeks are left?"))
    lo = dd - ddpw*wl
    print(f"You will have ${lo} left over.")

def sphereVol():
    r = float(input("Enter the radius of your sphere:"))
    v = float(3.14*r**3*4/3)
    v = round(v, 2)
    print(f"The volume of your sphere is {v}.")
              
            
def italianNight(ct):
    ct = float(ct)
    if ct < 20:
        return("We'll cook some other time.")
    elif ct >=20 and ct <35:
        return('Breadsticks')
    elif ct >=35 and ct <50: return('Pasta')
    else: return "Lasagna"
    
def toCook(nc, dd):
    nc = int(nc)
    dd = int(dd)
    if nc >3 and dd>10:
        print("Let's get Panda Express!")
    elif nc<=3 and dd>=50:
        print("Let's splurge on Chick-fil-A!")
    else:
        print("Guess I'll have to cook myself.")

def cookingClass(date, iw):
    iw = bool(iw)
    date = int(date)%2
    if date == 1:
        if iw == True:
            
            return "Unsure"
        else: return "Yes"
    else:
        if iw == True:
            return "Yes"
        else: return "No"
         
def captureTheFlag(dire):
    dire = str(dire)
    dire = dire[::-1]
    dire = dire.upper()
    dire = list(dire)
    for i in dire:
        if i =="L":
            print( "Turn left!")
        elif i == "R": print("Turn right!")
        
def demystifyMessage(jb):
    jb = str(jb)
    jbc = ""
    for i in jb:
        if i.isalpha():
            jbc += i
    return jbc

def gnomeAccounting(on):
    on = str(on)
    six = []
    for i in range(0,len(on),6):
        six.append(on[i:i+6])
    for j in six:
        print(j)
    
def countCase(ll):
    ll = str(ll)
    u_num = 0
    l_num = 0
    for i in ll:
        if i.isupper():
            u_num +=1
        elif i.islower():
            l_num +=1
    difference = abs(u_num-l_num)
    if u_num>l_num:
        return f"{difference} more uppercase letter(s)."
    elif u_num<l_num:
        return f"{difference} more lowercase letter(s)."
    else: return "Perfectly balanced!"
        
    
def findLove(c,fc):
    c = list(c)
    fc = str(fc)
    names = []
    for i in c:
        if i[1] == fc:
            names.append(i[0])
    return sorted(names)

def mutualInterests(yi,ti):
    mi = []
    for i in yi:
        if i in ti:
            mi.append(i)
    return mi

def numInventions(iv):
    completed = 0
    for i in iv:
        if i[1] == True:
            completed+=1
    return completed

def helpPhineas(b,bs):
    
    for i in bs:
        if i[0] == b:
            if int(i[1])>8 or int(i[1])<1:
                return False
            else: return True
            
import math
def agentDispatch(c,a):
    li = []
    for i in a:
        li.append(math.dist((i[1][0],i[1][1]),(c[0],c[1])))
    for i in a:
        
        if math.dist((i[1][0],i[1][1]),(c[0],c[1]))==min(li):
            return i[0]

def bestCity(voteDict):
    total = voteDict.items()
    min_list = []
    for combo in total:
        min_list.append(len(combo[1]))
    
    min_val= max(min_list)
    for key, value_list in voteDict.items():
        if len(value_list)==min_val:
            return key

def winningTeam(raceWinners):
    list_tuple_tuple_old = raceWinners.items()
    list_new = []
    for combo_tuple in list_tuple_tuple_old:
        if combo_tuple[1][1] >= 25:
            list_new.append(combo_tuple)
    list_new = dict(list_new)
    print(list_new)
    list_final = []
    for i in range(len(list_new)):
        list_ = min(dict(list_new), key = lambda x: list_new[x][1])
        list_final.append(list_)
        del list_new[list_]
        
        
    return(list_final)
            



#print(winningTeam({'red':('bob',300),'blue':('chris', 400), 'yellow': ("Jerry", 301), 'g':('aiden', 301.5)}))


def fantasyF1(driverCatalog, myPicks):
    driverCatalog1 = driverCatalog.items()
    total = 0
    for combo in list(driverCatalog1):
        for minorCombo in combo[1]:
            
            for key in combo[1]:
                
                for name in myPicks:
                    if key == name:
                        total+=combo[1][key]
    return total/2


#fantasyF1({"F":{"CL":500, "CS":400}, "M":{"LN":500,"OP":300}},["CL", "LN", "OP"])
    
with open("swiftieFlights.txt", 'r') as file:
    content = file.read()

content = content.split('\n\n')
content = list(content)
content_listList = []
for paragraph in content:
    paragraph = paragraph.split('\n')
    
    content_listList.append(paragraph)


def taylorEmissions(route):
    num = ""
    for combo in content_listList:
        if combo[0] == route:
            for i in combo[4]:
                if i in "1234567890.":
                    num += i
            return(float(num))

content_listList.remove(['Taylor Swift Flight Log'])
#print(content_listList)
def taylorFlights(carbonTons):
    
    result = []
    for combo in content_listList:
        num = ""
        for i in combo[4]:
                if i in "1234567890.":
                    num += i
        
        if float(num) > carbonTons:
            result.append(combo[0])


    return sorted(result)

def transportationModes():
    # transportationModes.txt ?
    pass

import requests

url = 'https://ghibliapi.vercel.app/films'

web = requests.get(url)
data_list_dict= web.json()

def letterLover(name):
    
    final_list = []
    for combo in data_list_dict:
        if combo['title'][0] == name.lower() or combo['title'][0] == name.upper():
            final_list.append(combo['title'])

    return sorted(final_list)

species_url = "https://ghibliapi.vercel.app/species"
response = requests.get(species_url)
data = response.json()

def speciesFinder(eyeColor):
    total = []
    for combo in data:
        for color_str in combo['eye_colors'].split(','):
        
            if color_str == eyeColor:
                total.append(True)
    if True in total:
        return True
    else: return False

url_ppl = "https://ghibliapi.vercel.app/people/"
ppl_response = requests.get(url_ppl)
ppl_info = ppl_response.json()

def characters(filmName):
    final = []
    for combo in ppl_info:
        movie = combo['films']
        response = requests.get(movie[0])
        data_list = response.json()
        
        if data_list['title'] == filmName:
                final.append(combo['name'])
    return sorted(final)

def foulCount(teamList, count = None):
    if count is None:
        count = 0
    if len(teamList) == 0 or teamList is None:
        return 0 
    
    if len(teamList) < 2:
        
        count += teamList[0][1]
        return count
    
    else:
        count = count+ teamList[-1][1]
        teamList.pop()
        return foulCount(teamList, count)

def convertTeams(teamsTup, teamList = None, count = 0):
    if teamList == None:
        teamList = list(teamsTup)
    if count == len(teamsTup):
        return teamList
        
    for i in str(teamsTup[count]):
        if i in "1234567890":
            print(teamList)
            teamList.remove(teamsTup[count])
            break
    count+=1
    return convertTeams(teamsTup, teamList, count)
        
            
def mergeTeamNames(team1, team2, bigName = None):
    if bigName == None:
        bigName = ""
    if team1 == "" and team2 == "":
        return ""
    elif team1 == "" and team2 != "":
        return team2
    elif team1 != "" and team2 == "":
        return team1
    
    
        
    bigName += team1[0]
    bigName += team2[0]
    team1 = team1[1:]
    team2 = team2[1:]
    if len(team1)<2 or len(team2)<2:
        bigName += team1[0]
        bigName += team2
        bigName += team1[1:]
        return bigName
   
    print(bigName)
    return mergeTeamNames(team1, team2, bigName)

class Spiderman:

    def __init__():
        pass
        



    


    
        
        
        
        
    
    
    
    
    
        
    
    
        
    


        
    

            
        
    
        





    



















    
    
    
