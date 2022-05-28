import random

word_list = ['drzewo','most','sauna','wieszak','walec','tancerka','cyrk','parasolka','astronauta']

# function witch select a word
def word_element(list):
    element = random.choice(list)
    return element

# function wich user choise letter, if letter is exist user must choise next letter
def user_choice(list_letter):
    while True:
        choise = input('Podaj litere -->  ')
        if choise in list_letter:
            print('Litera istnieje')
            continue
        else:
            return choise
            break

# function where the user play the game
def game(word_list,letter_list):
    is_letter = []
    for letter in letter_list:
        for letter_w in word_list:
            if letter == letter_w:
                is_letter.append(letter)
    word=''
    for letter in word_list:
        if letter in is_letter:
            word+=letter
        else:
            word+='-'
    hidden_word = hidden_element(word)
    return word, hidden_word

# function where words is hidden
def hidden_element(element):
    how_mane_hidden = element.count('-')
    return how_mane_hidden

def main():
    user_round = 10
    rounds = 0
    word = word_element(word_list)
    word = list(word)
    letters =[]
    last_move = game(word,letters)[1]
    while rounds < user_round:
        games = game(word,letters)[0]
        hidden = game(word,letters)[1]
        print('\nSzukane słowo: \n',games.upper())
        if '-' not in games:
            print(f'\nWygrałeś gratulacje!!!')
            break
        letter = user_choice(letters)
        letters.append(letter)
        if last_move != hidden:
            last_move = hidden
        else:
            user_round-=1
            last_move = hidden

    if user_round == 0:
        print('Przegrałeś spróbuj ponownie :)')

main()