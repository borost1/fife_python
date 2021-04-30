'''
1914-ben a matekamtikus Prasantha Mahalanobis meglátogatta Cambridge-ben az akkor már nagy hírnévnek örvendő kollégáját
és honfitársát, Ramanujant.

Mahalanobis magával vitt egyet az akkoriban rendkívül népszerű The Strand című folyóiratból. Ebben jelentek meg többek
közt az első Sherlock Holmes történetek, de volt benne egy rejtvényrovat is, amelyet a kor egyik legnagyobb rejtvény-
alkotója, Henry Dudeney szerkesztett.

Mahalanobis, tesztelendő Ramanujan legendás képességeit, rá is mutatott az éppen aktuális számban található egyik
rejtvényre, mely a következőképpen szólt:
Van egy fickó, aki egy hosszú utcában lakik. A házak számozása 1-gyel kezdődik, és folyamatos, tehát 1, 2,
3 ... stb. A fickó azt állítja, hogy ő abban a házban lakik, amelyre az igaz, hogy a tőle visszább elhelyezkedő házak
házszámainak összege, és tőle az utca felé haladva lévő házak házszámának összege megegyezik.

Ramanujan természetesen rávágta a helyes választ (sőt: az összes helyes választ).
Az ő megoldásával is fogalkozunk majd, de egyelőre próbáljuk meg próbálgatós, azaz brute force módszerrel
megfejteni, hogy melyik házban is lakik a fickó.
'''


def brute_force(street_length):
    street_variations = range(1, int(m)+1)
    res = []

    for v in street_variations:
        street = range(1, v)
        for s in street:
            if sum(range(1, s)) == sum(range(s + 1, v)):
                res.append((str(v-1), str(s)))

    return res


m = input("add meg a leghosszabb utca hosszat!")
results = brute_force(m)

for r in results:
    print(r[0] + " hazbol allo utca eseten " + r[1] + ". hazszam illik az esetre")
