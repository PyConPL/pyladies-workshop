try:
    liczba=int(input("podaj liczbe: "))
    print("twoja licza to " + liczba)
except ValueError:
    print("podaj liczbę całkowitą")