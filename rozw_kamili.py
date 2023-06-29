# 01 Tryb
print("Uczę się")
print("Pythona! :)")
# 02 Tekst
print("count przyjmujstringu:".count("na"))
len("Kamila")
print(len([1,2]))
print(len("Kamila Kazimierska"))
# QA: Jaka jest różnica między metodą a funkcją?
class Person:
    def __init__(self, name):
        self.name = name
    def przedstaw_sie(self):
        return f"Jestem {self.name}"

person = Person("Kamila")
print(person.przedstaw_sie())

def przedstaw_sie(name):
    return f"Jestem {name}"

print(przedstaw_sie("Kamila"))
# QA: Czy mogę mieć własne metody na istniejących obiektach?
class StrPaulina(str):
    def __init__(self, name):
        self.name = name
    def str_pauliny(self):
        return f"string z nazwa {self.name}"

str_p = StrPaulina("some")
print(str_p.replace("s", "S"))
print(str_p.str_pauliny())


# 04 Liczby i funckje
# Napisz funkcję, która zsumuje trzy liczby.
def sum(dzien, miesiac, rok):
    return dzien + miesiac + rok
print(sum(28,6,2023))

# QA: Czy zmienna w funkcji jest widoczna poza funkcją?
# QA: Czy mogę argument funkcji zmienić globalnie przez działanie funkcji?
def change_name(imie):
    return "Jakub"

def get_name(imie, nazwisko):
    imie = change_name(imie)
    imie_nazwisko = imie + " " + nazwisko
    return imie_nazwisko.title()

# 06 Zmienne i funkcje
imie_nazwisko_otrzymane = get_name(imie = "kamil", nazwisko= "synoradzki")
print(imie_nazwisko_otrzymane)

new_name = change_name("Kamil")
print(new_name)

# 07 Listy
lista_uczestnikow = ['Kamil']

def zaaktualizuj_liste_uczestnikow(ls, imie):
    ls.append(imie)
    return ls

zaaktualizuj_liste_uczestnikow(lista_uczestnikow, "Dorota")


print(lista_uczestnikow)

# 10 For
uczestnicy = ["Dorota", "Kamil", "Karolina", "Magda", "Paulina"]
lista_uczestnikow = []
for uczestnik in uczestnicy:
    zaaktualizuj_liste_uczestnikow(lista_uczestnikow, uczestnik)
    # lista_uczestnikow.append(uczestnik)
print(lista_uczestnikow)

# Powtórka - zadanie
# Napisz funkcję, która przyjmuje dwa argumenty, starą i nową listę.
# która zamienia listę imion uczestników na naziwska.

lista_imion = ["Kamila","Kamil"]
lista_nazwisk = ["Kazmierska","Synoradzki"]

def zamiana_imion_na_nazwiska(lista_imion,lista_nazwisk):
    for a in range(len(lista_imion)):
        lista_imion[a]= lista_imion[a] + " " + lista_nazwisk[a]
    # lista_imion = lista_nazwisk
    return lista_imion


print("Imiona")
print(lista_imion)

nowa_lista = zamiana_imion_na_nazwiska(lista_imion,lista_nazwisk)

print("Nazwiska")
print(nowa_lista)

# Zadanie: Wczytaj imiona z pliku.
plik = open("lista_imion.txt")
dane = plik.read()
print(dane)
for linia in plik:
    x = linia
    print(x)






def wczytaj_do_listy_ze_sciezki(sciezka):
    plik_lista = open(sciezka)
    lista = [linia.replace('\n', '') for linia in plik_lista]
    return lista

wczytana_lista_imion = wczytaj_do_listy_ze_sciezki("lista_imion.txt")
wczytana_lista_nazwisk = wczytaj_do_listy_ze_sciezki("lista_nazwisk.txt")
print(wczytana_lista_imion)
print(wczytana_lista_nazwisk)

# Uzyj list comprehesion zeby podniesc do kwadratu 5 pierwszych liczb.
kwadraty = [liczba**2 for liczba in range(1,6)]
print(kwadraty)

# Funkcja, ktora dla argumentu ścieżki listy imion i listy nazwisk,
# zworci liste imion i nazwisk.

def zamien_imiona_na_nazwiska_ze_sciezki(sciezka_imion, sciezka_nazwisk):
    wczytana_lista_imion = wczytaj_do_listy_ze_sciezki(sciezka_imion)
    wczytana_lista_nazwisk = wczytaj_do_listy_ze_sciezki(sciezka_nazwisk)
    nowa_lista = zamiana_imion_na_nazwiska(wczytana_lista_imion, wczytana_lista_nazwisk)
    return nowa_lista

zamien_imiona_na_nazwiska_ze_sciezki("lista_imion.txt", "lista_nazwisk.txt")


# print(lista_ze_sciezek)