import random
import sys

word_list = ['Disaster', 'Courage', 'Justice', 'Harmony', 'Freedom', 'Passion', 'Comfort', 'Laughter', 'Loyalty', 'Silence', 'Mystery', 'Sunrise', 'Victory', 'Wisdom', 'Success', 'Vibrant', 'Journey', 'Compass', 'Calmness', 'Kindness']
empty_list = []
chosen_word = random.choice(word_list).lower()

last_letter =chosen_word[6]
first_letter =chosen_word[0]   

for x in range(len(chosen_word)):
    empty_list += '_'

print(chosen_word)
print(f'Word starts with {first_letter} Ends with {last_letter}')


correct = '''
✅
'''
wrong = '''
❌
'''

you_loose = '''
💩
'''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(stages[0])
user_mis = 0
for i in chosen_word:
    user_ch =input('Choose a Letter : ').lower()
    if user_ch == chosen_word[chosen_word.index(i)]:      
        empty_list[chosen_word.index(i)] = user_ch
        print(f'{empty_list}{correct} ')
        print(stages[user_mis])
    else:
        print(f'{empty_list} {wrong} ')
        user_mis += 1
        print(stages[user_mis])
    if user_mis == 6:
        print(f'You Suck! {you_loose}')
'''
    if not '_' in empty_list:
        sys.exit(0)
'''         
