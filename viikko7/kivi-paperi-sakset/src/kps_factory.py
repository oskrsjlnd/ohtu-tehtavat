from oliot.kps_parempi_tekoaly import KPSParempiTekoaly
from oliot.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from oliot.kps_tekoaly import KPSTekoaly

class KPSTehdas:

    @staticmethod
    def luo_kps_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def luo_kps_pelaaja_vs_tekoaly():
        return KPSTekoaly()
    
    @staticmethod
    def luo_kps_pelaaja_vs_parempi_tekoaly():
        return KPSParempiTekoaly()