# QUIZ - check your knowledge

This game test your general knowledge.
The game have 8 questions, but you can add next question and test your friends.


## Technology to used in project
  * Python 3.9


## add question and answer
If you want add question whit answer you must use dictionary "questions".
This dictionary is the top project in app.py file.
You must add in code question in quote and that same about answer. 
Separate question and answer with colon.

## Rules the game
  1. You have three levels
      * amator - in this option player has 10 life
      * normalny - in this option player has 5 life
      * mistrz - in this option player has 3 life
  2. When you select level computer gives information:
     1. How many rounds you have
     2. How many question in the game
  3. Computer random question and wait to answer.
  4. When you take correct answer you tak point. In the game you have bonus points. In the game is a function that draws the appropriate multiplier:
     * multiplier times 1 - you have 10 points
     * multiplier times 2 - you have 20 points
     * multiplier times 3 - you have 30 points
     * multiplier times 4 - you have 40 points
     * multiplier times 5 - you have 50 poinst
  5. The multiplier random in the appropriate range, the rang in the function called " bonus_round"   
  6. The player win when he answered the all questions, then computer gives information about how many points user have.
  7. The player loses when he lose all chance.


## Instal the game 
You must copy this link in your git


     git clone https://github.com/Rideek9/hackaton/blob/main/HACKATON%2001/Quiz

### License
It's a free game, you can use code without permission





Quiz

Stwórz grę, która zawiera pytania z wiedzy ogólnej (Trivial pursuit)
Konieczność użycia modułu random.

1. Wszystkie pytania będą umieszczone w słowniku
2. Na początku gry kompyter pokazuje użytkownikowi ilość dostępnych pytań.
3. Użytkownik dostaje informację jaki poziom trudności wybiera (nowicjusz, normlany, mistrz)
4. W zależności od poziomu użytkownik ma dostępną ilość szans, które odejmują się w przypadku złej odpowiedzi na pytanie.
    a) nowisjusz - 10 szans
    b) normalny - 5 szansz
    c) mistrz - 3 szanse
5. Komputer losuje pytanie i prosi użytkownika o odpowiedź jeśli odpowiedź jest poprawna użytkownik zyskuje 10 pkt jeśli odpowiedź jest zła użytkownik traci swoją szansę.
6. Program bierze pod uwagę możliwe błędy użytkownika czyli wielkość liter, białe znaki - i konwertuje wszystko na jeden typ tekstowy
7. Użytkowniki wygrywa w momencie kiedy odpowie na wszystkie pytania, przegrywa kiedy straci wszystkie szanse
8. Na koniec gry pokazuje się tablica wyników 
9. Rundy bonusowe będzie to mnożnik punktów który trafia się w losowych momentach komputer losuje liczby z przedziału 0-100 w zależności jaka liczba wypadnie taki bonus przypadnie dla użytkownika., o rundzie losowej użytkownik będzie infomrowany razem z informacją o mnożniku punktów w danej rundzie.
    a) 2x - liczby w przedziale 10-30
    b) 3x - liczby w przedziale 50-60
    c) 4x - liczba w przedziale 70-75
    d) 5x - liczba  88