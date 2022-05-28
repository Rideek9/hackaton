Wisielec:

Program, będący implementacją gry "wisielec".

Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.

1. komputer wybiera słowo z listy dostepnych słów wykorzystując funkcje random
2. Następnie komputer ukrywa słowo za myślnikami - iloś myślników rówana sie długosci słowa
3. Użytkownik ma 10 prób na zgadnęcie słowa
4. Wygląd i działanie gry:
   1. komputer pokazuje ukryte słowo
   2. prosi użytkownika o podanie litery
   3. kiedy litera istnieje w zbiorze komputer prosi użytkownika o podanie litery jeszcze raz, gdy litera nie isnieje w zbiorze komputer dopisuje litere do zbioru
   4. program sprawdza czy litery ze zbioru są zawarte w słowie
   5. w momencie gdy użytkownik literę która nie jest zawarta w słowie komputer odejmuje 1 próbę
   6. gdy litera zawiera się w słowie użytkownik nie traci ruchu i wybiera następną literę
   7. w momencie gdy użytkownik zgadznie słowo program wysyłą komunikat o wygranej
   8. Jeśli użytkownik przekroczy ilość prób komputer daje komunikat o przegranej
