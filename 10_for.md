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
można rozwiązać przy pomocy **pętli**, czyli instrukcji, która wykonuje
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
Pamiętaj, że przed każdą operacją musi się znaleźć jednakowe wciącie
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


## Metoda `split`

String posiada metodę `split`, która rodziela go w miejscach wystąpienia
danego znaku i zwraca listę stringów, które powstały w ten sposób:

```python
>>> s = '2015,2016,2017'
>>> s.split(',')
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


## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy pojęcia *iteracja* oraz *pętla*,
* nauczyliśmy się korzystać w pętli `for`,
* dowiedzieliśmy się, że pętla `for` działa także na stringach, oraz że
stringi posiadają metodę `split`.


---

:checkered_flag: Następny rozdział: [Prawda i fałsz](./11_prawda_i_falsz.md) :checkered_flag:
