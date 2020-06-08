#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string
from IPython.display import clear_output


# In[ ]:


def text_importer():    
    with open("word_list.txt") as imported_string:
        word_bank = (imported_string).read().split()
        random.shuffle(word_bank)
        return word_bank


# In[ ]:


def get_game_word(word_bank):
    game_word = list(word_bank.pop().lower())
    return game_word


# In[ ]:


def replay():
    return input('Play again? Enter Y or N: ').lower().startswith('y')


# In[ ]:


def display_board(zone):
    print('________')
    print('\\|    ' + zone[0])
    print(' |    ' + zone[1])
    print(' |   ' + zone[2])
    print(' |   ' + zone[3])
    print('/|\\')
    print('"""""""""')


# In[ ]:


def hang_the_figure(player_lives):
    if player_lives == 7:
        game_board = [' ',' ','   ','   ']
    elif player_lives == 6:
        game_board = ['|',' ','   ','   ']
    elif player_lives == 5:
        game_board = ['|','O','   ','   ']
    elif player_lives == 4:
        game_board = ['|','O',' | ','   ']
    elif player_lives == 3:
        game_board = ['|','O','/| ','   ']
    elif player_lives == 2:
        game_board = ['|','O','/|\\','   ']
    elif player_lives == 1:
        game_board = ['|','O','/|\\','/  ']
    elif player_lives == 0:
        game_board = ['|','O','/|\\','/ \\']
    else:
        pass
    display_board(game_board)


# In[ ]:


def hangman():
    word_bank = text_importer()
    word = get_game_word(word_bank)
    word_letters = set(word)
    #alphabet = set(string.ascii_lowercase)
    guessed_letters = set()
    lives = 7
    
    while word_letters and lives:
        hang_the_figure(lives)
        print("\nYou have",lives,"lives remaining")
        if guessed_letters:
            print("Guessed letters: ","".join(sorted(guessed_letters)))
        disguised_word = [_ if _ in guessed_letters else "*" for _ in word]
        print("The word to guess is:", "".join(disguised_word).capitalize())
        
        current_guess = input('Please enter your next guess: ').lower()
        if current_guess.isalpha() and current_guess not in guessed_letters:
            guessed_letters.add(current_guess)
            if current_guess in word_letters:
                word_letters.remove(current_guess)
            else:
                print("Wrong guess")
                lives -= 1
                
        elif current_guess in guessed_letters:
            print("\nYou already guessed:",current_guess.upper())

        else:
            print("\nBad guess")
    if lives == 0:
        clear_output()
        hang_the_figure(lives)
        print("You lose")
        print("The word was:","".join(word).capitalize())
    else:
        clear_output()
        hang_the_figure(lives)
        print("Congratulations you win")
        print("The word is:","".join(word).capitalize())


# In[ ]:


while True:
    playing: True
    hangman()
    if not replay():
        break

