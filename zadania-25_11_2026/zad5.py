def liczBMI(waga,wzrost):
    BMI = waga/(wzrost*wzrost)
    if BMI<18.5:
        return "niedowaga"
    elif BMI >= 18.5 and BMI<=24.9:
        return "pożądana masa ciała"
    elif BMI >= 25 and BMI<=29.9:
        return "nadwaga"
    elif BMI >= 30 and BMI<=34.9:
        return "otyłość I stopnia"
    elif BMI >= 35 and BMI<=39.9:
        return "otyłość II stopnia"
    elif BMI >= 40:
        return "otyłość III stopnia"
    


waga = int(input("podaj aktualna wage (kg): "))
wzrost = float(input("podaj wzrost (m): "))
print(liczBMI(waga,wzrost))





    