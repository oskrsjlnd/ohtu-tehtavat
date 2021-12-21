from kps_template import KPS as default_kp

class KPSPelaajaVsPelaaja(default_kp):
    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
