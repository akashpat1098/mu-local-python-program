target=45
guesses=9
print("I'm thinking of a number! Try to guess the number I'm thinking of")
print("You have 9 guesses")
choice=input("Enter The Number:")
guesses=guesses-1
print(guesses,"guesses left")
while (guesses>=0):
    while (not choice.isnumeric()):
        print("Invalid Input")
        choice=input("Enter The Number again:")
    if int(choice)>target:
        choice=input("Too high! Guess again:")
    elif int(choice)<target:
        choice=input("Too low! Guess again:")
    else:
        print("You get the Number.You Won")
        break
    guesses=guesses-1
    print(guesses,"guesses left")
    if guesses==0:
        print("You Lost")
        break
   
    


