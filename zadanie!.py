import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,._-''"
#Zmienne są definiowane globalnie. W większych projektach lepiej używać stałych lub konfiguracji w osobnym module.
        all = lower + upper +numbers +symbols                   #błąd, nie ma takiej zmiennej (number), brakuje -s = numbers, #all może prowadzić do nieoczekiwanych efektów
            length = 16                        #Długość 16 może być zbyt krótka dla bezpiecznego hasła. Zalecana długość to minimum 12 znaków.
#Problem:
#Brak sprawdzania, czy length jest dodatnią liczbą całkowitą.
#trzeba dodac walidacje wejscia
                password = "".join(random.samplef (all, length))   #Funkcja random.sample() nie istnieje (brakujące ()). Poprawna składnia to random.sample(all, length)., #zamiast random samplef uzyj random.choices()
                    print(password)