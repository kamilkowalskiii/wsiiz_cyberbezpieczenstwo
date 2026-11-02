paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

print(paliwo)
while paliwo > 0:
    czas +=1
    paliwo = paliwo - paliwo_zużyte_na_s
    print(paliwo)
    if(paliwo==0):
        print("koniec lotu")
    

    