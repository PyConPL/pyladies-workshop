def pole_kola(promien):
    return 3.14*(promien**2)
print(pole_kola(2))
print(pole_kola(1))
print(pole_kola(2))

def cena_brutto(cena_netto, vat):
    return cena_netto*(100+vat)/100

print(cena_brutto(10,23))

def imie_nazwisko(imie, nazwisko):
    dane_osoby=imie +" " + nazwisko
    return dane_osoby.title()

print(imie_nazwisko("magdaLena", "iRLA"))

def lubi(imie, nazwisko, co):
    #dane_osoby_lubiacej=imie_nazwisko(imie, nazwisko)
    #opis_osoby= dane_osoby_lubiacej.title() + " lubi " + co.lower()
    opis_osoby= imie_nazwisko(imie, nazwisko) + " lubi " + co.lower()
    return opis_osoby

print (lubi("Magda", "iRLA", "książki"))

print(str(-10))
print(int(3.14))
#print(int("kotek"))
#print(int(2 kotki))
print(float(2))
#print(float(kotek))
#print(float(2 kotki))


###################################
def narodziny(rok_urodzenia):
    wiek=2017-rok_urodzenia
    print("Masz ", wiek, " lat.")
    return wiek
print(narodziny(1991))

test_formatu= "Mam {} lat i {} miesiace".format(32, 4)
print(test_formatu)