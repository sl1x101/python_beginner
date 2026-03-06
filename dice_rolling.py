#dice_rolling 
import random as rd
while True:
    choice = input("input (y/n): ").lower()
    if choice  == 'y':
       dice1 = rd.randint(1,6)
       dice2 = rd.randint(1,6)
       print(f"{dice1}:{dice2}")
    elif choice  == 'n':
        print("Thanks fo playing!")
        break
    else:
        print("invalid choice!")