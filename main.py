import random 

comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water, 2 for Gun: \n"))

def compare(comp, user): 
    if comp == user: 
        return 0 
    if comp == 0 & user == 1: 
        return -1 
    
    if comp == 1 & user == 2: 
        return -1 
    
    if comp == 2 & user == 0: 
        return -1 

score = compare(comp, user)

print("Computer", comp)
print("You", user)

if score == 0: 
    print("It's a Draw")
elif score == -1: 
    print("You Lose")
else: 
    print("You Won")
