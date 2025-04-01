import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-'"
all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all,length)) 
# sample picks out a random symbol length amount of times from the provided string
print(password)