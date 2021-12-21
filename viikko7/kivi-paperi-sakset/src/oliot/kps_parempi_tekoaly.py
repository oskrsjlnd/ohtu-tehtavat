from kps_template import KPS as default_kps
from tekoalyt.tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(default_kps):
    def __init__(self) -> None:
        self._tekoaly_parannettu = TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly_parannettu.anna_siirto()
        self._tekoaly_parannettu.aseta_siirto(ekan_siirto)
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
