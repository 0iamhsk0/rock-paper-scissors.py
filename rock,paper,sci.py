import random

def take_value():
    options = ['rock','paper','scissors']
    players_choice = input('Enter your choice!(rock,paper,scissors): ')
    computers_choice = random.choice(options)
    choices = {'player' : players_choice ,'computer' : computers_choice}
    return choices

def give_result(player , computer):
    print('So you have chosen: {0}, computer has chosen: {1}'.format(player,computer))
    if player == computer:
        return 'Its a tie!!'
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock beats Scissors! You win!!'
        else:
            return 'Paper covers Rock! You Loose!'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers Rock! You Win!!'
        else:
            return 'Scissors cut Paper! You Loose!'
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cut Paper! You Win!!'
        else:
            return 'Rock beats Scissors! You Loose!'

choices = take_value()
result = give_result(choices['player'], choices['computer'])
print(result)
