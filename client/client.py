#iremos utilizar mutithreading,sendo threadings funções que rodam paralelamentes (uma ao lado da outra)
import threading
import socket

#main será a função principal
def main():
    
    #objeto socket. AF_INET é pra ser IPV4 e SOCK_STREAM é pra dizer que é TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        #tentar a conexão com o servidor, utilizando o host e a porta do servidor
        client.connect(('localhost', 7777))
    except:
        #caso a conexão não consiga ser estabelecida
        return print('\nNão foi possível se conectar ao servirdo!!!')

    #armazenando o nome do usuário
    username = input('Usuário => ')
    print("\nConectado")

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args = [client, username])

    thread1.start()
    thread2.start()

def receiveMessages(client):
    while True:
        try:
            messages = client.recv(1024).decode('utf-8')
            print (messages+'\n')
        except:
            print ('\nNão foi possível permanecer conectado ao servidor')
            print ("Pressione <ENTER> para continuar...")
            client.close()
            break

def sendMessages(client, username):
    while True:
        try:
            messages = input('\n')
            client.send('f<{username}> {messages}'.encode('utf-8'))
        except:
            return 