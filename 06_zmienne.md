# Rozdział 6. Zmienne

W tym rozdziale:

* dowiesz się czym jest **zmienna**, jak ją zdefiniować i jak jej używać.


## Zmienna

W poprzednich rozdziałach wykonywaliśmy różne operacje: definiowaliśmy
stringi, mnożyliśmy liczby itd.  Każda z tych operacji zwracała jakiś
wynik, który od razu był wypisywany na ekran.  Tekst i liczby, które
w ten sposób tworzyliśmy, trafiały do pamięci komputera tylko na chwilę
i zaraz po wyświetleniu były z niej usuwane.  W związku z tym w kolejnych
operacjach nie mogliśmy wykorzystać wyników z operacji poprzednich.

Aby poradzić sobie z problemem przechowania wyniku operacji, używamy
**zmiennych**.  Zamiast tłumaczyć jak działają zmienne, najlepiej popatrzeć
na przykład:

```python
>>> x = 7
>>> x
7
>>> 5 + x
12
```

Przeanalizujmy co wydarzyło się w powyższym przykładzie.  Na początku
**zdefiniowaliśmy zmienną**, czyli przypisaliśmy wynik jakiejś operacji
do nazwy.  W tym przypadku operacją jest po prostu definicja liczby `7`,
natomiast nazwą jest `x`.  Od tego momentu mogliśmy używać **zmiennej**
`x` w kolejnych operacjach.  Jeżeli po prostu wpiszemy jej nazwę, wtedy
otrzymamy jej **wartość**.  Możemy też posłużyć się nią w innej operacji,
na przykład dodając ją do innej liczby.

Definiując zmienne możemy posługiwać się innymi zmiennymi:

```python
>>> a = 10
>>> b = 5
>>> c = a + b
>>> c
15
```

Oczywiście w realnym przypadku zmienne nazywamy w taki sposób, aby
mówiły nam co oznaczają:

```python
>>> cena_netto = 120
>>> podatek_vat = cena_netto * 0.23
>>> cena_brutto = cena_netto + podatek_vat
>>> cena_brutto
147.6
```


## Przypisanie

Operację `zmienna = wartość` nazywamy **przypisaniem**.  W wyniku
przypisania Python tworzy *zmienną*, która otrzymuje *wartość*.  Jeżeli
wartość jest operacją (np. dodawaniem), to najpierw jest obliczany jej
rezultat, a następnie zostaje on przypisany do zmiennej.


## Nazwy zmiennych

Tworząc zmienną musimy najpierw wymyślić dla niej nazwę.  Przede wszystkim
powinna ona wprost mówić jakie jest znaczenie zmiennej.  Dzięki temu, tak
jak w powyższym przykładzie, będziemy mogli z łatwością zrozumieć kod
programu.

Poza tym Python narzuca kilka ograniczeń na znaki, jakich możemy użyć
w nazwie zmiennej.  Dozwolone znaki to:

* litery od `a` do `z` (małe) oraz od `A` do `Z` (wielkie),
* cyfry,
* znak `_` (podkreślenie).

Wszystkie pozostałe znaki są niedozwolone. Co istotne, nazwa nie może
zaczynać się od cyfry!

:snake: Utwórz zmienne `imie` oraz `nazwisko`, przypisz do nich swoje imię
i nazwisko.  Następnie na ich podstawie utwórz zmienną `imie_nazwisko`,
która będzie zawierała imię i nazwisko oddzielone spacją.

:snake: Zobacz co się stanie, kiedy spróbujesz stworzyć zmienną, której
nazwa zaczyna się od cyfry.


## Zmiana wartości zmiennej

W każdej chwili możemy zmienić wartość zmiennej:

```python
>>> x = 'Ala ma kota'
>>> x
'ala ma kota'
>>> x = 'kot ma Alę'
>>> x
'kot ma Alę'
>>> x = x + '.'
>>> x
'kot ma Alę.'
```

## Zmienne i metody

W poprzednich rozdziałach wywoływaliśmy różne metody, np. `find` lub
`title`.  Zwróć uwagę, że metody, które możesz wykonać bezpośrednio
na obiekcie, możesz też wykonać na zmiennej:

```python
>>> imie_nazwisko = 'jan kowalski'
>>> imie_nazwisko
'jan kowalski'
>>> imie_nazwisko.title()
'Jan Kowalski'
>>> imie_nazwisko
'jan kowalski'
>>> imie_nazwisko = imie_nazwisko.title()
>>> imie_nazwisko
'Jan Kowalski'
```


## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się czym jest zmienna, jak ją definiować i jak jej używać.

---

:checkered_flag: Następny rozdział: [Funkcje](./07_funkcje.md) :checkered_flag:
