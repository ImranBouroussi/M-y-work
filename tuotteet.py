tuotteet = [
    {"id": "0001", "tuote": "Vasara", "hinta": 10, "varastosaldo": 3},
    {"id": "0002", "tuote": "Pora", "hinta": 15, "varastosaldo": 7},
    {"id": "0003", "tuote": "Saha", "hinta": 7, "varastosaldo": 10},
    {"id": "0004", "tuote": "Ruuvimeisseli", "hinta": 12, "varastosaldo": 4},
    {"id": "0005", "tuote": "Jakoavain", "hinta": 18, "varastosaldo": 6},
    {"id": "0006", "tuote": "Taltta", "hinta": 3, "varastosaldo": 9}
]

def hae_tuote(tunniste):
    for tuote in tuotteet:
        if tuote["id"] == tunniste or tuote["tuote"].lower() == tunniste.lower():
            return tuote
    return None

def nayta_varasto():
    print("\nTuotteet varastossa:")
    for tuote in tuotteet:
        print(f'{tuote["id"]} {tuote["tuote"]} {tuote["varastosaldo"]} kpl')

def lisaa_tuote():
    nimi = input("Anna uuden tuotteen nimi: ")
    while True:
        try:
            hinta = float(input(f"Anna tuotteen {nimi} hinta: "))
            varastosaldo = int(input(f"Anna tuotteen {nimi} varastosaldo: "))
            break
        except ValueError:
            print("Virheellinen syöte, yritä uudestaan.")
    uusi_id = f"{int(tuotteet[-1]['id']) + 1:04d}"
    tuotteet.append({"id": uusi_id, "tuote": nimi, "hinta": hinta, "varastosaldo": varastosaldo})

def tilaa_tuote():
    nayta_varasto()
    id = input("Anna tilattavan tuotteen id: ")
    tuote = hae_tuote(id)
    if tuote:
        while True:
            try:
                maara = int(input("Anna tilattava määrä: "))
                tuote["varastosaldo"] += maara
                break
            except ValueError:
                print("Virheellinen syöte, yritä uudestaan.")
    else:
        print("Tuotetta ei löydy!")

def kasittele_varasto():
    nayta_varasto()
    while True:
        toiminto = input("\n(p)alaa, (t)ilaa tai (l)isää: ").lower()
        if toiminto == 'p':
            break
        elif toiminto == 't':
            tilaa_tuote()
        elif toiminto == 'l':
            lisaa_tuote()
        else:
            print("Virheellinen valinta, yritä uudestaan.")

def kassa():
    ostoslista = []

    while True:
        tunniste = input("Anna myytävän tuotteen id tai nimi, 'varasto' tai 'valmis': ").lower()
        
        if tunniste == 'valmis':
            if ostoslista:
                print("\nMyydyt tuotteet:")
                yhteensa = 0
                for ostos in ostoslista:
                    summa = ostos["hinta"] * ostos["myyntimaara"]
                    yhteensa += summa
                    print(f'{ostos["tuote"]}: {ostos["myyntimaara"]} kpl, yhteensä {summa}€')
                print(f'Ostokset yhteensä: {yhteensa}€')

                while True:
                    maksu = input("\n(m)aksa tai (p)eruuta: ").lower()
                    if maksu == 'm':
                        for ostos in ostoslista:
                            tuote = hae_tuote(ostos["id"])
                            tuote["varastosaldo"] -= ostos["myyntimaara"]
                        ostoslista.clear()
                        print("Tuotteet maksettu!\n")
                        break
                    elif maksu == 'p':
                        ostoslista.clear()
                        print("Ostokset peruutettu!\n")
                        break
                    else:
                        print("Virheellinen valinta, yritä uudestaan.")
            else:
                print("Ostoslista on tyhjä.")
        
        elif tunniste == 'varasto':
            kasittele_varasto()
        
        else:
            tuote = hae_tuote(tunniste)
            if tuote:
                while True:
                    try:
                        maara = int(input("Kuinka monta myydään? "))
                        if maara <= 0:
                            print("Määrän tulee olla positiivinen luku.")
                        elif maara > tuote["varastosaldo"]:
                            print(f'Varastossa on vain {tuote["varastosaldo"]}!')
                        else:
                            ostoslista.append({
                                "id": tuote["id"],
                                "tuote": tuote["tuote"],
                                "hinta": tuote["hinta"],
                                "myyntimaara": maara
                            })
                            break
                    except ValueError:
                        print("Virheellinen syöte, syötä numero.")
            else:
                print("Tuotetta ei löydy!")

if __name__ == "__main__":
    while True:
        kassa()
