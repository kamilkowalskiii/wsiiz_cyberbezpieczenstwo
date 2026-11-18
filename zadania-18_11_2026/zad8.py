stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pulkownik",
)

ilosc_stopni = len(stopnie)
major_index = stopnie.index("Major")
pulkownik_wstepowanie = "Pulkownik" in stopnie
print(f"Ilosc stopni: {ilosc_stopni}, indeks majora: {major_index}, czy wystepuje puilkownik: {pulkownik_wstepowanie}")