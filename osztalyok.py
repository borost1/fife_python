class Haziallat:
    def __init__(self, nev, szuletesi_ido, szin):
        self.nev = nev
        self.szuletesi_ido = szuletesi_ido
        self.szin = szin

    labak_szama = 4


class Cica(Haziallat):
    def hang(self):
        print(f"{self.nev} mondja: miau!")


class Kutya(Haziallat):
    def hang(self):
        print("vau")


class Boci(Haziallat):
    def hang(self):
        print("múúú")


class Lovacska(Haziallat):
    def hang(self):
        print("nyihaha")


class Tyuk(Haziallat):
    def hang(self):
        print("kotkodács")
    labak_szama = 2


class Kacsa(Haziallat):
    def hang(self):
        print("háp")
    labak_szama = 2


mici = Cica("Mici", "2020.02.20", "cirmos")
print(mici.labak_szama)
mici.hang()

bodri = Kutya("Bodri", "2020.02.20", "cirmos")
print(bodri.labak_szama)
bodri.hang()

tyuk = Tyuk("Tyúk", "2020.02.21", "barna")
print(tyuk.labak_szama)
tyuk.hang()