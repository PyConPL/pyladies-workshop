# Rozdział 14. `None`

W tym rozdziale:

* dowiesz się czym jest **`None`**.


## `None`

W Pythonie istnieje jedna szczególna wartość, która nie reprezentuje
żadnego dotąd poznanego typu: **`None`**.  Nie jest to liczba, string, ani
nic innego co poznasz ucząc się tego języka.  `None` to unikalna wartość,
która reprezentuje osobny typ.  Powstała po to, żeby programista mógł
zdefiniować "nic".  Po co?  Okazuje się, że są sytuacje, w których chcesz
wprost zaznaczyć, że dana operacja nie zwróciła żadnej istotnej informacji.
W takich sytuacjach możesz użyć wartości `None`. Zwróć uwagę, że sam fakt
posłużenia się tą wartością jest na tyle wyjątkowy, że sugeruje, że
zaistniały jakieś szczególne okoliczności.

Przykładem użycia `None` może być dzielenie przez 0.  Jak wiemy, taka
operacja matematyczna jest niedozwolona.  Teraz wyobraźmy sobie, że piszemy
funkcję, która przyjmuje jako argumenty dwie liczby i zwraca wynik
dzielenia jednej przez drugą.

```python
def podziel(dzielna, dzielnik):
    return dzielna / dzielnik
```

Co się stanie gdy argument `dzielnik` będzie równy `0`?  Otrzymamy błąd:

```python
>>> podziel(3, 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in podziel
ZeroDivisionError: division by zero
```

Aby temu zapobiec, możemy przed wykonaniem dzielenia sprawdzić wartość
argumentu i w razie potrzeby zwrócić `None`, sygnalizując, że nie możemy
obliczyć wyniku:

```python
def podziel(dzielna, dzielnik):
    if dzielnik == 0:
        return None
    return dzielna / dzielnik
```

Teraz z łatwością możemy rozpoznać kiedy funkcja napotkała niestandardowe
wywołanie:

```python
>>> wynik = podziel(4, 2)
>>> print(wynik)
2.0
>>> wynik = podziel(5, 0)
>>> print(wynik)
None
```


## Domyślna wartość funkcji

Napiszmy prostą funkcję, która przyjmuje argument i wypisuje go na ekran:

```python
def wypisz(obiekt):
    print(obiekt)
```

Wywołanie funkcji spowoduje oczekiwane skutki:

```python
>>> wypisz(123)
123
>>> wypisz('ala ma kota')
ala ma kota
```

Widzimy, że ciało funkcji zostało wykonane, jednak jaka wartość została
zwrócona?  Innymi słowy: co się dzieje, jeżeli nie użyjemy instrukcji
`return`?  Odpowiedź brzmi: funkcja zwróci `None`.

```python
>>> rezultat = wypisz('abc')
abc
>>> print(rezultat)
None
```

Tak samo dzieje się, jeżeli użyjemy instrukcji `return` nie podając jej
żadnej wartości:

```python
def wypisz(obiekt):
    print(obiekt)
    return
```

Efekt będzie taki sam jak wtedy gdy nie użyjemy `return`:

```python
>>> rezultat = wypisz(3.14)
3.14
>>> print(rezultat)
None
```

Za takim zachowaniem nie kryje się żadna magia: po prostu twórcy Pythona
przyjęli, że domyślnie funkcja zwraca "nic", a wartość taka będzie
reprezentowana przez `None`.


## Operator `is`

Skoro wiemy, że funkcje mogą zwracać `None`, to w jaki sposób z tego
skorzystać?  Możemy na przykład sprawdzić zwróconą wartość w instrukcji
`if`:

```python
def imie_nazwisko(imie, nazwisko):
    if imie != '' and nazwisko != '':
        return imie + ' ' + nazwisko

def nazwa_uzytkownika(imie, nazwisko, email):
    pelne_nazwisko = imie_nazwisko(imie, nazwisko)
    if pelne_nazwisko == None:
        return email
    else:
        return pelne_nazwisko
```

W powyższym przykładzie funkcja `nazwa_uzytkownika` zwraca pełną nazwę
użytkownika na podstawie jego imienia, nazwiska i adresu email.  Jeżeli
imię i nazwisko są dane, to zwracane jest pełne nazwisko, w przeciwnym
wypadku zwrócony zostanie tylko adres email.  Sprawdzenie czy pełne
nazwisko jest podane zostało zapisane w instrukcji
`if pelne_nazwisko == None`.

Instrukcja `if zmienna == None` jest poprawna, jednak w ogólnym przypadku
może nie zawsze działać.  Dzieje się tak, ponieważ tworząc bardziej
zaawansowane struktury danych w Pythonie (co nie będzie omówione podczas
tych warsztatów), możemy zmienić zachowanie porównania, w efekcie wpływając
na wynik zwracany przez operator `==`.  Jeżeli zrobimy to nieostrożnie,
może się okazać, że jakaś operacja `if` działa inaczej niż się tego
spodziewamy.  Możemy wybrnąć z tej sytuacji stosując zamiast
tego **operator `is`**:

```python
if pelne_nazwisko is None:
    return email
```

W ten sposób nasz kod będzie niewrażliwy na modyfikacje zachowania
operatora `==`.

Kiedy zatem używać `is`?  Używaj tego operatora zawsze kiedy porównujesz
wartość do `None`.  Póki co nie będzie to robiło różnicy, ale dzięki temu
nabędziesz dobrego nawyku, który w przyszłości okaże się przydatny.

:snake: Napisz funkcję, która jako argument przyjmuje listę i zwróci
również listę, na której znajdą się wszystkie elementy z argumentu,
z wyjątkiem wartości równych `None`.


## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy `None`,
* dowiedzieliśmy się, że porównując wartości do `None` należy stosować
operator `is`.


---

:checkered_flag: Następny rozdział: [Pętla `while`](./15_petla_while.md) :checkered_flag:

