def element(lista, indeks):
    return lista[indeks]
mojalista=[0,1,2,"kot",10, "koliber"]
print(element(mojalista,3))

def ostatni_element(lista):
    return lista[-1]

print(ostatni_element(mojalista))

def dodawanie_do_funkcji(lista):
    lista.append(lista[0])
    return lista
print(dodawanie_do_funkcji(mojalista))
print(mojalista)

lista2=["kot", "pies", 666, "krokodyl", 0, 990, "kot"]
print(lista2)
def usuwanie_2_ostatnich(lista):
    ostatni=lista.pop()
    lista.pop()
    lista.append(ostatni)
    return lista

print(usuwanie_2_ostatnich(lista2))

#print(mojalista.pop())

#lista2.remove(10)

def usuwanie_elementu(lista, obiekt):
    lista.remove(obiekt)
    lista.append(obiekt)
    return lista
print(usuwanie_elementu(lista2, "kot"))

print(lista2.index(0))

lista_do_sortowania=[99, 4, 9, 100, 24, 5]
def sortowanie_listy(lista):
    posortowana=sorted(lista_do_sortowania)
    return posortowana[-1]
print(sortowanie_listy(lista_do_sortowania))

print(lista_do_sortowania[-3:8])