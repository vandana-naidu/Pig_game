import random

players_score=[]

def roll(no_of_players,current_score=0):
    for each_player in range(no_of_players):
        print("player",each_player+1,"turn")
        while True:
            play=input("""do you want to roll a die: 
            enter 'y' for yes and 'n' for no: """).lower()
            if play=="y":
                value_on_die=random.randint(1,6)
                if value_on_die==1:
                    print("your value on die is: ",value_on_die)
                    print("Game ends!!")
                    current_score += value_on_die
                    print("final score of player",each_player+1,"is",current_score)
                    players_score.append(current_score)
                    if each_player + 1 != no_of_players:
                        print("-----------------next player-----------------")

                    current_score=0
                    break

                else:
                    print("your value on die is: ",value_on_die)
                    current_score+=value_on_die
                    print("your current score:",current_score)


            elif play=="n":
                print("okay quiting..,")
                print("your score till now is:",current_score)
                players_score.append(current_score)
                current_score=0
                if each_player+1!=no_of_players:
                     print("-----------------next player-----------------")
                break

            else:
                print("please enter either y/n")
    max_score=max(players_score)
    ind=players_score.index(max_score)
    print("----------------------*******---------------------------")
    print("the final winner with highest score",max_score," is player",ind+1)




if __name__=="__main__":
    instructions="""-->This game is for 2 to 4 players, you have to first select how many players
-->for player 1 turn.., the player 1 can roll a die until he gets 1 on the die
-->when the number on the die is 1, the player 1 turn ends
-->each number on the die(until the 1) is added to their score
-->at the end.., the player will highest score will win"""
    print(instructions)
    no_of_players = int(input("enter no oof players: (2-4)"))
    while True:

        if no_of_players < 2 or no_of_players > 4:
            no_of_players=int(input("please enter number between 2-4 :)"))

        else:
            roll(no_of_players)
            break