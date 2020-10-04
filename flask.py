import math
import math
import pygame
import random

def Ex1():
    name = "John Smith"
    age = "20 years"
    isNew = True
    print(name)
    print(age)
    print(isNew)
    

def Ex2():
    name = input("What is your name: ")
    color = input("What is your favourite color:")
    print(f"Hey! {name} you like this stupid {color}")

def Ex3():
    by = int(input("What is your birth year: "))
    print("Loading....................")
    find = 2020 - by
    print(f"You are {find} years old")

def Ex4():
    HOW = input("In which unit do you want to convert your weight(Kilo/Pound): ")
    WHt = input("What is your weight: ")
    if HOW == "Kilo".lower():
        ct = int(WHt) * 0.45
        print(ct)
    elif HOW == "Pound".lower():
        ct2 = 1 - 1
        print(ct2)
    else:
        print("HIt")

# Ex4()
def Ex5():
    types = "Python is the easiest of all"
    print(types.upper())
    print(types[::-2])

# Ex5()
def Ex6():
    # print(10 // 3, 2 + 3, 4 - 6, 6 * 8)
    varn = 100
    varn -= 10 - 100
    print(varn)

# Ex6()
def Ex7():
    x = (100 + 100) * 2 - 300
    print(x)

# Ex7()
def Ex8():
    o = 99999.8
    ot = round(o)
    op = abs(o)
    print(f"{ot} == {op}")
    print(math.floor(1.9))
# Ex8()

def Ex9():
    day = input("How is the condition today, Hot or Cold: ").lower()
    if day == "Hot".lower():
        print("It's hot drink water")
    elif day == "Cold".lower():
        print("It'stoo cold don't go out")
    else:
        print("It's a lovely day")
    
# Ex9()
def Ex10():
    priceHouse = 1000000
    goodCredit = False
    if goodCredit == True:
        dp = 0.1 * priceHouse
        print(f"${dp}")
    elif goodCredit == False:
        dp = 0.2 * priceHouse
        print(f"${dp}")
    else:
        print("funs")

# Ex10()
def Ex11():
    highIncome = False
    goodCredit = False
    if highIncome and goodCredit:
        print("Eligible for loan")
    elif highIncome and not goodCredit or goodCredit and not highIncome:
        print("not eligible for loan")
    elif not highIncome and not goodCredit :
        print("never eligible for loan")
    else:
        print("Your loan is mine")

# Ex11()
def Ex12():
    highIncome = True
    goodCredit = False
    if highIncome or goodCredit:
        print("Eligible for loan")
    elif not highIncome or goodCredit:
        print("get lost")
    else:
        print("shut up")

# Ex12()
def Ex13():
    temp = -1
    if temp >= 30:
        print("It's a hot day do you need an ice tea")
    elif temp <= 10:
        print("the Heater cost's $100")
    elif temp <= 30:
        print("It's in medium range")
    else:
        print("It's your best day")

# Ex13()
def Ex14():
    name = input("What is your name: ")
    let = len(name)
    if let <= 4:
        print("Name doesn't exist too small")
    elif let >= 50:
        print("Can'yt be too long")
    else:
        print("nice name")

# Ex14()

# 1:14:16

# print(4 / 100)

def Ex15():
    a = input("What is your name: ")
    get = len(a)
    b = [1,2,5,3,6,65,7,35,45,453] 
    c = [0, 4, 34,2, 324, 5]
    d = random.randint(b + a + c )
# Ex15()