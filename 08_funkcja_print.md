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
więcej niż tylko ostateczny wynik.  Na przykład gdy piszemy program, który
przetwarza plik tekstowy i chcemy, żeby dla każdej linijki tekstu wypisał
coś na ekran.  W takim wypadku z pomocą przychodzi funkcja wbudowana
`print`.


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


## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy funkcję `print`.

---

:checkered_flag: Następny rozdział: [Listy](./09_listy.md) :checkered_flag:

