def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("podaj nr wyrazu (n): "))
print(f"F({n}) = {fibonacci(n)}")