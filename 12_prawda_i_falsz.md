# Rozdział 12. Prawda i fałsz

W tym rozdziale:

* poznasz pojęcia "prawda" i "fałsz" oraz ich reprezentację w Pythonie:
`True` i `False`,
* poznasz **instrukcję warunkową** `if`, która pozwala zmienić przebieg
programu, jeżeli określony warunek zostanie spełniony.


## Prawda, fałsz i warunek

Programy jakie dotąd pisaliśmy składały się z operacji, które Python
wykonywał jedna po drugiej.  Gdy jedna instrukcja została pomyślnie
zrealizowana, program przechodził do wykonania kolejnej.
Pisząc kolejne programy szybko przekonasz się, że taki scenariusz nie
zawsze będzie Ci odpowiadał, ponieważ często chcemy, żeby jakieś operacje
zostały wykonane tylko gdy zostanie spełniony pewien warunek.

Na przykład: mamy listę liczb i chcemy przejść po jej elementach, wypisując
tylko te nieparzyste.  W takim przypadku warunkiem wypisania liczby na
ekran jest "liczba jest nieparzysta".

Języki programowania pozwalają definiować takie warunki i sprawdzać je.
Wynikiem takiego sprawdzenia jest **prawda** lub **fałsz**.  Prawda oznacza
sytuację w której warunek został spełniony.  Przeciwieństwem jest fałsz.
Przykładowo wynikiem warunku "żyrafa to ptak" jest fałsz, a wynikiem dla
"Ziemia nie jest płaska" jest prawda.

Oczywiście w programach nie tworzy się tak abstrakcyjnych warunków.
Zamiast tego będziemy porównywali wartości zmiennych, sprawdzali czy wynik
jakiejś funkcji ma określoną wartość itd.  W tym rozdziale dowiesz się
jak wykonywać takie operacje oraz jak pisać programy, które realizują
różne instrukcje w zależności do tego czy jakiś warunek został spełniony.


## Warunki w Pythonie, `True` i `False`

W Pythonie mamy do dyspozycji szereg operatorów, które pozwalają nam
sprawdzać prawdziwość wyrażeń.  Możemy na przykład porównywać wartości.
Służy do tego operator `==`:

```python
>>> 1 == 2
False
>>> (2 + 2) == (2 * 2)
True
```

Odwrotnością operatora `==` jest `!=`:

```python
>>> 'ala' != 'Ala'
True
>>> [1, 2] != [1, 2]
False
```

Możemy również sprawdzać czy jedna wartość jest większa lub mniejsza od
drugiej:

```python
>>> 100 > 70
True
>>> 70 > 100
False
```

Operatory `>` i `<` można łączyć z `=`, w ten sposób tworząc warunek
"większy lub równy" i "mniejszy lub równy":

```python
>>> 3 >= 2
True
>>> 2 >= 2
True
>>> 1 >= 2
False
```

Zwróć uwagę, że w jednym wyrażeniu można użyć wielu operatorów:

```python
>>> 1 <= 2 < 3 <= 3 < 4
True
```

Ponadto możemy zaprzeczyć całemu wyrażeniu pisząc na początku `not`:

```python
>>> not 1 == 1
False
>>> not 1 == 2
True
```

Oczywiście w każdym przypadku wartości wpisane wprost możemy zastąpić
zmiennymi, a wynik wyrażenia zachować.

```python
>>> temperatura = 26
>>> jest_zimno = temperatura < 10
>>> print(jest_zimno)
False
```


## Porównywanie stringów

Porównywanie liczb wydaje się zrozumiałe, ale w jaki sposób porównywane
są stringi?  Odpowiedź jest prostsza niż mogło by się wydawać:
alfabetycznie.  Litery znajdujące się dalej w alfabecie są "większe"
od tych wcześniejszych.  Poza tym litery małe są "większe" od wielkich.

```python
>>> 'A' < 'B' < 'a' < 'b'
True
```

Co ze stringami, które mają więcej niż jeden znak?  Są one porównywane
znak po znaku, dopóki któryś z nich nie będzie się różnił, albo dopóki
jeden ze stringów nie będzie dłuższy.  W tym drugim przypadku większy
będzie ten string który ma więcej znaków.

```python
>>> 'a' < 'ala'
True
>>> 'ala' == 'ala'
True
>>> 'ala' < 'ala ma kota'
True
```


## Operator `in`

Poza dotychczas omówionymi operatorami, jest jeszcze jeden, przydatny
szczególnie kiedy pracujemy z listami.  Operator `in` zwraca `True` jeżeli
dany element znajduje się na liście:

```python
>>> 'Basia' in ['Tomek', 'Magda', 'Karol', 'Basia']
True
>>> 12 in [10, 20, 30, 40]
False
```


## Instrukcja warunkowa `if`

Sprawdzanie czy jakieś wyrażenie jest prawdziwe nie miałoby większego sensu
gdybyśmy nie mogli w jakiś sposób na tej podstawie podjąć decyzji
o dalszym przebiegu naszego programu.  W tym celu używamy **instrukcji
warunkowej** `if`:

```python
if temperatura > 30.0:
    print('Uf jak gorąco!')
```

Struktura tej instrukcji jest bardzo prosta: po słowie `if` wpisujemy
warunek, następnie dwukropek i w kolejnych liniach, po wcięciu, instrukcje,
które zostaną wykonane jeżeli warunek będzie prawdziwy (mówimy: jeżeli
warunek zostanie spełniony).

:snake: Napisz funkcję, która przyjmuje argumenty `element` i `lista`
i jeżeli dany element znajduje się na liście, to zwraca jego pozycję
(użyj metody `index`), w przeciwnym wypadku zwraca `-1`.

:snake: Napisz funkcję `iloraz`, która przyjmuje argumenty `dzielna`
i `dzielnik`. Jeżeli dzielnik jest różny od zera, funkcja powinna zwrócić
wynik dzielenia.  W przeciwnym wypadku powinna wypisać komunikat o błędzie.


## `if ... else` oraz `elif`

Do instrukcji `if` możemy dopisać drugą część, która zostanie wykonana
tylko jeżeli warunek nie będzie spełniony:

```python
if godzina <= godzina_odjazdu:
    print('Godzina odjazdu:', godzina_odjazdu)
else:
    print('Przepraszamy za opóźnienie')
```

Zwróć uwagę na wcięcia w kodzie: `if` oraz `else` są na tym samym
"poziomie".

Jeżeli chcemy, możemy w ramach jednej instrukcji `if` sprawdzić kilka
alternatywnych warunków, jeżeli poprzednie okażą się nieprawdziwe:

```python
if 5 <= godzina < 12:
    print('rano')
elif godzina == 12:
    print('południe')
elif 12 < godzina < 17:
    print('popołudnie')
elif 17 < godzina < 20:
    print('wieczór')
else:
    print('noc')
```

:snake: Napisz funkcję, która porównuje dwie liczby.  Jako argumenty
powinna przyjmować liczby `a` i `b`.  Jeżeli `a` jest większe od `b`
powinna zwrócić 1, jeżeli liczby są równe `0`, a jeżeli `a` jest mniejsze
od `b`, `-1`.  Dodatkowo, w zależności od wyniku porównania, funkcja
powinna wypisać jeden z komunikatów: `a < b`, `a == b` lub `a > b`.


## Łączenie warunków

Czasami będziemy chcieli wykonać jakieś operacje tylko jeżeli spełnionych
zostanie kilka warunków jednocześnie.  W takim wypadku możemy użyć
operatora `and`:

```python
if substancja == 'woda' and temperatura > 100:
    stan_skupienia = 'para wodna'
```

Gdybyśmy chcieli, żeby operacja została wykonana jeżeli przynajmniej jeden
z kilku warunków zostanie spełniony, to należy użyć operatora `or`:

```python
if produkt == 'sok' or produkt == 'herbata':
    cena = 4.50
```

Operatory `or` i `and` można łączyć w jednym wyrażeniu.


## Prawdziwość obiektów, funkcja `bool`

Warunek nie musi być porównaniem.  Każdy typ obiektu w jakiś sposób
definiuje prawdziwość.  Na przykład pusta lista to fałsz, a lista z co
najmniej jednym jednym elementem to prawda.

Aby przekonać się jaką wartość w rozumieniu logiki reprezentuje dany
obiekt, możemy posłużyć się funkcją wbudowaną `bool`.  Przyjmuje ona jeden
argument - dowolny obiekt - i zwraca jego wartość logiczną: `True` lub
`False`.

```python
>>> bool([])
False
>>> bool([1, 2, 3])
True
```

:snake: Dla każdego z następujących typów odszukaj wartość, dla której
funkcja `bool` zwróci `True` i taką dla której zwróci `False`: string,
krotka, integer, float.

Ponieważ każdy obiekt można rozważać w kategorii "prawdziwości", każdym
obiektem możemy posłużyć się w instrukcji `if`:

```python
if imie and nazwisko and len(haslo) > 5:
    print('Podano prawidłowe dane')
```

:snake: Napisz funkcję, która jako argument przyjmie listę i zwróci `True`
jeżeli wszystkie elementy na tej liście są prawdziwe, albo `False` jeżeli
przynajmniej jeden element nie jest prawdziwy.


## :pushpin: Podsumowanie

W tym rozdziale:

* nauczyliśmy się sprawdzać prawdziwość wyrażeń,
* poznaliśmy instrukcję `if`, która może zmienić przebieg programu gdy
określone wyrażenie jest prawdziwe.


---

:checkered_flag: Następny rozdział: [Słowniki](./13_slowniki.md) :checkered_flag:

