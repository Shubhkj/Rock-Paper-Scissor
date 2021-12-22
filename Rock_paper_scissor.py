import random

def game(comp,you):
    if comp==you:
        print("Game is a tie")
    elif comp=='r':
        if you=='p':
            print("You Win")
        elif you=='s':
            print("You Loose")
    elif comp=='p':
        if you=='s':
            print("You Win")
        elif you=='r':
            print("You Loose")
    elif comp=='s':
        if you=='r':
            print("You Win")
        elif you=='p':
            print("You Loose")
    else:
        print("Don't use your brain if you don't have one")

comp=random.choice(['r','p','s'])
you=input("Choose: Rock{r} Paper{p} Scissors{s}::: ")
print(f"Computer chose {comp}")
print(f"You chose {you}")
game(comp,you)