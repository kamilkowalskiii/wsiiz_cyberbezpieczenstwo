def potega(a, n):
  if n == 0:
    return 1
  elif n < 0:
    return 1 / potega(a, -n)
  else:
    return a * potega(a, n - 1)


try:
  a = float(input("podaj podstawe (a): "))
  n = int(input("podaj wykladnik (n): "))
  print(f"wynik: {potega(a, n)}")
except ValueError:
  print("podaj poprawne liczby!")
except ZeroDivisionError:
  print("nie mozna dzielic przez 0")