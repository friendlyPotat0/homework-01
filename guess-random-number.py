import random

randomNumber = random.randint(1, 20)
print("A random number between 1 and 20 (inclusive) was generated. Can you guess the number in five attempts?")

for i in range (0, 5):
    guessedNumber = int(input("Enter value: "))
    if randomNumber == guessedNumber:
        print("Well done! You guessed the number")
        break
else:
    print("%s%i" %("Game over! The number was: " , randomNumber))
