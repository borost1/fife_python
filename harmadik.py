# ['Boros', 'Tamás', 33]

lista = ["a", "a", "b", "A", "Sanyi", "Alfonz", "Zoli", 12]
print(lista)
kor = lista.pop(len(lista)-1)
print(lista)
lista.insert(0, kor)
print(lista)
lista[0] = str(lista[0])
lista.sort()
print(lista)
hany_darab_a = lista.count('a')
print(hany_darab_a)
print(lista)
lista_2 = lista.copy()
print(lista_2)
del lista[0]
print(lista)
print(lista_2)
osszeg = lista + lista_2
print(osszeg)

szoveg = "Külföldi jeladós barátkeselyűt lőhettek le Szabolcs-Szatmár-Bereg megyében, írja a Magyar Madártani és Természetvédelmi Egyesület (MME) közleménye és a parlagisas.hu."
szoveg_visszafele = list(szoveg)
szoveg_visszafele.reverse()
print(szoveg_visszafele)
szoveg_visszafele = ''.join(szoveg_visszafele)
print(szoveg_visszafele)
