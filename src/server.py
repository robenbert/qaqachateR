import socket
import threading


class myfred(threading.Thread):
    msgs = []
    def __init__(self, client, chat):
        threading.Thread.__init__(self)
        self.client = client
        self.chat = chat

    def search(self):
        lock.acquire()
        for i in range(0, len(myfred.msgs)):
            if myfred.msgs[i][0] == self.chat:
                lock.release()
                return i

    def run(self):
        chat = -1
        lock.acquire()
        for i in range(0, len(myfred.msgs)):
            if myfred.msgs[i][0] == self.chat:
                chat = i
        if chat == -1:
            myfred.msgs.append([self.chat])
            for i in range(0, len(myfred.msgs)):
                if myfred.msgs[i][0] == self.chat:
                    chat = i
        lock.release()
        while True:
            msg = self.client.recv(1024)
            msg = str(msg, "utf8")
            print(msg)
            if msg.split(" ")[0] == "send":
                lock.acquire()
                myfred.msgs[chat].append(msg.split(" ", 1)[1])
                lock.release()
            elif msg == "show":
                lock.acquire()
                liste = ""
                for i in range(1, len(myfred.msgs[chat])):
                    liste += myfred.msgs[chat][i] + "\n"
                self.client.send(bytes(liste, "utf8"))
                lock.release()
            elif msg == "exit":
                self.client.close()
                break


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

freds = []
lock = threading.Lock()
i = 0
server.bind(("127.0.0.1", 1337))
server.listen(5)
while True:
    (client, addr) = server.accept()
    print(f"mit client {addr} verbunden")
    chat = str(client.recv(1024), "utf8")
    freds.append(myfred(client, chat))
    freds[i].start()
    i += 1
