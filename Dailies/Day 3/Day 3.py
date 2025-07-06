age = 18

name = "Bob"

my_f_str = f"Hello my name is {name}, and I am {age} years old "

def place_an_order():
    order = input("What woudld you like to order")
    while order != "Nothing else":
        print("{} coming right up". format(order))
        order = input("What else?")

def withdrawl(balance):
    while balance > 0:
        amount = int(input("How much"))
        balance -= amount
        if balance >0:
            print(f"{round(balance, 2)} left")
        else: print(f"You owe {-balance}")
        



def keep_lower(sentence):
    stringl = ""
    for char in sentence:
        if char.islower():
            stringl += char
    print(stringl)



dicy = {"b":["Klaus"], "Ramya":["Klaus","Howey"]}
list1 = [['b'],'c']

list1.append('c')
print(list('b') in list1)
