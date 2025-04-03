# generator_hasla
# Zadanie do wykonia:
1. Zapoznaj się z zasadami tworzenia **raportu o błędzie (bug report)** :
   
   https://myservername.com/how-write-good-bug-report#Some_Bonus_Tips_To_Write_A_Good_Bug_Report
   
3. Stwórz konspekt zagadnienia
4. Przetestuj podany kod na dołączonym obrazku: **Generator hasła**
5. Stwórz raport o blędzie na podstawie przykładowego pliku.

import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,._-''"
        all = lower + upper + number + symbols
        length = 16
        password=" ".join(random.samplef (all.length))
        print(password)
