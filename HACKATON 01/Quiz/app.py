import random


# dictionary with start questions
questions = {
    'W którym roku Titanic zatonął na Oceanie Atlantyckim 15 kwietnia podczas dziewiczej podróży z Southampton?' : '1912',
    'Jak nazywa się największa firma technologiczna w Korei Południowej?' : 'samsung',
    'Który metal odkrył Hans Christian Oersted w 1825 roku?': 'aluminium,',
    'Jaka jest stolica Portugalii?':'Lizbona'
}

# function that selects and return question
def choise_question():
    list_with_questions = list(questions.keys())
    question = random.choice(list_with_questions)
    print(len(list_with_questions))
    return question


