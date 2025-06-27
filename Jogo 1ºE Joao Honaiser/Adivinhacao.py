import random
import os
from colorama import Fore, Style, init

int(autoreset=True)  # Inicializa o colorama e reseta a cor automaticamente

erros = 0
sorteado = random.randrange(0, 100)

Jogador = int(input(Fore.CYAN + "Digite seu número!   "))

while sorteado != Jogador:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if sorteado > Jogador:
        print(Fore.YELLOW + "ERRO, o número é maior")  # Jogador precisa chutar mais alto
    else:
        print(Fore.YELLOW + "ERRO, o número é menor")  # Jogador precisa chutar mais baixo
    
    erros += 1
    Jogador = int(input(Fore.CYAN + "Digite seu número:   "))

print(Fore.GREEN + f"Número {Jogador}, você acertou em {erros + 1} tentativas! 🎉")