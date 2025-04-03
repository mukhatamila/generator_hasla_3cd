import random
def main() -> str:
    '''
    :param all: combines all characters
    :param password: generates random password
    :return: returns random password
    '''
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-'"

    all = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    return password
if __name__ == "__main__":
    print(main())