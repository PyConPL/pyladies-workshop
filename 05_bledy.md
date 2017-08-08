# Rozdział 5. Błędy

W tym rozdziale:

* dowiesz się czym są **wyjątki**,
* nauczysz się czytać komunikaty o błędach.

## Wyjątki

Tworząc programy nigdy nie jesteśmy w stanie przewidzieć wszystkich
sytuacji jakie mogą się wydarzyć.  Czasami stanie się coś, czego się nie
spodziewaliśmy, a czasami po prostu użyjemy języka w nieprawidłowy sposób.
Na każdą taką sytuację Python zareaguje zgłaszając błąd.  Dzięki temu
dowiemy się na czym polegała nasza pomyłka i będziemy mogli poprawić kod
programu, żeby uniknąć tego samego problemu w przyszłości.

Słowa "błąd" czy "problem" są bardzo ogólne, ponieważ mogą dotyczyć rzeczy
na które jako programiści nie mamy wpływu.  Dlatego posługujemy są terminem
**wyjątek**.  Oznacza on sytuację, w której Python zatrzymał wykonywanie
programu, ponieważ napotkał *wyjątkową* sytuację, której sam nie potrafił
obsłużyć.  Mówi się, że program **rzucił wyjątek**.  Kiedy tak się stanie,
rolą programisty jest dostosowanie programu w taki sposób, aby
w przyszłości podobna sytuacja nie skutkowała zatrzymaniem.

Czym są wyjątkowe sytuacje o których wspomnieliśmy?  Może to być próba
wykonania operacji, której Python nie potrafi zrealizować, na przykład
dodanie liczby do tekstu.  Albo błąd "za mało miejsca na dysku twardym"
podczas zapisywania jakiegoś pliku.  Nie sposób wymienić wszystkie takie
możliwości - z czasem poznasz zestaw najczęściej występujących wyjątków
i nauczysz się przewidywać jakie operacje mogą skutkować rzuceniem wyjątku.

## Jak czytać wyjątki

Spróbujmy wywołać wyjątek, dodając tekst do liczby:

```python
>>> 123 + 'ala ma kota'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Jak widzisz, zamiast zwrócić wynik operacji, Python zgłosił wyjątek.
Przeczytajmy go linijka po linijce.

* Na samym początku widzimy zawsze wiadomość
`Traceback (most recent call last):`.  Słowem "Traceback" określa się listę
operacji, których wykonanie spowodowało błąd.  W tym przypadku wykonana
została tylko jedna operacja (dodawanie), ale w przyszłości spotkasz się
z sytuacjami, w których wyjątek został rzucony w skutek wykonania całego
ciągu poleceń.  Python zawsze pokazuje cały traceback, aby programista
mógł zrozumieć co poszło nie tak.  Zdanie `most recent call last`
informuje, że ostatnia operacja na liście została wykonana najpóźniej
spośród wszystkich.
* `File "<stdin>", line 1, in <module>` to właśnie traceback. W naszym
przypadku jest to tylko jedna linijka.  Widzimy tutaj opis miejsca,
w którym wystąpił błąd: `File <stdin>`, co oznacza po prostu "standardowe
wejście" (*standard input*), jak określa się sposób wprowadzania informacji
do komputera z użyciem samego tekstu.  Oznacza to tyle, że błąd powstał
w trybie interaktywnym.
* Ostatnia linijka zawiera najważniejszą informację, czyli bezpośrednią
przyczynę błędu.  Zaczyna się od typu wyjątku.  W tym przypadku to
`TypeError`.  Typ można rozumieć jako kategorię: nie mówi on czego
dokładnie dotyczył błąd, ale pozwala zaklasyfikować różne wyjątki, aby
łatwiej byłe je zrozumieć.  `TypeError` oznacza niepoprawne użycie jakiegoś
typu, w tym przypadku typów *integer* i *string*.  Dalej widzimy szczegóły
błędu: operator dodawania został użyty na liczbie całkowitej (*integer*)
oraz łańcuchu znaków (*string*), co nie jest dozwolone.

Tworząc bardziej zaawansowane programy spotkasz się z jeszcze dłuższymi
komunikatami o błędach.  Nie zniechęcaj się tym: każdy wyjątek sprowadza
się do tylko jednej niepoprawnej operacji, a traceback, nieważne jak długi,
pomoże Ci zlokalizować przyczynę niepowodzenia.  Jeżeli mimo wszystko nie
będziesz w stanie zrozumieć dlaczego Twój program przestał działać, wklej
ostatnią linijkę komunikatu do wyszukiwarki internetowej.  Jest bardzo
możliwe, że ktoś już kiedyś spotkał się z takim problemem i znalazł
rozwiązanie.

:snake: Wywołaj błędy i przeczytaj ze zrozumieniem wyjątki spowodowane
następującymi operacjami: dzielenie przez zero; wywołanie na dowolnym
stringu metody, która nie istnieje; wykonanie kodu, który nie ma sensu
(możesz wpisać losowy ciąg znaków).

## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się czym jest wyjątek i jak czytać jego treść.

---

:checkered_flag: Następny rozdział: [Zmienne](./06_zmienne.md) :checkered_flag:
