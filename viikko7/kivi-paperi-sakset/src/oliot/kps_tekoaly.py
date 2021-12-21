from kps_template import KPS as default_kp
from tekoalyt.tekoaly import Tekoaly

class KPSTekoaly(default_kp):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        return tokan_siirto
