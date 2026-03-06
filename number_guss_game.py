#number random  (1-20)
import random as rd
random_to_number = rd.randint(1,20)
while True:
    try:
        guess = int(input("input put your number (1-20): "))     
        if guess < random_to_number:
            print("to low")
        elif guess> random_to_number:
            print("to height")
        else:
            print("Congratulation! you guess the number! ")
            break
    except ValueError:
        print("input number!")