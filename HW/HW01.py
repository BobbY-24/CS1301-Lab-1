def dinnerTime():
    e = float(input("How many entrees will you be ordering? "))
    d = float(input("How many drinks will you be ordering? "))
    t = 4.5*d + 12*e
    t = round(t, 2)
    print(f"The total cost of all the meals and drinks is ${t}.")

def bottleBonanza():
    r= float(input("What is the radius of the water bottle? "))
    h= float(input("What is the height of the water bottle? "))

    v= h*r**2*3.14
    v = round(v, 2)
    print(f"The volume of the water bottle is {v}.")

def winterBreak():
    e = float(input("How many episodes did you watch? "))
    y = float(input("How many YouTube videos did you watch? "))
    t = int(40*e + 10 * y)
    h = t//60
    m = t%60
    print(f"You spent {h} hours and {m} minutes watching Netflix and YouTube over winter break.")
    
def skateboardMoney():
    a = float(input("How much is your monthly allowance? "))
    p = float(input("What percentage of your allowance do you want to save? "))
    t = round(a-311.7-a*p/100,2)
    print(f"You'll have ${t} left to spend on your skateboard after savings and fees."

  )  
    
