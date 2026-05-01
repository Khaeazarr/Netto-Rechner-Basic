def berechne_einkommensteuer(jahres_brutto):
    grundfreibetrag = 11604  # Steuerfrei
    
    if jahres_brutto <= grundfreibetrag:
        return 0
    elif jahres_brutto <= 66760:
        # Eingangssteuersatz bis mittleres Einkommen (ca. 14% bis 42%)
        steuerbare_summe = jahres_brutto - grundfreibetrag
        return steuerbare_summe * 0.25 
    else:
        # Hoher Steuersatz für Besserverdiener
        steuerbare_summe = jahres_brutto - grundfreibetrag
        return steuerbare_summe * 0.42

print("--- Professioneller Gehaltsrechner (Simulation) ---")
monats_brutto = float(input("Dein monatliches Bruttogehalt in Euro: "))
jahres_brutto = monats_brutto * 12

# Sozialabgaben (Rente, Krankenversicherung etc.) ca. 20%
sozialabgaben = jahres_brutto * 0.20
einkommensteuer = berechne_einkommensteuer(jahres_brutto)

jahres_netto = jahres_brutto - sozialabgaben - einkommensteuer
monats_netto = jahres_netto / 12

print(f"\nERGEBNIS FÜR {monats_brutto}€ PRO MONAT:")
print(f"Jahresbrutto: {jahres_brutto:.2f}€")
print(f"Abzüge Sozialversicherung: {sozialabgaben:.2f}€")
print(f"Abzüge Einkommensteuer: {einkommensteuer:.2f}€")
print("-" * 30)
print(f"Dein monatliches NETTO: {monats_netto:.2f}€")
