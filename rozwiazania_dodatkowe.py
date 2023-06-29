#napisz funkcję, która przyjmuje dwa argumenty, starą i nową listę i zamienia listę imion uczestnikow na nazwiska.

imiona = ["Anna", "Dawid", "Edyta"]
nazwiska = ["Krokodyl", "Iguana", "Waran"]

def zmiana_imion_na_nazwiska(stara_lista, nowa_lista):
    limit = len(stara_lista)
    for i in range(0,limit):
        stara_lista[i]= nowa_lista[i]
    return stara_lista

print(zmiana_imion_na_nazwiska(imiona, nazwiska))


imiona2 = ["Anna", "Dawid", "Edyta"]
nazwiska2 = ["Krokodyl", "Iguana", "Waran"]
imiona_nazwiska=[]

def lacze_imie_nazwisko(lista_imion, lista_nazwisk, lista_uczestnikow):
    limit = len(lista_imion)
    for i in range(0,limit):
        lista_uczestnikow.append(lista_imion[i] + " " + lista_nazwisk[i])
    return lista_uczestnikow
print(lacze_imie_nazwisko(imiona2, nazwiska2, imiona_nazwiska))

####
sciezka_imion='/home/witch/pyladies-workshop/imiona.txt'
sciezka_nazwisk='/home/witch/pyladies-workshop/nazwiska.txt'

plik_imion = open(sciezka_imion)
plik_nazwisk = open(sciezka_nazwisk)

imiona_z_pliku=plik_imion
nazwiska_z_pliku=plik_nazwisk

#print(imiona_z_pliku)

lista_z_plikow=[]

def odczyt_z_pliku(plik1, plik2, lista):
    for linia in plik1:
        for linijka in plik2:
            lista.append(linia.replace("\n","") + " " + linijka.replace("\n",""))
    #for i in range(len(lista)):
    #    lista[i]=lista[i].replace("\n","")
    return lista
print(odczyt_z_pliku(imiona_z_pliku, nazwiska_z_pliku, lista_z_plikow))
#print(odczyt_z_pliku(imiona_z_pliku))

plik_imion1 = open(sciezka_imion)
plik_nazwisk1 = open(sciezka_nazwisk)

imiona_z_pliku1=plik_imion1
nazwiska_z_pliku1=plik_nazwisk1

lista_im=[linia_imienia.replace("\n","") for linia_imienia in imiona_z_pliku1]
lista_na=[linia_nazwiska.replace("\n","") for linia_nazwiska in nazwiska_z_pliku1]
print(lista_im)
print(lista_na)

def zmiana_imion_na_nazwiska(stara_lista, nowa_lista):
    limit = len(stara_lista)
    for i in range(0,limit):
        stara_lista[i]= nowa_lista[i]
    return stara_lista
print(zmiana_imion_na_nazwiska(lista_im, lista_na))

#użyj list comprehension zbey podniesc do kwadratu piec pierwszych liczb

kwadraty=[liczba**2 for liczba in range(1,6)]
print(kwadraty)

########################################
