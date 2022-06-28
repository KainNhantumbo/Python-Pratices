import os

def save_user_data():
  try:
    user_name = input('What is your name? ')
    user_age = int(input('How old are you? '))
    new_user = 'Data collected. Your name is {} and you have {} years old.'.format(user_name, user_age)
    while len(user_name) <= 0:
      user_name = input('What is your name? ')
    print(new_user)
    
    authorize_saving = input('Save your data into a file? (y/n)')
    while len(authorize_saving) <= 0:
      authorize_saving = input('Save data into a file? (y/n)')
    if authorize_saving.lower() == 'y':
     if os.path.isfile('colleted-data.txt'):
      with open('colleted-data.txt', 'a') as file:
        file.write('\n'+ new_user.split('.')[1][1:]+'.')
        read_logs()
     else:
      with open('colleted-data.txt', 'w') as file:
       file.write('\n'+ new_user.split('.')[1][1:]+'.')
       read_logs()
    elif authorize_saving.lower() == 'n':
      print('Thanks!')
    else:
      print('Thanks for your colaboration!')
  except Exception as e:
    print('The was an error: '+ e)

def read_logs():
  answer = input('Read data file? (y/n)').lower()
  while answer != 'y' and answer != 'n':
    answer = input('Read data file? (y/n)').lower()
  try:
    if(answer == 'y'):
     with open('colleted-data.txt', 'r') as file:
      print(file.read())
      print('\n\nThats all. Thanks.')
    else:
      print('Thanks for your time.')
  except Exception as e:
    print(e) 
  
save_user_data()