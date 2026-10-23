from random import randint

computer = randint(1,50)
user = 0

guesses = 0
while (user != computer):
    guesses+=1
    user = int(input("Enter a number: "))
    if (user>computer):
        print("Enter a lower number.")
    elif (user<computer):
        print("Enter a higher number.")

print(f"You have correctly guessed the number '{computer}' in {guesses} attempts.")