# Rozdział 16. Biblioteka standardowa

W tym rozdziale:

* dowiesz się czym jest **biblioteka standardowa**,
* poznasz najważniejsze **moduły** biblioteki standardowej.


## Biblioteka

W programowaniu posługujemy się pojęciem **biblioteka**, które oznacza
zbiór programów i narzędzi do ich budowania, które możemy wykorzystać
pisząc własne programy.  Przykładem biblioteki może być zbiór funkcji
matematycznych (np. trygonometrycznych), do których możemy odwołać się
w naszym kodzie zamiast definiować je samodzielnie.


## Moduły

W Pythonie biblioteki programistyczne są dostępne poprzez **moduły**.
Moduł to po prostu kod umieszczony na dysku, w miejscu w którym
Python może go odnaleźć.  Może to być kod napisany w Pythonie, ale
są sposoby na pisanie modułów w innych językach programowania.  Python
znajdzie taki kod jeżeli zostanie on umieszczony w jednym z określonych
z góry katalogów.

Każdy może napisać własny moduł do Pythona.  W internecie znajdziemy
tysiące modułów, które różne osoby i firmy udostępniają.  Możemy je pobrać
i używać ich do pisania programów.  Możemy też tworzyć własne moduły
i dzielić się nimi z innymi użytkownikami.

Aby skorzystać z modułu w kodzie naszego programu musimy **zaimportować**
jego nazwę.  Robimy to instrukcją `import`.  Gdy moduł jest już
zaimportowany, możemy używać funkcji i zmiennych, które zostały w nim
zdefiniowane.  Robimy to wpisując nazwę modułu, a następnie, po kropce,
nazwę obiektu.

W poniższym przykładzie importujemy moduł o nazwie `math` i wywołujemy
funkcję `sqrt`, która zwraca pierwiastek kwadratowy z podanej liczby:

```python
import math
print(math.sqrt(9))
```

## Biblioteka standardowa Pythona

Poza modułami, które użytkownicy sami mogą pisać, istnieje zbiór modułów,
który zawsze jest dostępny w Pythonie. Ten zbiór nazywamy **biblioteką
standardową**.  Znajdziemy w nim dziesiątki modułów, a w nich narzędzia
do komunikacji sieciowej, obsługi różnych formatów plików, obliczeń
matematycznych etc.

Biblioteka standardowa jest obszernie udokumentowana na [oficjalnej
stronie Pythona](https://docs.python.org/3/library/index.html).


## Najważniejsze moduły

Omówienie całej biblioteki standardowej to zadanie na co najmniej kilka
tygodni, dlatego podczas tych warsztatów wspomnimy tylko o kilku
najbardziej popularnych modułach.


### [`math`](https://docs.python.org/3/library/math.html)

Moduł `math` zawiera kilkadziesiąt funkcji matematycznych, które mogą
okazać się pomocne przy prostych obliczeniach.  Poniżej opisaliśmy kilka
z nich.

Funkcje `ceil` i `floor` zwracają wartości zaokrąglone odpowiednio
w dół i w górę:

```python
>>> math.ceil(3.5)
4
>>> math.floor(3.5)
3
```

Funkcja `sqrt` zwraca pierwiastek kwadratowy z danej liczby:

```python
>>> math.sqrt(25)
5.0
```

`pi` oraz `e` reprezentują wartości stałych matematycznych:

```python
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
```

:snake: Napisz funkcję, która zwróci wartość pola powierzchni koła
o zadanym promieniu (według wzoru `PI * r^2`, gdzie `r` to promień).


### [`datetime`](https://docs.python.org/3/library/datetime.html)

Moduł `datetime` to podstawowe narzędzie do pracy z datami i czasem.
Zawiera obiekty `date`, `datetime` oraz `timedelta`, które reprezentują
odpowiednio datę, datę i czas oraz różnicę w czasie.

Aby otrzymać dzisiejszą datę należy wywołać metodę `today` na obiekcie
`date`:

```python
>>> datetime.date.today()
datetime.date(2017, 8, 13)
```

Otrzymany w ten sposób obiekt zawiera trzy **atrybuty**: `year`, `month`
oraz `day`, czyli odpowiednio rok, miesiąc i dzień.

```python
>>> dzisiaj = datetime.date.today()
>>> dzisiaj.year
2017
>>> dzisiaj.month
8
>>> dzisiaj.day
13
```

Metoda `now` na obiekcie `datetime` zwróci nam datę i godzinę, którą mamy
w tej chwili.  Poza atrybutami `year`, `month` oraz `day` posiada także
`hour`, `minute`, `second` i `microsecond`, czyli godzinę, minutę, sekundę
i mikrosekundę.

```python
>>> teraz = datetime.datetime.now()
>>> teraz
datetime.datetime(2017, 8, 13, 18, 53, 13, 366193)
>>> teraz.hour
18
>>> teraz.minute
53
>>> teraz.second
13
>>> teraz.microsecond
366193
```

Oba typy obiektów możemy wypisać na ekran w czytelnym formacie:

```python
>>> print(dzisiaj)
2017-08-13
>>> print(teraz)
2017-08-13 18:53:13.366193
```

Chcąc utworzyć reprezentację dowolnego momentu w czasie, wystarczy
wywołać `date` lub `datetime` i podać kolejno `year`, `month`, `day`,
`hour`, `minute`, `second`, `microsecond`:

```python
>>> print(datetime.date(2010, 5, 10))
2010-05-10
>>> print(datetime.datetime(2020, 11, 23, 15, 7, 30))
2020-11-23 15:07:30
```

:snake: Zobacz co się stanie jeżeli spróbujesz utworzyć obiekt `date`
z miesiącem spoza zakresu od 1 do 12 lub datę, która nie istnieje, np.
31 kwietnia.

:snake: Zobacz co się stanie jeżeli spróbujesz utworzyć obiekt `datetime`
z godziną, minutą lub sekundą o wartości spoza dopuszczalnego zakresu
(np. godzina 26).

Jeżeli chcemy zobaczyć różnicę w czasie między dwoma obiektami typu
`datetime`, możemy je po prostu odjąć od siebie:

```python
>>> a = datetime.datetime(2017, 8, 16, 17, 00)
>>> b = datetime.datetime(2017, 8, 16, 19, 00)
>>> roznica = b - a
>>> roznica
datetime.timedelta(0, 7200)
>>> roznica.seconds
7200
```

W powyższym przykładzie otrzymaliśmy obiekt `timedelta`, który posiada
atrybut `seconds` o wartości równej liczbie sekund pomiędzy `a` i `b`.

Jeżeli różnica jest większa niż jedna doba, to zostanie ona podzielona
na dwie wartości: `seconds` i `days`, czyli sekundy i dni.

```python
>>> c = datetime.datetime(2017, 8, 16, 17, 00)
>>> d = datetime.datetime(2017, 8, 18, 15, 00)
>>> roznica = d - c
>>> roznica.seconds
79200
>>> roznica.days
1
```

Jeżeli do daty `c` dodamy jeden dzień i 79200 sekund, to otrzymamy `d`.

:snake: Napisz funkcję, która przyjmuje dwie daty jako argumenty.
Jeżeli druga data jest mniejsza od pierwszej, funkcja powinna zwrócić
`None`.  W przeciwnym wypadku funkcja powinna zwrócić liczbę sekund
dzielącą obie daty.  Zwróć uwagę, że różnica może być większa niż jedna
doba.  W takim wypadku liczbę dni należy zamienić na sekundy.


### [`random`](https://docs.python.org/3/library/random.html)

Moduł `random` służy do wykonywania operacji, których wynik jest losowy:
generowania liczb losowych, losowego wybierania obiektów z danego zakresu,
itd.

Funkcja `randint` przyjmuje dwa integery jako argumenty i zwraca losowo
wybraną liczbę całkowitą, której wartość znajduje się pomiędzy argumentami.

```python
>>> random.randint(1, 100)
9
>>> random.randint(1, 100)
44
```

Funkcja `choice` przyjmuje jako argument dowolną sekwencję (listę, krotkę,
string) i zwraca losowo wybrany element:

```python
>>> random.choice('ala ma kota')
'm'
>>> random.choice([9, 7, 5, 3])
7
>>> random.choice(('pycon', 'pl', '2017'))
'pl'
```

:snake: Napisz funkcję, która przyjmie jako argument dowolną sekwencję
i zwróci *krotkę* z trzema losowo wybranymi z niej elementami.


### [`json`](https://docs.python.org/3/library/json.html)

Moduł `json` pozwala zapisywać obiekty Pythona (słowniki i listy) jako
string w formacie JSON (*JavaScript Object Notation*), który jest
powszechnie używany np. w serwisach internetowych do wymiany danych między
przeglądarką a serwerem.

Żeby zapisać obiekt do stringa należy wywołać funkcję `dumps`:

```python
>>> json.dumps({'miejsce': 'Ossa', 'data': '2017-08-16'})
'{"miejsce": "Ossa", "data": "2017-08-16"}'
>>> json.dumps([2017, 8, 16])
'[2017, 8, 16]'
```

Do zamiany stringa na słownik lub listę służy funkcja `loads`:

```python
>>> json.loads('{"miejsce": "Ossa", "data": "2017-08-16"}')
{'miejsce': 'Ossa', 'data': '2017-08-16'}
>>> json.loads('[2017, 8, 16]')
[2017, 8, 16]
```

## Co dalej?

Wyżej wymieniliśmy tylko kilka najbardziej popularnych modułów, więc
zachęcamy do zapoznania się z resztą biblioteki standardowej.  Warto
zacząć od oficjalnej dokumentacji, ale w internecie znajdziemy mnóstwo
artykułów poświęconych stosowaniu biblioteki standardowej na co dzień.
Oczywiście nie trzeba znać jej w całości żeby swobodnie programować
w Pythonie.  Wiele z tych modułów ma bardzo specyficzne zastosowania
i większość programistów nigdy z nich nie korzysta.  Warto natomiast
pamiętać, że jeżeli trafisz na jakiś nowy problem, to dobrze jest najpierw
przejrzeć bibliotekę standardową w poszukiwaniu modułu, który może okazać
się pomocny.


## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się czym jest **biblioteka standardowa** i jak z niej
korzystać,
* poznaliśmy moduły `math`, `datetime`, `random` i `json`.


---

:checkered_flag: Następny rozdział: [Podsumowanie](./17_podsumowanie.md) :checkered_flag:

