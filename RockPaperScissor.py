import random
rounds=5 
comp_score,user_score=0,0
user_choice=int()
print(f"Comp:{comp_score},You:{user_score}")

for i in range(rounds):
    choices=["Rock","Paper","Scissor"]
    while True:
        try:
            print(f"Round {i+1}")
            user_choice=int(input("Enter the 1 for Rock 2 for Paper and 3 for Scissor:"))
        except ValueError:
            print("You entered the wrong input.Please try again")
            continue
        if user_choice not in (1,2,3):
            print("You entered the wrong input.Please try again")
            continue
        break
    print(f"You chose {choices[user_choice-1].capitalize()}")
    comp_choice=random.choice(choices)
    print(f"Computer chose {comp_choice.capitalize()}")
    if choices[user_choice-1] is comp_choice:
        print("*****Tie*****")
        print(f"Comp:{comp_score},You:{user_score}")
    elif  (choices[user_choice-1] =="Rock" and comp_choice=="Scissor") or (choices[user_choice-1] =="Paper" and comp_choice=="Rock") or (choices[user_choice-1] =="Scissor" and comp_choice=="Paper"):
        print("*****You Won*****")
        user_score+=1
        print(f"Comp:{comp_score},You:{user_score}")
    else:
        print("*****Computer Won*****")
        comp_score+=1
        print(f"Comp:{comp_score},You:{user_score}")
if user_score>comp_score:
    print("*****You won the Game*****")
else:
    print("*****Computer won the Game*****")

