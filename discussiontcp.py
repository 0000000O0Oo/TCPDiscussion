import socket

host = ""
port = 5467

print("Création du socket en cours...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Création du socket terminé !")
print("Bind du socket à l'hote/port")
s.bind((host, port))
print("Bind terminé ! ")
print("Lancement de l'écoute")
s.listen(1)
client, adresse = s.accept()
print(adresse)
print(client.getpeername())
client.send("Bonjour entrez un mot ou fin si vous voulez arretez la discussion : ".encode("utf-8"))
while(1):
	data = client.recv(1024)
	if data == "fin":
		break
	print(b"Client > " + data)
	mot = input("Serveur > ")
	client.send(mot.encode("utf-8")+"\n".encode("utf-8"))
client.close()
s.close()