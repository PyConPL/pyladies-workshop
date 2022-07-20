# Rozdział 4. Liczby

W tym rozdziale:

* dowiesz się czym jest `integer` oraz `float`,
* nauczysz się wykonywać operacje arytmetyczne na liczbach.

## Liczby całkowite

Aby zdefiniować liczbę całkowitą (**integer**) po prostu wpisz ją nie stawiając
spacji między cyframi:

```python
>>> 2017
2017
```

Liczby możemy dodawać i odejmować:

```python
>>> 20 + 17
37
>>> 2 + 0 + 1 + 7
10
>>> 20 - 17
3
>>> 20 - 1 - 7
12
```

...mnożyć i dzielić:

```python
>>> 20 * 17
340
>>> 20 / 17
1.1764705882352942
```

...dzielić bez reszty:

```python
>>> 20 // 17
1
```

...podnosić do potęgi:

```python
>>> 201 ** 7
13254776280841401
```

...albo sprawdzić resztę z dzielenia (ang. modulo):

```python
>>> 20 % 17
3
```

Wszystkie te operacje możemy dowolnie łączyć:

```python
>>> 20 / 2 + 17 * 3
61
```

Jeżeli chcemy mieć większą kontrolę na kolejnością wykonywania działań, możemy
posłużyć się nawiasami okrągłymi:

```python
>>> (20 * (2 + 17)) / 3
126
```

:snake: Oblicz następujące wartości:

* suma dzisiejszego dnia, numeru miesiąca i roku,
* wynik dzielenia roku Twojego urodzenia przez sumę dnia i miesiąca,
  w których się urodziłaś.


## Liczby rzeczywiste

Wszystkie powyższe operacje możemy wykonywać również na liczbach rzeczywistych
(**float**, zmiennoprzecinkowych):

```python
>>> 2.5 * 2.0
5.0
>>> 7 / 2.0
3.5
>>> 6.7 + 0.3 - 2.5
4.5
>>> 1.0 / 3
0.3333333333333333
```

:snake: Czy wiesz kiedy Python zwróci *float* a kiedy *integer*? Upewnij się,
sprawdź różne kombinacje liczb i działań.


## Operatory i ich kolejność

Znaki, których używamy do wykonywania działań (`+`, `*` itd.) nazywamy **operatorami**.
Każdy operator ma swój priorytet, co oznacza, że jeżeli w jednym działaniu użytych
jest kilka różnych operatorów (np. `2 + 1 * 3`), to Python najpierw obliczy te, które
mają wyższy priorytet.

Przykładowo, w takim działaniu:

```python
>>> 4 + 10 * 6
```

najpierw zostanie wykonane mnożenie, a dopiero potem dodawanie, ponieważ
operator `*` ma wyższy priorytet niż `+`, czyli rezultatem będzie `64`.

Poniższa tabelka prezentuje operatory oraz ich znaczenie. Kolejność wierszy odpowiada
priorytetowi, czyli na samej górze są operatory z najwyższym priorytetem, a na dole
z najniższym.

Operatory | Znaczenie
--------- | ---------
`**` | Potęgowanie
`*`, `/`, `//`, `%` | Mnożenie, dzielenie, dzielenie całkowite, modulo
`+`, `-`  | Dodawanie, odejmowanie

## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się, jak definiować liczby całkowite (**integer**)
  i zmiennoprzecinkowe (**float**),
* poznaliśmy najważniejsze **operatory** matematyczne i ich priorytety.

---

:checkered_flag: Następny rozdział: [Błędy](./05_bledy.md) :checkered_flag:
