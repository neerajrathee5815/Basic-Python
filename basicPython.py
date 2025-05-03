age = input("Please enter your age : ")

def voting_machine(age) :
    if (int(age) < 18 ):
        print("You are not eligible to vote")
    else:
        print("You can vote")

voting_machine(age)