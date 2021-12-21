from kps_factory import KPSTehdas

def pelinluonti():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = pelimuoto(vastaus)
        if peli is None:
            break
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        peli.pelaa()

def pelimuoto(vastaus):
    kps_tehdas = KPSTehdas()
    if vastaus.endswith("a"):
        return kps_tehdas.luo_kps_pelaaja_vs_pelaaja()
    elif vastaus.endswith("b"):
        return kps_tehdas.luo_kps_pelaaja_vs_tekoaly()
    elif vastaus.endswith("c"):
        return kps_tehdas.luo_kps_pelaaja_vs_parempi_tekoaly()
    return None