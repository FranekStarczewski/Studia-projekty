a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Wynik: Równanie tożsamościowe (0=0) - nieskończenie wiele rozwiązań.")
        else:
            print(f"Wynik: Równanie sprzeczne ({c}=0) - brak rozwiązań.")
    else:
        x = -c / b
        print(f"Wynik: Równanie liniowe. Jedno rozwiązanie: x = {x}")
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        pierwiastek_delty = delta ** 0.5
        x1 = (-b - pierwiastek_delty) / (2 * a)
        x2 = (-b + pierwiastek_delty) / (2 * a)
        print("Wynik: Dwa rozwiązania rzeczywiste:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Wynik: Jedno rozwiązanie rzeczywiste (pierwiastek podwójny): x0 = {x0}")
    else:
        print("Wynik: Brak rozwiązań rzeczywistych (Delta < 0).")