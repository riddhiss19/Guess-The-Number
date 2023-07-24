import random
from logo import logo_ascii
list_of_num = list(range(1, 101))
chosen_num=random.choice(list_of_num)

print(logo_ascii)
print("WELCOME TO THE GUESS THE NUMBER GAME\nI am thinking of a number between 1 to 100")
level=input("Choose a level 'easy' or 'hard':").lower()

def find_num():
        print(f"You have {i} attempts to guess the number")
        guess=int(input("Make a guess:"))
        if guess>chosen_num:
            print("Too high\n")
        elif guess<chosen_num:
            print("Too low\n")
        elif guess==chosen_num:
            print(f"You got it right!! the number is {chosen_num}")
            return
        else:
            print(f"You lost it!! The number chosen was {chosen_num}")

        if(i==1):
            print(f"You lost it!! The number chosen was {chosen_num}")


if(level=="easy"):
    i=10
    while i>0:
        find_num()
        i-=1


if(level=="hard"):
    i=5
    while i>0:
        find_num()
        i-=1