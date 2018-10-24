import random
guessesTaken = 0

number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

while guessesTaken < 10
:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
 
    if guess < number:
        print("Your guess is too low.") # There are eight spaces in front of print.

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("That's Right! You guessed my number in " + guessesTaken + " guesses!")

