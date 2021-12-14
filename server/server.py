import threading
import socket

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')
    
    while True:
        client, addr = server.accept()
        clients.append(client)

def messagesTreatment(client):
    while True:
        try:
            messages = client.recv(1024)
        except:
            pass

def broadcast(messages, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(messages)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    client.remove(client)