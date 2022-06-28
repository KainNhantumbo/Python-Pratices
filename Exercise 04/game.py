import random

# starts the game
def game_start():
  choices = ['paper', 'rock', 'scissors']
  computer_choice = random.choice(choices)
  player_choice = None
  
  print('Welcome to Paper - Scissors - Rock Game!')
  while player_choice == None:
    player_choice = input('Choose one from paper, scissors or rock: ').lower()
    
  if computer_choice == player_choice:
    print('Computer choise: {}.'.format(computer_choice))
    print('Your choice: {}.'.format(player_choice))
    print('Congratulations... You win!')
  else:
    print('Computer choise: {}.'.format(computer_choice))
    print('Your choice: {}.'.format(player_choice))
    print('Sorry, you lost this one.')

# runs the game
def run_game():
  game_start()
  continue_game = None
  while continue_game != 'yes' and continue_game != 'no':
    continue_game = input('Play again? (yes/no) ').lower()
  if continue_game == 'yes':
    game_start()
  else:
    print('Bye.')

run_game()