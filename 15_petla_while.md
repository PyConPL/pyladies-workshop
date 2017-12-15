# Rozdział 15. Pętla `while`

W tym rozdziale:

* nauczysz posługiwać się pętlą `while`.


## Pętla `while`

Wiesz już czym jest pętla oraz znasz jedną z nich: `for`.  Teraz poznasz
drugą, jednocześnie ostatnią jaka istnieje w Pythonie: `while`.  Jej
struktura jest jeszcze prostsza od poprzedniej:

```python
licznik = 1
while licznik < 10:
    print(licznik)
    licznik = licznik + 1
```

Definicję pętli zaczynamy słowem `while`, następnie definiujemy warunek
(tak jak w instrukcji `if`), a po dwukropku, w kolejnych linijkach
i po wcięciu, wypisujemy instrukcje, które będą wykonywane tak długo
jak warunek będzie prawdziwy.

Zwróć uwagę, że jeżeli zdefiniujemy warunek, który zawsze będzie prawdziwy,
wtedy pętla będzie wykonywana w nieskończoność:

```python
while 1 == 1:
    print('.')
```

:snake: Napisz funkcję, która przyjmie listę jako argument i wypisze
wszystkie jej elementy przy użyciu pętli `while`.

## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy pętlę `while`.


---

:checkered_flag: Następny rozdział: [Biblioteka standardowa](./16_biblioteka_standardowa.md) :checkered_flag:
