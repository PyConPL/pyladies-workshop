lista_liczb=[1,5,6,3,0,2,1.5]
def kwadraty(lista):
    for i in lista:
        print(i**2)
            
print(kwadraty(lista_liczb))

lista_stringow=["kot", "pies", "CHOMIK", "słOŃ"]
def stringi_male_litery(lista):
    nowa_lista=[]
    for i in lista:
        nowa_lista.append(i.upper())
    print(nowa_lista)

print(stringi_male_litery(lista_stringow))

def liczenie_liter(lista):
    for i in lista:
        print(i, " w ilości: ", lista.count(i))
print(liczenie_liter("Dzien dobry co slychac"))