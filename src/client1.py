import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ("127.0.0.1", 1337)
client.connect(server_addr)
client.send(bytes(input("welcher chat: "), "utf8"))
print("""sie sind mit qaqachateR verbunden dass hier ist eigentum der
roman und qaqa gmbh schreiben sie send und danach eine nachricht um eine nachricht zu versenden
mit show können sie sich alle nachrichten ansehen mit exit können sie verlassen
version 0.1""")

while True:
    msg = input(": ")
    if msg == "show":
        client.send(bytes(msg, "utf8"))
        msg = client.recv(1024)
        msg = str(msg, "utf8")
        print(msg)
    elif msg.split(" ")[0] == "send":
        client.send(bytes(msg, "utf8"))
    elif msg == "exit":
        client.send(bytes(msg, "utf8"))
        break
