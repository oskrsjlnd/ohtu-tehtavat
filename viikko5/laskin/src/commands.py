class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.edellinen_arvo = self.sovelluslogiikka.tulos

    def suorita(self):
        self.sovelluslogiikka.plus(self.syote)
    
    def peruuta(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)
    
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.edellinen_arvo = self.sovelluslogiikka.tulos

    def suorita(self):
        self.sovelluslogiikka.miinus(self.syote)

    def peruuta(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        self.edellinen_arvo = self.sovelluslogiikka.tulos

    def suorita(self):
        self.sovelluslogiikka.nollaa()

    def peruuta(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        if self.sovelluslogiikka.edellinen_komento == "erotus":
            Erotus.peruuta()
        elif self.sovelluslogiikka.edellinen_komento == "summa":
            Summa.peruuta()
        else:
            Nollaus.peruuta()
