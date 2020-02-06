import random 

# Compute choice a number  between 1 and 100
ChoosedNumber = random.randint(1, 100)
print("Choose a number")
UserTry = 0
for x in range(10):  # 10 try
    UserNumber = int(input())
    UserTry += 1  # Increment each time user is entering a new number
    if UserNumber < ChoosedNumber:
        print("It's bigger")
    elif UserNumber > ChoosedNumber:
        print("It's smaller")
    elif UserNumber == ChoosedNumber:
        print("You win ! (Nothing)")
        exit(1)
    if UserTry >= 10:
        print("You lose !")
        exit(1)
