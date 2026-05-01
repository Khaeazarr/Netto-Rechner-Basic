print("Basis Brutto-Netto Rechner")

brutto = float(input("Gib dein monatliches Bruttogehalt ein (Euro): "))

# (approx 35%)
abzuege = brutto * 0.35
netto = brutto - abzuege

print(f"Dein Brutto: {brutto}€")
print(f"Geschätzte Abzüge (35%): {abzuege}€")
print(f"Dein geschätztes Netto: {netto}€")
