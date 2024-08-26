# Rozdział 8. Funkcja `print`

W tym rozdziale:

* poznasz funkcję wbudowaną `print`.


## Wypisywanie tekstu na ekran

Gdy korzystaliśmy z trybu interaktywnego i chcieliśmy wypisać coś na ekran,
wystarczyło wpisać jakieś wyrażenie i wcisnąć Enter:

```python
>>> 2 + 2
4
>>> x = 'PyLadies'
>>> x
'PyLadies'
```

Mogliśmy tak robić, ponieważ w ten sposób działa tryb interaktywny:
wykonuje operację i wyświetla jej wynik.  Jednak zazwyczaj programy
w Pythonie są bardziej złożone i często zdarza się, że chcemy zobaczyć
więcej niż tylko wynik ostatniej operacji.  Na przykład gdy piszemy program,
który przetwarza plik tekstowy i chcemy, żeby dla każdej linijki tekstu
wypisał coś na ekran.  W takim wypadku z pomocą przychodzi funkcja
wbudowana `print`.


## `print`

Funkcja ta przyjmuje dowolną liczbę argumentów i wypisuje wszystkie na
ekran, oddzielając je spacjami:

```python
>>> print(2017)
2017
>>> print('PyCon PL', 2017)
PyCon PL 2017
```

Do `print` można przekazywać również zmienne:

```python
>>> temperatura = 24
>>> print('Temperatura:', temperatura, 'stopnie Celsjusza')
Temperatura: 24 stopnie Celsjusza
```

:snake: Napisz funkcję, która przyjmuje argument `rok_urodzenia`, wypisuje
tekst `Masz X lat`, gdzie `X` to wiek w roku 2017, oraz zwraca ten wiek.


## Formatowanie stringów

W tym miejscu warto wrócić do stringów i opowiedzieć o jeszcze jednej,
bardzo przydatnej metodzie: `format`.  Służy ona do **formatowania
stringów**, czyli "wstawiania" do nich wartości zmiennych.  Spójrz na
poniższy przykład:

```python
>>> 'ala {} kota'.format('ma')
'ala ma kota'
```

Jak widzisz, wywołanie metody `format` spowodowało, że para znaków `{}`
została zastąpiona argumentami funkcji.  W podobny sposób możemy wstawić
dowolną liczbę i typ obiektów:

```python
>>> szerokosc = 110
>>> wysokosc = 50.5
>>> jednostka = 'mm'
>>> '{}x{} {}'.format(szerokosc, wysokosc, jednostka)
'110x50.5 mm'
```

Możliwości metody `format` nie kończą się na zwykłym wstawianiu wartości
do stringa.  [Dokumentacja Pythona](https://docs.python.org/3.12/library/string.html#formatspec)
w szczegółach opisuje tę funkcję.  Warto przyjrzeć się choćby przykładom,
które tam zamieszczono.

:snake: Zobacz co się stanie, jeżeli liczba argumentów metody `format`
będzie __mniejsza__ niż liczba wystąpień `{}` w stringu.


## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy funkcję `print` oraz metodę `format`.

---

:checkered_flag: Następny rozdział: [Listy](./09_listy.md) :checkered_flag:

