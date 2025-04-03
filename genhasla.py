import random

lower = "abcdefghijklmnopqrstuwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "0123456789"
symbols = "{}[]()*:/,._-''"

all = lower + upper + numbers + symbols
length = 16

password = "".join(random.sample(all, length))  #commit-powinno być sample a nie samplef problemem w tym kodzie był samplef
print(password)  #metoda sample slorzy do Do wylosowania n elementów bez powtórzeń