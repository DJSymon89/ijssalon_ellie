def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

# Test de functie met de gegeven argumenten
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

# Test de functie met de gegeven argumenten
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))