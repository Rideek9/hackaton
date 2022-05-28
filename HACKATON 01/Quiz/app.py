import random


# dictionary with start questions
questions = {
    'W którym roku Titanic zatonął na Oceanie Atlantyckim 15 kwietnia podczas dziewiczej podróży z Southampton' : '1912',
    'Jak nazywa się największa firma technologiczna w Korei Południowej' : 'samsung',
    'Który metal odkrył Hans Christian Oersted w 1825 roku?': 'aluminium',
    'Jaka jest stolica Portugalii':'Lizbona','Ile godzin żyje ważka':'24',
    'W którym roku po raz pierwszy ukazał się Ojciec chrzestny': '1972',
    'W jakim śródziemnomorskim kraju urodził się reżyser Frank Capra, znany z filmu To wspaniałe życie': 'Włochy',
    'Polski kierowca F1 - podaj nazwisko': 'Kubica'
}

# function that selects and return question
def choise_question():
    list_with_questions = list(questions.keys())
    question = random.choice(list_with_questions)
    return question

# function witch let user choise level
def game_start(game):
    if game == 0:
        level_game = user_level()
        numb = number_user_attemps(level_game)
        user_round = numb
        start_game = 1
        return user_round, start_game

# function that decides how many attempts the user has
def number_user_attemps(level):
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

# function where the user selects the level
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

# function witch return question and values
def game_question():
    question = choise_question()
    for keys, value in questions.items():
        if question == keys:
            return question, value

# game function
def game():
    print('\nPytanie')
    question_and_anwser = list(game_question())
    question = question_and_anwser[0]
    anwser = question_and_anwser[1]
    print(question,"?")
    odp = input("Poprawna odpowiedź to?:\n--->")
    if odp.lower().strip() == anwser.lower():
        del questions[question]
        print("dobra odpowiedź")
        return 'ok'
    else:
        del questions[question]
        print('zła odpowiedź')

# function end game
def end_game(points,start,end):
    if len(questions.keys()) == 0:
        print('\nOdpowiedziałeś na wszystkie pytania')
        print(f'Zdobyłeś: {points} punktów ')
        print(f'Straciłeś prób: {start - end}')
        exit()

# funciot wer AI choice bonus for user
def bonus_round():
    number = random.randint(0,100)
    if 10 <= number <= 30:
        print('Bonus -- punkty 2 razy')
        return 2
    elif 50<= number <= 60:
        print('Bonus -- 3 razy wiecej punktów')
        return 3
    elif 70<= number <= 75:
        print('Bonus -- 4 razy wiecej punktów !!!!')
        return 4
    elif number == 88:
        print('MEGA Bonus -- 5 razy wiecej punktów  WOOOW!!!!')
        return 5
    else:
        return 1

# when user lose all chances function end the game and show result
def user_lose(lose,points):
    if lose == 0:
        print("\nNiestety przegrałeś")
        print(f'Zdobyłeś {points} punktów')
        exit(
        )

# main function where are they all function
def main():
    user_points = 0
    # module start game - start the game and add round for user
    start_game = 0
    element = list(game_start(start_game))
    user_round = element[0]
    start_rounds = element[0]
    start_game = element[1]
    while True:
        user_lose(user_round,user_points)
        end_game(user_points,start_rounds,user_round)
        test = game()
        if test == 'ok':
            bonus = bonus_round()
            user_points += (bonus*10)
        else :
            user_round-=1
        print(f'Liczba Twoich punktów to: {user_points}')

main()