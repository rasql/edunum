# ==============================================
# Hacking : décoder le code romain
# Objectifs:
# - utilisation des boucles
# - utilisation des tests
# https://www.youtube.com/watch?v=vT8q1mXeZ2A
# ==============================================

# 

clef = 10

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_code = ""
messageChiffre = ""


# CALCUL DE L'ALPHABET CODE
alphabet_code = alphabet[clef:len(alphabet)] + alphabet[0:clef]

print("CHIFFREMENT D'UNE LETTRE")
lettreClaire = input("Entrez une lettre à chiffrer avec le code de Cesar : ")
index = alphabet.index(lettreClaire)
lettreChiffre = alphabet_code[index]
print("La lettre chiffrée est : ",lettreChiffre)

print("DECHIFFREMENT D'UNE LETTRE")
index = alphabet_code.index(lettreChiffre)
lettreClaire = alphabet[index]
print("La lettre claire est : ",lettreClaire)


# CODAGE
print("CHIFFREMENT D'UNE PHRASE")
messageClair = input("Entrez un texte à chiffrer avec le code de Cesar : ")

for c in messageClair:
	if c == " ":
		messageChiffre = messageChiffre+c
	else:
		index = alphabet.index(c)
		messageChiffre = messageChiffre + alphabet_code[index]

print(messageClair)
print(messageChiffre)

# DECODAGE
messageClair=""
print("DECHIFFREMENT D'UNE PHRASE")
for c in messageChiffre:
	if c == " ":
		messageClair = messageClair+c
	else:
		index = alphabet_code.index(c)
		messageClair = messageClair + alphabet[index]

print(messageChiffre)
print(messageClair)


# DECODAGE SANS CONNAITRE LA CLEF DE CHIFFRAGE
# Cassage par force brute

print("DECODAGE FORCE BRUTE")

messageADecoder = "moddo vsqxo ocd mobdksxowoxd vk zvec vscslvo no dyedoc"

clef = 0
for clef in range(25):
	clef = clef + 1
	alphabet_code = alphabet[clef:len(alphabet)] + alphabet[0:clef]
	messageDecode = ""
	for c in messageADecoder:
		if c == " ":
			messageDecode = messageDecode+c
		else:
			for l in alphabet_code:
				if (l == c):
					index = alphabet_code.index(l)
					messageDecode = messageDecode+alphabet[index]
	print("[clef ",clef," ] : ",messageDecode)	



# DECODAGE SANS CONNAITRE LA CLEF DE CHIFFRAGE
# Cassage par analyse fréquentielle


print("DECODAGE ANALYSE FREQUENTIELLE")

frequence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

alphabet = "abcdefghijklmnopqrstuvwxyz"
message_code = "moddo vsqxo ocd mobdksxowoxd vk zvec vscslvo no dyedoc"

for c in message_code:
    i = 0
    for l in alphabet:
        if c == l :
            frequence[i] = frequence[i] + 1
        i = i + 1

index_max = frequence.index(max(frequence))
index_lettre_e = 4
clef = index_max - index_lettre_e

message_decode = ""
for c in message_code:
    if c == " ":
        message_decode = message_decode+c
    else:
        i = 0
        for l in alphabet:
            if c == l :
                nouvel_index = (i-clef) % len(alphabet)
                nouvelle_lettre = alphabet[nouvel_index]
                message_decode = message_decode+nouvelle_lettre
            i = i + 1
print("Message decode : ",message_decode)




