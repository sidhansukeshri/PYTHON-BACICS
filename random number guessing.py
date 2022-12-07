import random
n = random.randrange(1,100)
print("Lets play a game of gessing random numbers between 1 to 100!")
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("low!")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("high!")
        guess = int(input("Enter number again: ")) 
    else:
      break
print("you guessed it right!!")
