import random


# dictionary with start questions
questions = {
    'W którym roku Titanic zatonął na Oceanie Atlantyckim 15 kwietnia podczas dziewiczej podróży z Southampton?' : '1912',
    'Jak nazywa się największa firma technologiczna w Korei Południowej?' : 'samsung',
    'Który metal odkrył Hans Christian Oersted w 1825 roku?': 'aluminium,',
    'Jaka jest stolica Portugalii?':'Lizbona'
}
# all variables
start_game = 0
user_round = 0

# function that selects and return question
def choise_question():
    list_with_questions = list(questions.keys())
    question = random.choice(list_with_questions)
    return question

def game_start(game):
    if game == 0 :
        level_game = user_level()
        numb = number_user_arremps(level_game)
        user_round = numb
        start_game = 1
        return user_round, start_game

def number_user_arremps(level):
    round_list ={
        'a': 10,
        'n' : 5,
        'm' : 3
    }
    for key, value in round_list.items():
        if level == key:
            print(f"Masz {value} prób ")
            return value


def user_level():
    levels_list = {'a' : 'amator',
                   'n': 'normalny',
                   'm': 'mistrz'}
    while True:
        level = input('Wybierz poziom trudności: [a] - amator, [n] - normalny, [m] - mistrz\n--> ')
        level.lower()
        if level  in levels_list.keys():
            for key, value in levels_list.items():
                if key == level:
                    print(f'Wybrałeś poziom {value}')
            return level
        else:
            print('Taki poziom nie istnieje, spróbuj jeszcze raz')
            continue
        break


def main():
    # module start game
    start_game =0
    start_start = game_start(start_game)
    list_start = list(start_start)
    start_game = list_start[1]
    user_round = list_start[0]



    # question = choise_question()
    # print(question)

main()