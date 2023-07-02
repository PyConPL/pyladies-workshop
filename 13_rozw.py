slownik_liter = {"a": 1, "b": 2, "c": 3}

def drukuje_klucze(slownik):
    for key in slownik:
        print(key)
print(drukuje_klucze(slownik_liter))


####

def drukuje_wartosci(slownik):
    for key, value in slownik.items():
        print(value)

print(drukuje_wartosci(slownik_liter))