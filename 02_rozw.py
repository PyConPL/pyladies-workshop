print("Magdalena Irla, Zabrze, Babel")
mstring="Testowy string DO PRINTA"

print(mstring.lower())
print(mstring.upper())
print(mstring.title())

mystring="""Zwróć uwagę, że litera `a` jest na pozycji `0`, więc litera `r` tak
naprawdę jest nie dwudziestą trzecią, ale dwudziestą czwartą literą
alfabetu.  Ten przykład pokazuje jak ważne jest poprawne interpretowanie
informacji zwracanych przez programy.
"""
print(mystring.find("ale"))

print(mystring.replace(" ", "@"))
print(mystring.count("i"))
print(mystring.count("string"))
print(mystring.count("na"))

print(len(mystring))
print(len(''))
print(len("Magdalena Irla"))