# ==============================================
# Hacking : décoder le code romain
# Objectifs:
# - utilisation des boucles
# - utilisation des tests
# ==============================================

# 

clef = 10
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
messageClair = "Ceci est mon premier message a coder"
messageChiffre = ""

#messageClair = input("Entrez un texte à chiffrer avec le code de Cesar : ")

# CODAGE

for c in messageClair:
	i = 0
	if c == " ":
		messageChiffre = messageChiffre+c
	else:
		for l in lettres:
			if c == l :
				new_pos = (i+clef) % len(lettres)
				new_lettre = lettres[new_pos]
#				print("Lettre clair ",c, " pos ",i, ": lettre chiffrée ",new_lettre, " pos ",new_pos)
				messageChiffre = messageChiffre+new_lettre
			i+=1

print("Clef de chiffrement : ",clef)
print("Message clair       : ",messageClair)
print("Message codé        : ",messageChiffre)


# DECODAGE

messageADecoder = "Yrlfl xq qrxyhdx phvvdjh txh mh vrxkdlwh ghfrghu"

messageDecode = ""

for c in messageADecoder:
	i = 0
	if c == " ":
		messageDecode = messageDecode+c
	else:
		for l in lettres:
			if c == l :
				new_pos = (i-clef) % len(lettres)
				new_lettre = lettres[new_pos]
				messageDecode = messageDecode+new_lettre
			i+=1

print("Clef de chiffrement : ",clef)
print("Message codé        : ",messageADecoder)
print("Message décodé      : ",messageDecode)

# DECODAGE SANS CONNAITRE LA CLEF DE CHIFFRAGE
# Cassage par force brute

messageADecoder = "MoCCo vsqxo oBC moACksxowoxC vk zvDB vsBslvo no CyDCoB"

for clef in range(20):
	clef = clef + 1
	messageDecode = ""
	for c in messageADecoder:
		i = 0
		if c == " ":
			messageDecode = messageDecode+c
		else:
			for l in lettres:
				if c == l :
					new_pos = (i-clef) % len(lettres)
					new_lettre = lettres[new_pos]
					messageDecode = messageDecode+new_lettre
				i+=1
	print("[",clef," ] : ",messageDecode)	





