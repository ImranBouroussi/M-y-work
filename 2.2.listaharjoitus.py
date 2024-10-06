def luo_shakkilauta():
    lauta = [
        ['t', 'n', 'b', 'q', 'k', 'b', 'n', 't'],  
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'],  
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'],  
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
        ['T', 'N', 'B', 'Q', 'K', 'B', 'N', 'T'] 
    ]
    return lauta

def tulosta_shakkilauta(lauta):
    for rivi in lauta:
        print(''.join(rivi))

def muunna_koordinaatit(x, y):
    kirjain = chr(97 + y)  
    numero = 8 - x 
    return f"{kirjain}{numero}"

def etsi_nappula(lauta, nappula):
    sijainnit = []
    for x in range(8):
        for y in range(8):
            if lauta[x][y] == nappula:
                sijainnit.append(muunna_koordinaatit(x, y))
    return sijainnit

def main():
    lauta = luo_shakkilauta()
    tulosta_shakkilauta(lauta)
    
    nappula = input("\nMitä nappulaa haluat etsiä: ")
    sijainnit = etsi_nappula(lauta, nappula)
    
    if sijainnit:
        print(', '.join(sijainnit))
    else:
        print(f"{nappula} ei ole nappula!")

if __name__ == "__main__":
    main()
