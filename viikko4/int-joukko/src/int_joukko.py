class IntJoukko:
    def __init__(self):
        self.ljono = set()
        self.alkioiden_lkm = len(self.ljono)

    def kuuluu(self, var):
        if var in self.ljono:
            return True
        return False

    def lisaa(self, var):
        if not self.kuuluu(var):
            self.ljono.add(var)
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, var):
        if var in self.ljono:
            self.ljono.remove(var)
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
    def yhdiste(first, second):
        res = IntJoukko()
        res.ljono = first.ljono.union(second.ljono)
        return res

    @staticmethod
    def leikkaus(first, second):
        res = IntJoukko()
        res.ljono = first.ljono.intersection(second.ljono)
        return res

    @staticmethod
    def erotus(first, second):
        res = IntJoukko
        res.ljono = first.ljono.difference(second.ljono)
        return res

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        res = "{"
        for i in self.ljono:
            res += str(i) + ", "
        res = res[0:-2]+"}"
        return res
