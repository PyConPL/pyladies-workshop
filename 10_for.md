# Rozdział 10. Pętla `for`

W tym rozdziale:

* dowiesz się czym jest **iteracja** i **pętla**,
* poznasz pętlę `for`.


## Iteracja

Kiedy operujemy na liście, bardzo często chcemy "przejść" po wszystkich
jej elementach po kolei i na każdym z nich wykonać jakąś operację.  Takie
"przejście" nazywamy **iteracją**.  W Pythonie aby otrzymać każdy element
listy po kolei możemy oczywiście użyć indeksów:

```python
>>> daty = ['15/07/2017', '16/07/2017', '17/07/2017']
>>> print(daty[0])
15/07/2017
>>> print(daty[1])
16/07/2017
>>> print(daty[2])
17/07/2017
```

Jednak takie podejście jest niewygodne kiedy lista jest bardzo długa.
A co gdy w ogóle nie wiemy na jak długiej liście działamy?  Te problemy
można rozwiązać za pomocą **pętli**, czyli instrukcji, która wykonuje
podane operacje dopóki jakiś warunek nie zostanie spełniony.  Z użyciem
pętli możemy na przykład iterować, czyli wykonywać operacje na kolejnych
elementach listy, dopóki nie dojdziemy do jej końca.

## Pętla `for`

Pętle mają wiele zastosowań, ale iteracja jest jednym z najczęściej
spotykanych.  Dlatego Python posiada pętlę `for`, która służy właśnie do
tego. Spójrzmy na taki przykład:

```python
godziny_odjazdu = ['7:30', '13:45', '16:10']
for godzina in godziny_odjazdu:
    print(godzina)
```

Przepisz do edytora powyższy kod i wykonaj go.  W oknie trybu
interaktywnego zobaczysz, że funkcja `print` została wykonana dla każdego
elementu na liście, wypisując go na ekran.  Stało się tak, ponieważ Python
przeszedł po wszystkich elementach listy `godziny_odjazdu` i dla każdego
z nich przypisał jego wartość do zmiennej `godzina` i wykonał operację
`print`.

Definicja pętli zaczyna się od słowa `for`, następnie należy podać nazwę
zmiennej, do której będą przypisywane wartości kolejnych elementów, dalej
wpisujemy słowo `in`, nazwę listy oraz dwukropek.  W kolejnych linijkach
znajdują się operacje, które zostaną wykonane dla każdego elementu.
Pamiętaj, że przed każdą operacją musi się znaleźć jednakowe wcięcie
w kodzie.  Ich szerokość nie ma znaczenia, ważne żeby były takie same.

Jeżeli pętla znajduje się wewnątrz funkcji, to wcięcie wewnątrz `for`
należy powiększyć o szerokość wcięcia funkcji:

```python
def wypisz_elementy(lista):
    for element in lista:
        print(element)
```

:snake: Napisz funkcję, która jako argument przyjmie listę liczb i wpisze
na ekran wartość każdej z nich podniesioną do kwadratu.

:snake: Napisz funkcję, który przyjmie listę stringów i zwróci nową listę,
na której znajdą się wszystkie te stringi pisane wielkimi literami
(użyj metody `upper`).


## `for` i stringi

Pętla `for` jest bardzo elastyczna: możesz jej użyć również na stringu.
W takim wypadku jej elementami będą poszczególne litery:

```python
for litera in 'ala ma kota':
    print(litera)
```

:snake: Napisz funkcję, która jako argument przyjmie string i wypisze każdą
jego literę wraz z liczbą wystąpień tej litery w stringu (użyj metody
`count`).


### Metoda `split`

Możemy również iterować po słowach.  Służy do tego metoda `split`:

```python
for slowo in 'ala ma kota'.split():
    print(slowo)
```

Tak naprawdę metoda `split` ma dużo szersze zastosowanie.  Jeżeli
podamy jej jako argument jakiś znak, wtedy string zostanie podzielony
w miejscach występowania tego znaku:

```python
>>> tekst = '2015,2016,2017'
>>> tekst.split(',')
['2015', '2016', '2017']
```

Jeżeli nie przekażemy żadnego argumentu, to string zostanie rozdzielony
w miejscach spacji:

```python
>>> 'ala ma kota'.split()
['ala', 'ma', 'kota']
```

:snake: Napisz funkcję, która jako argument przyjmuje string i wypisuje
wszystkie jego słowa, każde w osobnej linijce.


## `range`

W tym miejscu warto wspomnieć o funkcji wbudowanej `range`.  Przyjmuje
ona jako argumenty dwa integery: początek i koniec przedziału liczbowego,
który zwraca.  Możemy następnie iterować po takim przedziale i wówczas
elementami będą kolejne liczby całkowite:

```python
for liczba in range(10, 20):
    print(liczba)
```

W powyższym przykładzie wypisujemy liczby całkowite od 10 do 19.  Liczba,
którą podaliśmy jako koniec przedziału, nie jest w nim uwzględniona.

Co ciekawe, możemy podać tylko jeden argument, który wtedy jest traktowany
jako koniec przedziału, zaś za początek przyjmuje się liczbę 0.  Kolejny
przykład pokazuje jak wypisać liczby od 0 do 99:

```python
for liczba in range(100):
    print(liczba)
```

:snake: Napisz funkcję, która przyjmie jeden argument o nazwie `limit`
i zwróci listę wartości od 0 do `limit` podniesionych do kwadratu.
S

## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy pojęcia *iteracja* oraz *pętla*,
* nauczyliśmy się korzystać w pętli `for`,
* dowiedzieliśmy się, że pętla `for` działa także na stringach, oraz że
stringi posiadają metodę `split`,
* poznaliśmy funkcję wbudowaną `range`.


---

:checkered_flag: Następny rozdział: [Krotki](./11_krotki.md) :checkered_flag:
