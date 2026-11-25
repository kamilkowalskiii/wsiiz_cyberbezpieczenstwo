import math


def oblicz_pole_trójkąta():
  try:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    if a <= 0 or b <= 0 or c <= 0:
      print("dlugosci musza byc wieksze od 0")
      return 
 
    s = (a + b + c) / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"pole trojkata wynosi: {pole:.2f}")

  except ValueError:
    print(
        "\n wprowadzono zle dane popraw je "
    )




oblicz_pole_trójkąta()