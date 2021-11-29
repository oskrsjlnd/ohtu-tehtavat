from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori_hinta = 0
        self.tuotteet = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        count = 0
        for i in self.tuotteet:
            count += i.lukumaara()
        return count
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.kori_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        for i in self.tuotteet:
            if i.tuotteen_nimi() == ostos.tuotteen_nimi():
                i.muuta_lukumaaraa(1)
                self.kori_hinta += ostos.hinta()
                return

        self.tuotteet.append(ostos)
        self.kori_hinta += ostos.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for i in self.tuotteet:
            if i.tuotteen_nimi() == poistettava.nimi():
                if i.lukumaara() == 1:
                    self.tuotteet.remove(i)
                    self.kori_hinta -= poistettava.hinta()
                    return
                i.muuta_lukumaaraa(-1)
                self.kori_hinta -= poistettava.hinta()
                break

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.tuotteet
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
