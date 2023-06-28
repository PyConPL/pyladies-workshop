def imienazwisko(imie, nazwisko):
    imie_nazwisko = imie + " " + nazwisko
    return imie_nazwisko.title()

imie_nazwisko_cale = imienazwisko("magdalena", "iRLA")
print(imie_nazwisko_cale)



lista_uczestnikow = ['Kamil']
def aktualizacja_listy_uczestnikow(ls):
    ls.append("Dorota")
    return ls
aktualizacja_listy_uczestnikow(lista_uczestnikow)
print(lista_uczestnikow)


def dodaj_imie_do_listy(ls,imie):
    ls.append(imie)
    return ls

dodaj_imie_do_listy(lista_uczestnikow, "Magda")
print(lista_uczestnikow)

obecni = ["Paulina", "Karolina", "Zuza"]

for obecny in obecni:
    dodaj_imie_do_listy(lista_uczestnikow, obecny)
print(lista_uczestnikow)
