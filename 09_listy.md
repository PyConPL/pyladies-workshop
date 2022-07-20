# Rozdział 8. Listy

W tym rozdziale:

* dowiesz się czym są **listy**,
* poznasz metody `append`, `pop`, `count`, `remove` i `index`,
* poznasz funkcje wbudowane `sum`, `max`, `min` oraz `sorted`.

## Lista

Listy towarzyszą nam na co dzień.  Kiedy chcemy posłuchać muzyki,
odtwarzamy playlistę.  W sklepie spoglądamy na listę zakupów.  Szukając
czegoś w internecie, przeglądamy listę wyników.

Jeśli pomyślimy o tym dłużej, zauważymy, że w formie listy można
zaprezentować wiele innych zjawisk i rzeczy: zbiór książek w bibliotece,
wydarzenia z jakiegoś okresu, zadania do wykonania, kolejka samochodów
na stacji benzynowej itd.  Lista to w programowaniu bardzo ważne pojęcie,
bo pozwala w prosty sposób opisać zbiór obiektów, które są ułożone w jakimś
porządku: alfabetycznym, chronologicznym, losowym etc.  Listy w Pythonie
to potężne, a równocześnie proste narzędzie, którego używa się niemal na
każdym kroku.

Aby zdefiniować listę, należy wypisać obiekty (stringi, integery)
oddzielone przecinkami w nawiasach kwadratowych:

```python
>>> kolory = ['niebieski', 'czerwony', 'zielony', 'czarny']
>>> print(kolory)
['niebieski', 'czerwony', 'zielony', 'czarny']
```

W taki sposób definiujemy pustą listę:

```python
>>> lista = []
>>> print(lista)
[]
```

Możemy odwołać się do poszczególnych elementów listy wpisując jej nazwę
po czym, w nawiasach kwadratowych, numer elementu (**indeks**).  Pamiętaj,
że numeracja zaczyna się od zera!

```python
>>> print(kolory[0])
niebieski
>>> print(kolory[2])
zielony
```

Chcąc otrzymać ostatni element na liście, możemy użyć indeksu `-1`:

```python
>>> print(kolory[-1])
czarny
```

**Indeksy ujemne** to sposób na dostęp do elementów listy "od końca":

```python
>>> print(kolory[-2])
zielony
>>> print(kolory[-3])
czerwony
```

Możemy dowolnie mieszać typy elementów na liście:

```python
>>> liczby = ['jeden', 2, 'trzy', 4, 5]
```

Lista może zawierać w sobie również inne listy:

```python
>>> odcienie_czerwieni = ['karmazynowy', 'czerwony', 'bordowy']
>>> kolory = ['zielony', odcienie_czerwieni, 'niebieski']
>>> print(kolory)
['zielony', ['karmazynowy', 'czerwony', 'bordowy'], 'niebieski']
```

:snake: Napisz funkcję `element`, która przyjmuje dwa argumenty, listę oraz
numer indeksu (integer) i zwraca element listy znajdujący się pod podanym
indeksem.

:snake: Napisz funkcję `ostatni_element`, która jako argument przyjmuje
listę i zwraca jej ostatni element.  Użyj w niej funkcji `element`.


## Metody listy

Listy, podobnie jak stringi, mają wiele metod.  Poniżej
znajdziesz opis kilku najbardziej przydatnych z nich.


### `append`

Ta metoda służy do dodawania elementu do listy:

```python
>>> liczby = [1, 3]
>>> print(liczby)
[1, 3]
>>> liczby.append(5)
>>> print(liczby)
[1, 3, 5]
>>> liczby.append(7)
>>> print(liczby)
[1, 3, 5, 7]
```

:snake: Napisz funkcję, która jako argument przyjmuje listę i dodaje na
jej końcu taki sam element jaki jest na samym jej początku.


### `pop`

Metoda `pop` nie przyjmuje żadnych argumentów, a zwraca ostatni element
listy, jednocześnie usuwając go z niej:

```python
>>> litery = ['a', 'b', 'c', 'd']
>>> print(litery)
['a', 'b', 'c', 'd']
>>> litery.pop()
'd'
>>> print(litery)
['a', 'b', 'c']
>>> litery.pop()
'c'
>>> litery.pop()
'b'
>>> print(litery)
['a']
```

:snake: Napisz funkcję, która usuwa z listy dwa ostatnie elementy, po czym
dodaje do niej ten element, który na samym początku był ostatni.


### `count`

`count` przyjmuje jako argument jeden dowolny obiekt i zwraca liczbę
wystąpień tego obiektu na liście:

```python
>>> oceny = [4, 3, 3, 5, 2, 3, 5, 4, 2, 4, 5, 4, 3, 3]
>>> oceny.count(3)
5
>>> oceny.count(4)
4
>>> oceny.count(2)
2
```

### `remove`

Metoda `remove` przyjmuje jako argument dowolny obiekt i usuwa go z listy.
Jeżeli obiekt występuje na liście wielokrotnie, to tylko jego pierwsze
wystąpienie jest usuwane:

```python
>>> liczby = [10, 20, 25, 20, 10, 15]
>>> liczby.remove(20)
>>> print(liczby)
[10, 25, 20, 10, 15]
>>> liczby.remove(20)
>>> print(liczby)
[10, 25, 10, 15]
>>> liczby.remove(10)
>>> print(liczby)
[25, 10, 15]
```

:snake: Sprawdź co się stanie jeżeli spróbujemy usunąć element, którego
nie ma na liście.

:snake: Napisz funkcję, która przyjmuje dwa argumenty: listę oraz dowolny
inny obiekt.  Funkcja powinna usunąć z listy pierwsze wystąpienie tego
obiektu, a następnie dodać go na końcu listy.  Funkcja powinna zwrócić
liczbę wystąpień tego elementu na liście.


### `index`

`index` przyjmuje jeden obiekt jako argument i zwraca numer pozycji na
jakiej ten obiekt znajduje się na liście:

```python
>>> litery = ['r', 't', 'b', 'w', 'h']
>>> litery.index('t')
1
>>> litery.index('h')
4
```

:snake: Sprawdź co się stanie jeżeli spróbujemy pobrać indeks elementu,
którego nie ma na liście.


## Listy i funkcja `len`

Podobnie jak w przypadku stringów, długość listy możemy sprawdzić funkcją
wbudowaną `len` :

```python
>>> litery_nazwiska = ['K', 'o', 'w', 'a', 'l', 's', 'k', 'i']
>>> print(len(litery_nazwiska))
8
```


## Funkcje wbudowane `sum`, `min`, `max` i `sorted`

Istnieje kilka funkcji wbudowanych, które pomagają nam w pracy z listami.
Tutaj opiszemy część z nich.

Pierwsze trzy są najbardziej pomocne gdy operujemy na listach, których
wszystkie elementy są liczbami.  `sum` zwraca sumę wszystkich elementów,
`min` zwraca element o najmniejszej wartości, a `max` ten o największej
wartości:

```python
>>> pomiary = [2, 4.25, 5.30, 3]
>>> sum(pomiary)
14.55
>>> min(pomiary)
2
>>> max(pomiary)
5.3
```

:snake: Napisz funkcję, która jako argument przyjmuje listę i wypisuje na
ekran element o największej wartości oraz liczbę wystąpień tego elementu
na liście.

Kolejna funkcja to `sorted`, która przyjmuje listę, a zwraca posortowaną
kopię tej listy:

```python
>>> wyniki = [45.5, 47.2, 35.8, 41.0, 33.3]
>>> posortowane_wyniki = sorted(wyniki)
>>> print(posortowane_wyniki)
[33.3, 35.8, 41.0, 45.5, 47.2]
>>> print(wyniki)
[45.5, 47.2, 35.8, 41.0, 33.3]
```

:snake: Napisz funkcję, która jako argument przyjmie listę, posortuje ją,
a następnie zwróci jej ostatni element.  (W ten sposób otrzymamy własną
wersję funkcji `max`!)


## Wycinki list

Czasami operując na liście chcielibyśmy używać tylko jej fragmentu, np.
10 pierwszych elementów, albo elementy od drugiego do piątego.  Python
jest przygotowany na taką sytuację: umożliwia utworzenie *wycinka*
listy (ang. *slice*).  Aby stworzyć wycinek należy wpisać nazwę listy,
a następnie w nawiasach kwadratowych indeksy pierwszego i ostatniego
wycinka elementu oddzielone dwukropkiem.

Przykładowo, zwrócenie fragmentu listy od drugiego do czwartego elementu
będzie wyglądało tak:

```python
>>> lista = [1, 2, 3, 4, 5, 6, 7]
>>> lista[1:4]
[2, 3, 4]
```

Pamiętaj, że indeksy listy zaczynając się od zera, a element o indeksie
końcowym (w tym wypadku: `5`) nie zostanie dołączony do wycinka.

Możemy też pominąć indeks początkowy.  W takim wypadku Python zwróci
wszystkie elementy od początku:

```python
>>> lista[:5]
[1, 2, 3, 4, 5]
```

Jeżeli pominiemy indeks końcowy, dostaniemy wszystkie elementy do końca
listy:

```python
>>> lista[2:]
[3, 4, 5, 6, 7]
```

Jeżeli indeks końcowy będzie liczbą ujemną, to pozycja ostatniego elementu
wycinka będzie liczona od końca listy:

```python
>>> lista[:-1]
[1, 2, 3, 4, 5, 6]
>>> lista[:-2]
[1, 2, 3, 4, 5]
```

Co ciekawe, wycinki możemy tworzyć również ze stringów:

```python
>>> tekst = 'ala ma kota'
>>> tekst[2:8]
'a ma k'
```

:snake: Zobacz co się stanie, jeżeli indeks początkowy będzie liczbą
ujemną, lub jeżeli indeks końcowy będzie większy niż długość listy.


## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się czym są listy, jak je definiować i jak odnosić się
do poszczególnych elementów listy,
* poznaliśmy najważniejsze metody list,
* dowiedzieliśmy się, w jaki sposób używać na listach funkcji wbudowanych
`len`, `sum`, `max`, `min` oraz `sorted`.


---

:checkered_flag: Następny rozdział: [Pętla `for`](./10_for.md) :checkered_flag:

