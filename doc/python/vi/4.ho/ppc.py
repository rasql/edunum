import random

emoji = ['💎', '📜', '✂️']
coups = ['0', '1', '2']
humain = 0
ordi = 0

print('0=pierre ',emoji[0], ' 1=papier ',emoji[1],', 2=ciseaux ',emoji[2])
x = input('votre choix:')

while x :
    you = int(x)
    if x in coups:
        bot = random.randint(0, 2)
        print('(vous)',emoji[you], 'contre' ,emoji[bot],'(ordi)')
        if you == bot :
            print('match nul')
        elif you == 0 and bot == 2:
            print('humain gagne')
            humain = humain + 1
        elif you == 1 and bot == 0:
            print('humain gagne')
            humain = humain + 1
        elif you == 2 and bot == 1:
            print('humain gagne')
            humain = humain + 1
        else:
            print('ordi gagne')
            ordi = ordi + 1    
    else:
        print('Choisissez entre 0,1,2')
    x = input('votre choix:')

print('game over')
print('Score final : humain ',humain,' ordi : ',ordi)
if humain  == ordi:
    print('match nul')
elif humain > ordi:
    print('vous avez gagné')
else:
    print('l\'ordi a gagné')
