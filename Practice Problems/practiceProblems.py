
def rockRambleRoll():
    pizza = input("How many pizzas do you want at Campus Crust?")
    sandwich = input("How many sandwiches do you want at 5th Street Deli?")
    sushi = input("How many sushi rolls do you want at Bento Sushi?")
    tacos = input("How many tacos do you want at Twisted Taco?")
    total = float(pizza) * 9 +float( sandwich) * 5.5 + float(sushi )* 8 +float(tacos) *2.25
    print("You need to spend $"+ str(total)+" at Rock, Ramble, and Roll.")

def houseParty():
    a = input("How many autographs will you get?")
    t = input("How many times will you visit the bouncy castle?")
    v = input("How many video game contests will you participate in?")
    w = input("How many times will you walk through the locker rooms?")
    total = float(a)*10 + float(t)*20 +float(v)*45+float(w)*15
    mins = int(total%60)
    h = int(total//60)
    print(f"You will spend {h} hour(s) and {mins} minutes at the house party.")
    
def enterTheCave(p,c):
    if p =="Open Sesame" and (c<=25 and c>=0):
        print("You have opened the door")
    elif p == "Hello World" and (c<=100 and c>=75):
        print("You have opened the door")
    elif p =="Python Enjoyer" and c ==50:
        print("You have closed the door")
    else: print("INTRUDER ALERT")

def dinnerTime(x):
    rr = [("Sun, Sand, and Seafood", 250),("The Beachcomber's Bistro", 460), ("Coastal Catch", 820), ("Beachside Bonanza", 870), ("Tidal Wave Tavern", 940)]
    time = []
    for i in rr:
        time.append(abs(i[1]-x))
    index = time.index(min(time))
    return rr[index][0]

def lightCommunicator(udm):
    new = ""
    for i in udm:
        if i == "S":
            new+="T"
        elif i == "s":
            new+='t'
        elif i == "T":
            new+="S"
        elif i == "t":
            new+="s"
        else: new+=i 
    return new[::-1]

def totalTime(er):
    er=er.split(" ")
    tt=0
    for i in er:
        tt+=int(i)
    h = tt//60
    m = tt%60
    return f"{h} hour(s) and {m} minute(s)"

def meatlessMonday(d):
    if d == '':
       return []
    d = d.split("-")
    v = []
    
    
    for i in d:
        if i[0] == "v" or i[0]=="V":
            v.append(i[1:])
    
    v1 = ""
    m=0
    for i in v:
        
        for j in v[m]:
          if j.isalpha():
            v1 += j
        m+=1
    
        v1+="-"
    
    v1 = v1.lower()
    v1 = v1.split("-")
                
    return sorted(v1)[1:]

def eatingOut(yl,fl):
    ll = []
    for i in yl:
      for j in fl:
          
        if i == j:
            ll.append(i)
    if len(yl)==0 and len(fl)==0:
        return "Whatever, we'll go to Nave"
    else: return sorted(ll)

def organizeTimes(ul):
    iii=[]
    ii=[]
    for i in ul:
        print(i[0])
        i[0].remove(max(i[0]))
        i[0].sort()
        ii = i[::-1]
        iii.append(ii)
    
    iii=sorted(iii) 
    return iii



def findPlates(mb):
    mb -= 45
    if mb > 600 or mb%5 != 0:
        return []
    n = [45, 35, 25, 10, 5]
    count = []
    rem = mb
    for i in n:
        if rem > i*5:
            count.append(5)
            rem -= i *5
        else:
            count.append(rem//i)
            rem -= i * (rem//i)
    return [(45,count[0]),(35,count[1]),(25, count[2]), (10,count[3]), (5,count[4])]

def lunchSpots(fp):
    reversed_dict = {}
    for key, value_list in fp.items():
        for value in value_list:
            if value not in reversed_dict:
                reversed_dict[value]=[key]
            else:
                reversed_dict[value].append(key)
    
    reversed_dict = dict(sorted(reversed_dict.items()))
    reversed_dict = {key:sorted(value) for key, value in reversed_dict.items()}
    
    return reversed_dict

def creditHours(courseCatalog, myCourses):
    creditS = 0
    
    for subject_my, course_num_list in myCourses.items():
        
        for num in course_num_list:
            for subject, dicts in courseCatalog.items():
                for code, credit in dicts.items():
                    if num == code:
                        creditS += credit
    return creditS

import re

try:
 with open('movies.txt', 'r') as file:
    file_str = ""
    num =0
    for line in file:
        file_str += line
        if line.strip() =="":
            num += 1
            
  
    
    for line in file:
        if line.strip()!="":
            pass
        
    file = file.read()   
            
except:
 print("error occurred")
 
file_str.split(" ")

paragraphs = re.split(r'\n{2,}', file_str)
cleaned_paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]
info_list = []
for attributes in paragraphs:
    attributes = attributes.splitlines()
    info_list.append(attributes)



def foreignFilms(friendTupList):
    friendDict={}
    
    for friend_name, country in friendTupList:
        for ind_movie_info in info_list:
            if country in ind_movie_info:
                if friend_name not in friendDict:
                    friendDict[friend_name]=[ind_movie_info[0]]
                else: friendDict[friend_name].append(ind_movie_info[0])
    for friend_name, country in friendTupList:
        if country not in str(info_list):
            friendDict[friend_name]=[]
        
            
                
    friendDict = dict(sorted(friendDict.items()))
    
    friendDict = {key:sorted(value) for key, value in friendDict.items()}
    print(friendDict)
    return friendDict

"""
import sys
sys.path.append("/Users/bobyan/Desktop/CS 1301/Practice Problems")



import pandas as pd
summerDrinks=pd.read_csv("summerDrinks.csv")

for row in summerDrinks['name']:
    #print(row)
    pass

def inSeason(favDrinks, currentMonth):
    drinkList = []
    
    
    for drink1 in favDrinks:
        for drink2 in summerDrinks['name']:
            if drink1 == drink2:
                for status in summerDrinks['name']==drink1:
                    if status == True:
                        drinkList.append(drink1)
    print( drinkList)
    return drinkList
    
                
                
inSeason(["acai"], "July")            
                
 """
import csv

with open("summerDrinks.csv", "r") as file:
    read_file = csv.reader(file)
    header = next(read_file)

    drink_list = []
    for row in read_file:
        name = row[0]
        scores=list(map(str, row[1:]))
        drink_list.append((name,scores))
     


def inSeason(favDrinks, currentMonth):
    fav_list=[]
    for drink1 in favDrinks:
        for drink2 in drink_list:
            if drink1 == drink2[0] and currentMonth == drink2[1][2] and drink2[1][1]=="uncaffeinated":
                fav_list.append(drink1)
    if fav_list == []:
                
            return "Nothing is in season :("
    else: return sorted(fav_list)


import requests


url = "https://restcountries.com/v3.1/name/Mexico?fullText=true"
response = requests.get(url)
#print(type(response.json()[0]["cioc"]))

def shareBorder(country1, country2):
    

    url11 = f"https://restcountries.com/v3.1/name/{country1}?fullText=true"
    r1 = requests.get(url11)
    country1 = r1.json()[0]["cioc"]
    
    url22 = f"https://restcountries.com/v3.1/name/{country2}?fullText=true"
    r2 = requests.get(url22)
    country2 = r2.json()[0]["cioc"]

    url1 = f"https://restcountries.com/v3.1/alpha/{country1}"
    u1 = requests.get(url1)
    url2 = f"https://restcountries.com/v3.1/alpha/{country2}"
    u2 = requests.get(url2)

    
    if "borders" not in u1.json()[0] or "borders" not in u2.json()[0] :
     return False   
    
    list_dict1 = u1.json()[0]["borders"]
    list_dict2 = u2.json()[0]["borders"]

    for nation in list_dict1:
        if nation == country2:
            return True
        else: return False
        
def currencyRatio(continent, currency):

    currency = currency.lower()
    
    url_currency = f"https://restcountries.com/v3.1/currency/{currency}?fullText=true"
    uc = requests.get(url_currency)

    

    url_continent = f"https://restcountries.com/v3.1/region/{continent}"
    ucon = requests.get(url_continent)
    
    ACR = list(uc.json()[0]["currencies"].keys())[0]
    count_cur = 0
    count_total = 0

    for nations in ucon.json():
        count_total +=1
        for item in nations['currencies']:
            #count_total +=1
            if item == ACR:
                count_cur += 1
    floatr = round(count_cur/count_total, 2)        
    print(   floatr)
    return floatr

def numCoffees(num):
    num = int(num)
    
    if num < 1:
        print("No more coffee!")
    else:
        print(f"Coffees left: {num}")
        numCoffees(num-1)



def atlCoffee(listOfShops, shopsToVisit = None):
    if shopsToVisit is None:
        shopsToVisit = {}
    
    listOfShops = [combo for combo in listOfShops if combo[2] > 5]
    
    
    if len(listOfShops)<1:
        
       return {k: sorted(v) for k, v in sorted(shopsToVisit.items())}
       
    else: 
        min_combo = min(listOfShops, key = lambda x:x[2])
        if min_combo[1] not in shopsToVisit:
            shopsToVisit[min_combo[1]]=[min_combo[0]]
        else:
            shopsToVisit[min_combo[1]].append(min_combo[0])
        listOfShops.remove(min_combo)
        
        return atlCoffee(listOfShops, shopsToVisit)

class Friend:
    def __init__(self, name, age, foodItem, rsvpStatus):
        self.name = name
        self.age = age
        self.foodItem = foodItem
        self.rsvpStatus = rsvpStatus
        
    def __str__(self):
        if self.rsvpStatus == True:
            return f"My name is {self.name}. I am {self.age} years old, and I am bringing {self.foodItem}!"
        
        else: return f"My name is {self.name}. Unfortunately, I cannot go to the potluck :("

    def __eq__(self, other):
        if self.name == other.name and self.foodItem == other.foodItem and self.age == other.age:
            return True

class Potluck:
    def __init__(self, host, guestlist):
        self.host = host
        self.guestlist = guestlist

    def __str__(hostName, numGuest):
        hostName = self.host
        numGuest = len(self.guestlist)
        return f"My name is {hostName}, and I am hosting a potluck. There are {numGuests} people coming."

    def invite(friend_name):
        if friend_name.rsvpStatus == True:
            
         pass

Chris = Friend('Chris', 20, 'apple juice', True)
Bob = Friend('Chris', 20, 'apple juice', True)
print(Bob)
         
            
            
            

