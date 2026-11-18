imie = str(input("podaj imie: "))
nazwisko = str(input("podaj nazwisko: "))
wiek = int(input("podaj wiek: "))
print(f"witaj {imie} {nazwisko} Twoj wiek to: {wiek}")

print(imie[0]+nazwisko[0])#INICJALY

lancuch1 = input("podaj tekst do powtorzenia: ")
print(lancuch1 * 5)#wyswietlanie 5 razy

lancuch1_1 = input("podaj tekst do powtorzenia: ")
lancuch1_2 = input("podaj tekst do powtorzenia: ")
lancuch1_3 = lancuch1_1+lancuch1_2
print(lancuch1_3)#wyswietlanie polaczonego lancucha

lancuch2_1 = input("podaj tekst do powtorzenia: ")
lancuch2_2 = input("podaj tekst do powtorzenia: ")
polowa_pierwszego = lancuch2_1[: len(lancuch2_1) // 2]
polowa_drugiego = lancuch2_2[len(lancuch2_2) // 2 :]
koncowy = polowa_pierwszego + polowa_drugiego
print(koncowy)#poloweczki