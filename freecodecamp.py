import random


def get_choices():
    palyer_choice = input('enter choice: ')
    options = ['rock','paper','sisssors']

    computer_choice = random.choice(options)
    choice = {'player': palyer_choice, 'computer': computer_choice}

    return choice

def check_win(player, computer):
    print(f"you chose {player}, coputer chose {computer}")
    if player == computer:
        return 'tie'
    elif player == 'rock':
        if computer == 'sissor': 
            return 'Rock smashes sissors! You Win hurray!!'
        else:
            return 'paper covers rock! you loose.'
    elif player == 'sissor':
        if computer == 'paper':
            return 'paper covers rock! You win.'
        else:
            return 'Rock smashes sissor! you lose.'
    elif player == 'paper':
        if computer == 'rock':
            return 'paper covers rock! you win.'
        else:
            return 'sissor cuts the paper! you lose.'
    
choices = get_choices()
result = check_win(choices['player'],choices['computer'])
print(result)



