def powitanie(imie="Uzytkowniku", jezyk="polski"):
    if(jezyk=="polski"):
        print("Czesc, "+imie)
    elif(jezyk=="angielski"):
        print("Hello, "+imie)
    elif(jezyk=="niemiecki"):
        print("Guten Morgen, "+imie)
    else:
        print("Witaj "+imie)

imie = input("podaj swoje imie: ")
jezyk = input("podaj swoj jezyk: ")
powitanie(imie,jezyk)
