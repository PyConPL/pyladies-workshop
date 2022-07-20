# Rozdział 3. Funkcja `help`

W tym rozdziale:

* poznasz funkcję `help`.


## Pomoc w Pythonie

Nawet najlepszy programista nigdy nie zapamięta wszystkich funkcji i metod,
jakie oferuje Python.  W trakcie tego szkolenia poznasz ich wiele, ale
za kilka dni zapomnisz, jak działają.  Nie przejmuj się, twórcy Pythona
pomyśleli o tym...


## Dokumentacja metod w Pythonie

Każda metoda zdefiniowana w Pythonie posiada **dokumentację**, która
w kilku słowach opisuje jej działanie.  Aby przeczytać tę dokumentację,
należy wywołać funkcję `help`, na przykład:

```python
>>> help('jakiś string'.find)
Help on built-in function find:

find(...)
    S.find(sub [,start [,end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
```

Dokumentacja nie zawsze jest pisana prostym językiem, ale nie zrażaj się.
Warto oswajać się z nią od samego początku. Przeczytaj powyższy fragment
jeszcze raz, a zaraz wyjaśnimy, co dokładnie oznaczają poszczególne części.

Dokumentacja pokazuje wszystkie argumenty jakie przyjmuje dana metoda.
Tę informację zawiera linia "S.find(sub [,start [,end]])".
Dalej dokumentacja informuje jakiego typu wynik jest zwracany oraz w skrócie
wyjaśnia, co ta metoda robi.  Dzięki temu możemy ją sobie bardzo szybko
przypomnieć.

Zwróć uwagę, że w tym przykładzie nie otworzyliśmy nawiasu przy nazwie
metody `find`, a co za tym idzie, nie podaliśmy jej żadnych argumentów.
W ten sposób zamiast wywołać tę metodę, po prostu posłużyliśmy się jej
nazwą.  Kiedy przekażemy taką nazwę do funkcji `help`, Python pokaże nam
dokumentację danej metody.

:snake: Użyj funkcji `help` i przeczytaj dokumentację do metod `replace`
i `count` oraz do funkcji `len`.


## :pushpin: Podsumowanie

W tym rozdziale:

* poznaliśmy funkcję `help` i dowiedzieliśmy się, że warto jej używać
wtedy, kiedy nie rozumiemy jakiejś metody lub nie pamiętamy jak działa.


---

:checkered_flag: Następny rozdział: [Liczby](./04_liczby.md) :checkered_flag:
