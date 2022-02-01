import random
n=input("enter your name : ")
print("Hello",n,"welcome to snake water gun game")
rounds=1
options=["r","p","s"]
print("\nyou have three options r-rock,p-paper,s-scissor")
player_win=0
computer_win=0
while rounds<11:
    print(f"*round no.{rounds}")
    player_input=input("enter your choice ")
    if player_input!= 'r' and player_input!= 'p' and player_input!= 's':
        print('Invalid input! Please enter again')
        continue
    computer_input=random.choice(options)
    if computer_input==player_input:
        print("draw")

    if computer_input=="r":
        if player_input=="p":
            print("you got point!")
            player_win+=1
        elif player_input=="s":
            print("no point")
            computer_win+=1

    if computer_input=="p":
        if player_input=="r":
            print("no point")
            computer_win+=1
        elif player_input=="s":
            print("you got point")
            player_win+=1

    if computer_input=="s":
        if player_input=="r":
            print("you got point")
            player_win+=1
        elif player_input=="r":
            print("no point")
            computer_win+=1
    rounds+=1
print("your score is:",player_win)
print("opponent score is:",computer_win)
if player_win>computer_win:
    print("congratulations,you have won the game!")
elif computer_win>player_win:
    print("sorry,you have lost the game!")
else:
    print("game is draw!!!!!")
