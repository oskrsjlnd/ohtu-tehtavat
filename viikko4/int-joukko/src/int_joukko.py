class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.ljono = set()
        self.alkioiden_lkm = len(self.ljono)

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono.add(n)
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = []
        for i in self.ljono:
            taulu.append(i)
        return taulu

    @staticmethod
    def yhdiste(a, b):
        res = IntJoukko()
        res.ljono = a.ljono.union(b.ljono)
        return res

    @staticmethod
    def leikkaus(a, b):
        res = IntJoukko()
        res.ljono = a.ljono.intersection(b.ljono)
        return res

    @staticmethod
    def erotus(a, b):
        res = IntJoukko
        res.ljono = a.ljono.difference(b.ljono)
        return res

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        res = "{"
        for i in self.ljono:
            res += str(i) + ", "
        res = res[0:-2]+"}" 
        return res
