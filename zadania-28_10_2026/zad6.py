x = str(input("podaj jedna litere: "))
if len(x)==1 and x.isalpha():
    if x.isupper():
        print("duza litera")
    else:
        print("mala litera")
else:
    print("nie wpisales jeden litery!")