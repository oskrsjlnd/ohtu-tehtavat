from kps_template import KPS as default_kps

class KPSPelaajaVsPelaaja(default_kps):
    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
