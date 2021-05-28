rekordok = input("add meg vesszovel elvalasztva, hogy miket akarsz rogziteni: ")
rekord_lista = rekordok.split(',')
print(rekord_lista)

adatok = {}

for r in rekord_lista:
    adatok[r] = input(f'Add meg a(z) ' + str(r) + ' -t: ')

print(adatok)
