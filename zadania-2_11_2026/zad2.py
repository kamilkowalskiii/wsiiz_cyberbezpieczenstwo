licznik = 0
liczba_p = 2
lista_l_p=[]
while(licznik < 10):
    jest_pierwsza=True

    for i in range(2,liczba_p):
        if liczba_p % i == 0:
            jest_pierwsza = False
            break

    if jest_pierwsza:
        lista_l_p.append(liczba_p)
        licznik+=1

    liczba_p+=1

print("Oto 10 pierwszych liczb pierwszych:")
print(lista_l_p)

    
