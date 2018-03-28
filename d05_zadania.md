# Dodatek 5. Zadania

Ten dodatek zawiera zbiór zadań, które pomogą Ci utrwalić wiedzę zdobytą
podczas kursu. Nauczą Cię też dobierać odpowiednie typy danych i operacje
w zależności od problemu przed jakim stajesz.

Rozwiązując zadania skup się przede wszystkim na napisaniu działającego
programu. Nie myśl o jego "jakości": tym jak szybko działa, albo jak
ładnie wygląda kod. Zacznij od rozwiązania problemu, a dopiero potem
oceń czy trzeba cokolwiek poprawić.


---


## 1. Funkcja `title`

Napisz funkcję o nazwie `title`, która będzie działała tak jak metoda
`title` na stringu, ale nie używaj tej metody.

Przykład:

```python
>>> title('ala MA kOTA')
'Ala Ma Kota'
```


## 2. Grupowanie słowników

Napisz funkcję `grupuj`, która będzie grupowała słowniki według wartości
dla wybranego klucza.

Przykład:

```python
>>> owoce = [
...     {'nazwa': 'jabłko', 'kolor': 'czerwony'},
...     {'nazwa': 'banan', 'kolor': 'żółty'},
...     {'nazwa': 'cytryna', 'kolor': 'żółty'},
...     {'nazwa': 'gruszka', 'kolor': 'zielony'},
...     {'nazwa': 'truskawka', 'kolor': 'czerwony'}
... ]
>>> grupy = grupuj(owoce, 'kolor')
>>> for kolor, lista_owocow in grupy.items():
...     print(kolor, lista_owocow)
...
czerwony [{'nazwa': 'jabłko', 'kolor': 'czerwony'}, {'nazwa': 'truskawka', 'kolor': 'czerwony'}]
żółty [{'nazwa': 'banan', 'kolor': 'żółty'}, {'nazwa': 'cytryna', 'kolor': 'żółty'}]
zielony [{'nazwa': 'gruszka', 'kolor': 'zielony'}]
```

Funkcja powinna przyjmować dwa argumenty: listę słowników oraz nazwę
klucza. Wynikiem funkcji powinien być słownik, gdzie kluczami będą nazwy
grup, a wartościami listy słowników znajdujących się w tych grupach.


## 3. Algorytm "delta compression"

Napisz funkcję `delta_compression`, która jako argument przyjmuje
**posortowaną** listę liczb całkowitych i zwróci tę samą listę
skompresowaną następującym algorytmem:

1. Pierwszy element listy wyjściowej jest taki sam jak pierwszy
   element listy wejściowej.
2. Każdy następny element listy wyjściowej jest równy różnicy między
   odpowiadającym mu elementem listy wejściowej a elementem
   poprzedzającym go, czyli `WY[i] = WE[i] - WE[i-1]`.

Przykład:

```python
>>> we = [5, 7, 11, 21, 28, 39]
>>> delta_compression(we)
[5, 2, 4, 10, 7, 11]
```


## 4. Grupuj i licz

Napisz funkcję `grupuj_i_licz`, która jako argument przyjmie listę
dwuelementowych krotek, gdzie pierwszy element to data (instancja
`datetime.date`), a drugi to liczba całkowita, i obliczy sumy tych liczb
dla każdego miesiąca jaki występuje wśród tych dat. Funkcja powinna zwrócić
słownik, gdzie kluczami będą krotki `(rok, miesiąc)`, a wartościami sumy
liczb.

Przykład:

```python
>>> x = grupuj_i_licz([
...     (datetime.date(2015, 1, 29), 10),
...     (datetime.date(2015, 1, 30), 12),
...     (datetime.date(2015, 1, 31), 10),
...     (datetime.date(2015, 2, 1), 9),
...     (datetime.date(2015, 2, 2), 9)
... ])
>>> print(x)
{(2015, 1): 32, (2015, 2): 18}
```


## 5. Cięcie stringa

Napisz funkcję `tnij`, która przyjmie dwa argumenty: tekst oraz liczbę.
Funkcja powinna zwrócić tekst pocięty na fragmenty (listę), każdy
o długości takiej jak liczba podana w argumencie. Ostatni fragment może
być krótszy niż wymagana długość.

Przykład:

```python
>>> tnij('12345678', 3)
['123', '456', '78']
>>> tnij('12345678', 5)
['12345', '678']
>>> tnij('123', 4)
['123']
```


## 6. Liczenie słów

Napisz funkcję, która jako argument przyjmie dowolny tekst i zwróci
słownik, którego kluczami będą wszystkie słowa z tego tekstu, a wartościami
będą liczby wystąpień tych słów w tekście. Funkcja powinna być obojętna
na wielkość liter (czyli 'Kot' i 'kot' mają być traktowane jako jedno
słowo) i powinna ignorować znaki interpunkcyjne.

Przykład:

```python
>>> tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sollicitudin ultricies eros, vitae eleifend ipsum sodales ut. Pellentesque libero ipsum, euismod eget volutpat nec, hendrerit vel turpis."
>>> licz_slowa(tekst)
{'sollicitudin': 1, 'elit': 1, 'vel': 1, 'eleifend': 1, 'sodales': 1, 'eros': 1, 'sit': 1, 'nec': 1, 'consectetur': 1, 'pellentesque': 1, 'vitae': 1, 'eget': 1, 'hendrerit': 1, 'dolor': 1, 'turpis': 1, 'euismod': 1, 'integer': 1, 'lorem': 1, 'amet': 1, 'ipsum': 3, 'ut': 1, 'ultricies': 1, 'libero': 1, 'adipiscing': 1, 'volutpat': 1}
```
