def wyswietl_wartosci(*args):
  for arg in args:
    print(arg)

def zwroc_maksimum(*args):
  if not args:
    return None
  return max(args)



print("ZADANIE A: ")
wyswietl_wartosci(10, "kot", 3.14, "Python")

print("ZADANIE B: ")
wynik = zwroc_maksimum(55, 122, 919, -31, 42)
print("NW to:", wynik)
