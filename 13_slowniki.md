# Rozdział 13. Słowniki

W tym rozdziale:

* dowiesz się czym jest **słownik**, **klucz** oraz **wartość**,
* nauczysz się definiować słowniki oraz wykonywać na nich operacje,
* poznasz najczęściej spotykane zastosowania słowników.


## Czym jest słownik

Wiele sytuacji z jakimi spotkasz się pisząc programy będzie można opisać
jako zbiór kluczy i wartości im odpowiadających.  Przykładem z codziennego
życia jest encyklopedia, gdzie kluczami są różne hasła, a wartościami
są definicje tłumaczące te hasła.  Można pójść dalej i powiedzieć, że
internet to zbiór adresów (np. `pl.pycon.org`) oraz stron WWW, które się
pod nimi kryją.

Takie spojrzenie na otaczającą nas rzeczywistość jest bardzo wygodne,
bo pozwala opisać złożone zjawiska w systematyczny, łatwy do zrozumienia
sposób.  Dlatego też wiele języków programowania oferuje narzędzia do
tworzenia tego typu struktur danych.  W przypadku Pythona
są to **słowniki**.

Słownik (*dictionary*, w skrócie *dict*), to zbiór **kluczy** oraz
odpowiadających im **wartości**.  Nazwa "słownik" nie jest przypadkowa,
nawiązuje do formuły w której zbiorowi słów przypisujemy ich definicje.


## Definicja słownika

Słownik definiujemy poprzez wypisanie par klucz-wartość, oddzielonych
przecinkami, ujmując całość w nawiasy klamrowe.  Każda para to dwie
wartości oddzielone dwukropkiem.

```python
wiek = {'Marcin': 23, 'Agata': 17, 'Marta': 46}
```

Aby stworzyć pusty słownik wystarczą puste nawiasy klamrowe:

```python
d = {}
```

Wartości w słowniku nie muszą być tego samego typu, jedna może być liczbą,
kolejna stringiem itd.:

```python
d = {'liczba': 123, 'inna liczba': 12.34, 'lista': ['Ala ma kota']}
```

Klucze mogą być również liczbami:

```python
d = {15: 'Ala ma kota', 'Kot ma alę': 3.14}
```

Słownik może też być elementem listy:

```python
l = [{'a': 1, 'b': 2}, 3, 4]
```

Kiedy wypiszemy słownik na ekran, zobaczymy całą jego zawartość:

```python
>>> d = {'a': ['x', 9, 'z'], 'b': 2, 'c': 'Ala ma kota'}
>>> print(d)
{'a': ['x', 9, 'z'], 'b': 2, 'c': 'Ala ma kota'}
```


## Operacje na słownikach

Kiedy zdefiniujemy słownik, możemy na nim wykonać szereg operacji.


### Pobieranie wartości elementu

Aby otrzymać wartość dla danego klucza należy wpisać nazwę słownika,
a następnie, w nawiasach kwadratowych, nazwę klucza:

```python
>>> d = {'a': 1, 'b': 2}
>>> print(d['a'])
1
>>> print(d['a'] + d['b'])
3
```

:snake: Zobacz co się stanie jeżeli pobierzesz wartość dla klucza, który
nie istnieje w słowniku.

:snake: Napisz funkcję, która przyjmie dwa argumenty, listę słowników
oraz klucz i zwróci listę wartości znajdujących się pod tym kluczem
z każdego słownika na liście.


### Definiowanie elementu

W każdej chwili możemy zdefiniować wartość klucza w słowniku.  Żeby to
zrobić należy odwołać się do danego klucza i przypisać do niego wartość:

```python
>>> d = {'a': 1}
>>> d['b'] = 2
>>> d[5] = ['lista', 'elementów']
>>> print(d)
{'a': 1, 'b': 2, 5: ['lista', 'elementów']}
>>> print(d[5])
['lista', 'elementów']
```

Jeżeli dany klucz już istnieje, jego wartość zostanie nadpisana:

```python
>>> d = {'a': 1}
>>> print(d['a'])
1
>>> d['a'] = 2
>>> print(d['a'])
2
```


### Usuwanie elementu

Możemy usunąć dowolny klucz słownika posługując się instrukcją `del`:

```python
>>> d = {'a': 1, 'b': 2}
>>> del d['a']
>>> print(d)
{'b': 2}
```

:snake: Zobacz co się stanie jeżeli spróbujesz usunąć klucz, który nie
istnieje w słowniku.


### Iterowanie po kluczach i wartościach

W jednym z poprzednich rozdziałów mówiliśmy o iteracji w kontekście listy,
czyli o "przechodzeniu" po jej elementach.  Używaliśmy w tym celu pętli
`for`.  Jeżeli wykonamy tę samą operację na słowniku, to przejdziemy po
jego kluczach:

```python
for klucz in slownik:
    print(klucz)
```

:snake: Napisz funkcję, która przyjmuje jako argument słownik i przechodzi
po jego kluczach, wypisując każdy z nich.

W podobny sposób możemy iterować po samych wartościach słownika.  Służy
do tego metoda `values`:

```python
lista_startowa = {1: 'Puchatek', 2: 'Prosiaczek', 3: 'Tygrysek'}
for zawodnik in lista_startowa.values():
    print(zawodnik)
```

:snake: Napisz funkcję, która przyjmuje jako argument słownik i zwraca
sumę wszystkich wartości słownika.  Zakładamy, że wartości zawsze są
liczbami.

Słownik posiada również metodę `items`, dzięki której możemy iterować
jednocześnie po kluczach i wartościach słownika:

```python
lista_startowa = {1: 'Puchatek', 2: 'Prosiaczek', 3: 'Tygrysek'}
for numer_startowy, zawodnik in lista_startowa.items():
    print(numer_startowy, ':', zawodnik)
```

Zwróć uwagę, że tym razem w pętli `for` zdefiniowaliśmy dwie zmienne:
`numer_startowy` i `zawodnik`.  Nie jest to nic specyficznego dla słownika,
ale kolejna właściwość tej pętli.  Jeżeli pętla przechodzi po liście,
której wszystkie elementy są sekwencjami (czyli listami lub krotkami),
to możemy od razu **rozpakować** wszystkie elementy tych sekwencji do
zmiennych:

```python
lista = [['a', 'Arbuz', 'Anglia'], ['b', 'Banan', 'Brazylia']]
for litera, owoc, panstwo in lista:
    print(owoc)
```

Wracając do słowników, w naszym przypadku pierwszym elementem każdej
sekwencji jest klucz, a drugim wartość dla tego klucza.

:snake: Napisz funkcję, która przyjmie dwa argumenty, słownik oraz wartość
i zwróci nazwę klucza, którego wartość jest równa wartości z argumentu.


## Zagnieżdżanie słowników

Wartością w słowniku może być dowolny obiekt, również inny słownik.
Dzięki temu możemy w prosty sposób tworzyć złożone struktury danych:

```python
>>> auto = {}
>>> auto['kolor'] = 'czerwony'
>>> auto['silnik'] = {'pojemność': 1600, 'moc': 130}
>>> print(auto)
{'kolor': 'czerwony', 'silnik': {'pojemność': 1600, 'moc': 130}}
```


## "Długość" słownika

Kiedy po raz pierwszy wspomnieliśmy o funkcji `len`, powiedzieliśmy, że
służy ona do sprawdzania długości obiektów.  Każdy typ obiektu (string,
lista, etc.) może inaczej rozumieć pojęcie długości.  W przypadku stringów
chodzi o liczbę znaków, w przypadku list o liczbę elementów itd.
Słowniki również mają swoją "długość": jest ona równa liczbie kluczy.

```python
>>> print(auto)
{'kolor': 'czerwony', 'silnik': {'pojemność': 1600, 'moc': 130}}
>>> len(auto)
2
```


## Do czego możemy wykorzystać słowniki

Słownik jest bardzo uniwersalną strukturą danych, przez co ma wiele
zastosowań:

* reprezentacja obiektów i ich atrybutów (jak w powyższym przykładzie),
* mapowanie jednych wartości na inne (jak w prawdziwym słowniku, gdzie
mapujemy słowa z jednego języka na drugi),
* przechowywanie wielu powiązanych ze sobą wartości w jednym miejscu
(np. klucze to tytuły filmów, a wartości to ich reżyserowie).

:snake: Wybierz jedno z powyższych zastosowań słownika.  Napisz funkcję
`ustaw`, która przyjmuje trzy argumenty, słownik, klucz oraz wartość i
ustawia w słowniku daną wartość pod danym kluczem.  Napisz funkcję
`pobierz`, która przyjmuje dwa argumenty, słownik oraz klucz i zwraca
wartość słownika pod danym kluczem.  Stosując te funkcje wypełnij słownik
danymi adekwatnymi dla wybranego zastosowania i pobierz te dane.


## :pushpin: Podsumowanie

W tym rozdziale:

* nauczyliśmy się tworzyć słowniki i wykonywać na nich operacje, między
innymi iterowanie,
* dowiedzieliśmy się, że funkcja `len` zwraca liczbę kluczy w słowniku,
* poznaliśmy najczęściej spotykane zastosowania słowników.


---

:checkered_flag: Następny rozdział: [`None`](./14_none.md) :checkered_flag:

