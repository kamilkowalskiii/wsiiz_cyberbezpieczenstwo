ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
for nazwa_u in ulice:
    for blok in range(1,6):
       for mieszkanie in range(1,11):
        print(nazwa_u + " " + str(blok) + "/" + str(mieszkanie))