import random
HandsPlayed = []
ComputerHasChosen = 'null'
WinningHand = 'null'
def take_turn():
    Output = random.randrange(1,4)
    global ComputerHasChosen
    if (Output == 1):
        ComputerHasChosen = "rock"
    elif (Output == 2):
        ComputerHasChosen = "paper"
    else:
        ComputerHasChosen = "scissors"

print("Rock, Paper, Scissors?")
UserHasChosen = input("Please enter your Choice.\n")

def judge():
    global ComputerHasChosen, UserHasChosen, HandsPlayed, WinningHand
    #Player = 1, Computer = 2
    HandsPlayed = [UserHasChosen,ComputerHasChosen]
    if(HandsPlayed[0] + HandsPlayed[1] == 'rockscissors' or HandsPlayed[0] + HandsPlayed[1] == 'scissorsrock'):
        #print('rock wins')
        WinningHand = 'rock'
    elif (HandsPlayed[0] + HandsPlayed[1] == 'paperscissors' or HandsPlayed[0] + HandsPlayed[1] == 'scissorspaper'):
        #print('scissors wins')
        WinningHand = 'scissors'
    elif (HandsPlayed[0] + HandsPlayed[1] == 'paperrock' or HandsPlayed[0] + HandsPlayed[1] == 'rockpaper'):
        #print('paper wins')
        WinningHand = 'paper'
    else:
        #print("Draw")
        pass

def find_winner():
    if (WinningHand == UserHasChosen):
        print('You win!')
    elif(WinningHand == ComputerHasChosen):
        print('You lose!')
    else:
        print('Draw')

while True:
    if(UserHasChosen != "rock" and UserHasChosen != "paper" and UserHasChosen != "scissors"):
        UserHasChosen = input("Invalid choice, please choose rock,paper or scissors.\n")
    else:
        take_turn()
        print("You chose:", UserHasChosen)
        print("Computer chose:", ComputerHasChosen)
        judge()
        find_winner()
        break
