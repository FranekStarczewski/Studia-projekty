import math
a1 = float(input("Podaj a1"))
b1 = float(input("Podaj b1"))
c1 = float(input("Podaj c1"))
a2 = float(input("Podaj a2"))
b2 = float(input("Podaj b2"))
c2 = float(input("podaj c2"))
W  = a1 * b2 - a2 * b1
Wx = c1 * b2 - c2 * b1
Wy = a1 * c2 - a2 * c1
if W != 0:
    x=Wx/W
    y=Wy/W
    print(f"Jest to układ oznaczony x={x} y={y}")
    wynik1= a1 * x + b1 * y
    wynik2= b1 * x + b2 * y
    if math.isclose(wynik1, c1) and math.isclose(wynik2, c2):
        print(f"")
elif W == 0 and Wx == 0 and Wy == 0:
    print("układ nieoznaczony")
else:
    print("układ sprzeczny")