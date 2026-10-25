rok=int(input("podaj rok"))
dzien=int(input("podaj dzień w roku"))
miesiace=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    miesiace[1]=29
miesiac=1
for ilosc_dni in miesiace:
    if dzien<=ilosc_dni:
        break
    dzien -= ilosc_dni
    miesiac+=1
print(f"{dzien:02d} {miesiac:02d}")