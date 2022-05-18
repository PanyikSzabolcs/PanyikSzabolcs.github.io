class Kolcsonzes:
    def __init__(self, sor):
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.jazon = adatok[1]
        self.eora = int(adatok[2])
        self.eperc = int(adatok[3])
        self.vora = int(adatok[4])
        self.vperc = int(adatok[5])


def ftime(ora, perc):
    result = ''
    if ora < 10:
        result += '0' + str(ora) + ':' 
    else:
        result += str(ora) + ':' 
    if perc < 10:
        result += '0' + str(perc)
    else: 
        result += str(perc)
    return result
        
        
        
lista = []
file = open('kolcsonzesek.txt', 'r', encoding='utf-8')
file.readline()
sor = file.readline()
while sor:
    adatsor = Kolcsonzes(sor.strip())
    lista.append(adatsor)
    sor = file.readline()
file.close()

kolcsonzesek_szama = len(lista)
print(f'5. feladat: Napi kölcsönzések száma: {kolcsonzesek_szama}')

beker = input(f'6. feladat: Kérek egy nevet: ')
print(f'\t{beker} kölcsönzései:')
talalt =  False

for menet in lista:
    if menet.nev == beker:
        print(f'\t{ftime(menet.eora, menet.eperc)} - {ftime(menet.vora, menet.vperc)}')
        talalt = True
        
if not talalt:
    print('\tNem volt ilyen nevű kölcsönző!')

idopont = input(f'7. feladat: Adjon meg egy időpontot óra:perc alakban: ').split(':')

for menet in lista:
    if idopont[0] <= menet.eora

# print(f'8. feladat: A napi bevétel: ')

# print(f'10. feladat: Statisztika\n A - {}\n B - {}\n C - {}\n D - {}\n E - {}\n F - {}\n G - {}\n ')