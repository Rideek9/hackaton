import random


# dictionary with start questions
questions = {
    'W którym roku Titanic zatonął na Oceanie Atlantyckim 15 kwietnia podczas dziewiczej podróży z Southampton?' : '1912',
    'Jak nazywa się największa firma technologiczna w Korei Południowej?' : 'samsung',
    'Który metal odkrył Hans Christian Oersted w 1825 roku?': 'aluminium,',
    'Jaka jest stolica Portugalii?':'Lizbona'
}
# all variables
# start_game = 0
start_rounds = 0
user_round = 0
user_points = 0

# function that selects and return question
def choise_question():
    list_with_questions = list(questions.keys())
    question = random.choice(list_with_questions)
    return question

def game_start(game):
    if game == 0:
        level_game = user_level()
        numb = number_user_arremps(level_game)
        user_round = numb
        start_rounds = numb
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
            print(f"Całkowita ilość dostępnych pytań to: {len(questions.keys())}")
            print('Zaczynamy:)\n')
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

def game_question():
    question = choise_question()
    for keys, value in questions.items():
        if question == keys:
            return question, value
def game():
    print('\nPytanie')
    question_and_anwser = list(game_question())
    question = question_and_anwser[0]
    anwser = question_and_anwser[1]
    print(question)
    odp = input("Poprawna odpowiedź to?:\n--->")
    if odp.lower().strip() == anwser.lower():
        print("dobra odpowiedź")
        del questions[question]
        return 10
    else:
        del questions[question]
        print('zła odpowiedź')
        return 1



def end_game(points,start,end):
    if len(questions.keys()) == 0:
        print('Odpowiedziałeś na wszystkie pytania')
        print(f'Zdobyłeś {user_points} ')
        print(f'Straciłeś {start_rounds - user_round} prób zostało CI jeszcz {user_round}')
        exit()


def main():
    # module start game - start the game and add round for user
    start_game =0
    start_start = game_start(start_game)
    list_start = list(start_start)

    while True:
        end_game(user_points,start_rounds,user_round)
        game()




main()