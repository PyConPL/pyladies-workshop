# Rozdział 11. Krotki

W tym rozdziale:

* dowiesz się czym jest **krotka**.


## Krotka

Czytając kod programów napisanych w Pythonie bardzo szybko natkniesz się
na coś z pozoru bardzo podobnego do listy:

```python
waluty = ('EUR', 'PLN', 'USD')
```

Powyższy przykład to definicja **krotki**.  Na pierwszy rzut oka różni się
ona od listy tylko tym, że zamiast nawiasów kwadratowych ma okrągłe.
Jednak krotka posiada jedną istotną cechę, która odróżnia ją od listy:
nie można jej modyfikować.  Oznacza to, że do raz utworzonej krotki nie
można dodawać elementów, usuwać ich, ani nawet zmieniać.  Dlatego też nie
znajdziemy w krotce metod `append` ani `remove`.  Za to z powodzeniem
możemy odnosić się do poszczególnych elementów używając ich indeksów:

```python
>>> waluty[1]
'PLN'
```

Oznacza to, że możemy również iterować po krotce pętlą `for`.  Jeśli zaś
przekażemy krotkę do funkcji `len`, to dostaniemy liczbę jej elementów.

:snake: Napisz funkcję, która jako argument przyjmie krotkę i zwraca
listę, która zawiera dokładnie takie same elementy.


## Zastosowanie krotek

Z pozoru krotka może się wydawać czymś zupełnie zbędnym.  Po co nam taka
lista, której nie można modyfikować?  Otóż w wielu przypadkach potrzebujemy
dokładnie czegoś takiego.  Dobrym przykładem jest właśnie zbiór nazw walut.
Wyobraźmy sobie, że piszemy program do przeliczania wartości pieniężnych
między różnymi walutami.  W naszym programie będą zmieniały się kursy,
ale same waluty będą cały czas takie same.  Dlatego możemy je zdefiniować
w krotce, tym samym chroniąc się przed modyfikacją zbioru walut, co byłoby
niepożądane.  Nawet jeżeli w przyszłości będziemy chcieli dodać kolejną
walutę, łatwiej będzie wydać nową wersję programu niż ryzykować modyfikację
zbioru, który powinien pozostać niezmieniony.

Podobnych przykładów jest więcej i czytając kod różnych programów szybko
przekonasz się, że krotki przydają się częściej niż mogło by się wydawać.


## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się czym jest krotka i jakie operacje możemy na niej
wykonywać.


---

:checkered_flag: Następny rozdział: [Prawda i fałsz](./12_prawda_i_falsz.md) :checkered_flag:
