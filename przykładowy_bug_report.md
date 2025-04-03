# Raport o blędzie

## Numer / identyfikator błędu
1, 2, 3

## Tytuł błędu
1.Literówka
2.zmienna symbols nie posiada zamkniecia zmiennej
3.Źle ułożone tabulatory
## Platforma / środowisko

pycharm

## Opis



## Kroki do reprodukcji

1.Usuniecie lkitery "f" z sample
2.Zamknięcie zmiennej symbols
3.Poprawienie tabulatorow
## Oczekiwany i rzeczywisty wynik

Oczekiwnay: Kod powinien wygenerowac haslo
Rzeczywisty: kod nie dziala poprawnie

## Zrzut ekranu
![image](https://github.com/user-attachments/assets/94a6d072-486f-4381-aae7-eca8be728580)

##sample
wybiera dlugos stringa np gdy jest 16 to wybierze 16 liter/liczb/symboli

##Poprawiony kod
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}*;/,._-'"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
print(password)

#Co robil
Karol, Dawid P
