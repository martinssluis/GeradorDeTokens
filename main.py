import string
import random


def geradorDeToken(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

tamanho_string = int(input("Escolha o tamanho do seu token: "))
token = geradorDeToken(tamanho_string) 
print(token)