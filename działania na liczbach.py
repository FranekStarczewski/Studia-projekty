a=int(input("Podaj a"))
b=int(input("Podaj b"))
print("suma", a+b)
print("różnica", a - b)
print("iloczyn", a * b)
print("suma bitowa", a | b)
print("iloczyn bitowy:", a & b)
print("różnica symetrycnza", a ^ b)
if b>=0:
    print("przesunięcie bitowe w lewwo", a << b)
else:
    print("aby przesunąć w kewo b>=0")
if b !=0:
    print("dzielenie z resztą", divmod(a,b))
else:
    print("nie można dzielić przez zero")