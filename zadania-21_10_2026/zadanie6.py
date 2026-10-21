import random

"""droga = float(input("podaj pokonana droge (km): "))
spalanie = float(input("podaj srednie spalanie (l/100km): "))
cena_paliwa = 6.5
zuzycie_paliwa = (droga*spalanie)/100
koszty = zuzycie_paliwa*cena_paliwa
print(f"Przewidywalne zuzycie paliwa {zuzycie_paliwa:.2f} l\nSzacowane koszty podrozy {koszty:.2f} zl")"""

##################################################################################################################

droga = random.randint(1,500)
spalanie = float(input("podaj srednie spalanie (l/100km): "))
cena_paliwa = float(input("podaj aktualna cene paliwa (zl): "))
zuzycie_paliwa = (droga*spalanie)/100
koszty = zuzycie_paliwa*cena_paliwa
print(f"Przewidywalne zuzycie paliwa {zuzycie_paliwa:.2f} l\nSzacowane koszty podrozy {koszty:.2f} zl\nPrzebyte kilometry:{droga} km")