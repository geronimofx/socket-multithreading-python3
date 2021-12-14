#iremos utilizar mutithreading,sendo threadings funções que rodam paralelamentes (uma ao lado da outra)
import threading
import socket

#main será a função principal
def main():
    
    #objeto socket. AF_INET é pra ser IPV4 e SOCK_STREAM é pra dizer que é TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
