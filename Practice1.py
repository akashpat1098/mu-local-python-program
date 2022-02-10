# Program tell user when they will turn into 100 yrs after providing year or age
from datetime import date

from numpy import intersect1d
if __name__=="__main__":
    '''input should be between 1 to 130 and should be only numeric and between 1000 to 9999'''
    inp=input("Enter the Age or Year of birth:")
    while True:
        try:
            inp=int(inp)
            if (1<=inp<=130 or 1000<=inp<=9999):
                if 90<=inp<=130:
                    print("Your age is {}\nYou seems oldest person".format(inp))
                    break
                elif 1<=inp<=89:
                    print("Your age is {}".format(inp))
                    break
                elif 1000<=inp<=9999:
                    print("Your year of birth is {}".format(inp))
                    break
            else:
                inp=input("You entered wrong input.Please try again:")
                continue
        except ValueError:
            inp=input("You entered wrong input.Please try again:")
            continue
today_date=date.today()
if 1<=inp<=99:
    yrsat100=(100-inp)+today_date.year
    print("You will turn 100 in {}".format(yrsat100))
elif 100<=inp<=130:
    yrsat100=today_date.year-(inp-100)
    print("You already turned 100 in {} i.e {} year ago".format(yrsat100,inp-100))
elif 1000<=inp<=9999:
    yrsat100=inp+100
    if inp<today_date.year:
        print("You will turn 100 in {}".format(yrsat100))
    elif inp>today_date.year:
        print("Your are not yet born! but still you will turn 100 in {}".format(yrsat100))
    interestedYr=int(input("Enter the year you want to know your age in:"))
    if interestedYr>inp:
        print(f"You will be {interestedYr-inp} year old in {interestedYr}")
    else:
        print(f"You are not born")

