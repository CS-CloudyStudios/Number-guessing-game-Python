import random

upper_bound = 100

secret_number = random.randint(0, upper_bound)

print("Welcome to the number-guessing-game.")
guess = int(input("Gebe hier eine Zahl zwischen 1 und 100 ein: "))

def random_number():
    global guess2
    if guess or guess2 > secret_number:
        print("The number you search is smaller")
        guess2 = (int(input("Enter the next guess:")))
    if guess or guess2 < secret_number:
        print("The number you search is bigger")
        guess2 = (int(input("Enter the next guess:")))
    if guess or guess2 == secret_number:
        print("Yeah, that's the right number!")


random_number()

