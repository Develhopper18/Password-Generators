import turtle
import random
import time
import string

def main():
    list_1 =  []
    name = input("Enter your name: ")
    list_1.extend(name)
    list(name)
    # print(list_1)
    passw = list_1[1]
    p = input("Enter the password (Remember it is one letter of your name): ")
    if p == passw:
        print("You got the password right")
        print("Let me generate a random password for you ")
        print("wait five seconds")
        i = 0
        while i < 5:
           i += 1
           print(i)
           time.sleep(0.5)
        random.shuffle(list_1)
        list_1.extend(passw)
        pkl = []
        li = string.digits
        pkl.extend(li)
        list_1.extend(pkl[:3])
        random.shuffle(list_1)
        n = "".join(list_1)
        print(f"Password = {n}")
        print(list_1)
    else:
        print("Try again")

main()
