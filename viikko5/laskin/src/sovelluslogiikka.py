class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_komento = None

    def miinus(self, arvo):
        self.edellinen_komento = "erotus"
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen_komento = "summa"
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edellinen_komento = "nollaus"
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
