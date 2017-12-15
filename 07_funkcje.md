# Rozdział 7. Funkcje

W tym rozdziale:

* nauczysz się definiować **funkcje**.


## Czym jest funkcja

Dotychczas dowiedzieliśmy się czym jest *string*, *integer* i *float*, oraz
jak używać zmiennych do przechowywania wartości pomiędzy operacjami.
Dzięki temu możemy napisać program, który wykona jakieś operacje na danych,
na przykład przetworzy tekst, lub coś obliczy, a następnie wypisze wynik
na ekran.  Im bardziej zaawansowane problemy będziemy chcieli rozwiązać
naszym programem, tym bardziej skomplikowany będzie jego kod.

Jednym ze sposobów na pisanie bardziej zrozumiałego kodu jest definiowanie
funkcji.  **Funkcja** to wydzielony zbiór instrukcji, który możemy
wielokrotnie wykonać w programie.  **Definicja funkcji** to sposób w jaki
opisujemy, które operacje mają być zawarte w funkcji.

Przykładowo, poniższa funkcja zwraca liczbę podniesioną do kwadratu:

```python
def kwadrat(liczba):
    wynik = liczba ** 2
    return wynik
```

Linijka zaczynająca się od słowa `def` to **nagłówek funkcji**.  Składa się
z następujących elementów:

* słowo `def`,
* **nazwa** funkcji (w tym przykładzie to `kwadrat`),
* **lista argumentów** ujęta w nawiasy okrągłe (tutaj mamy jeden argument
`liczba`, ale możemy ich podać wiele, oddzielając je przecinkami),
* dwukropek.

Zwróć uwagę na spacje! W całym nagłówku odstęp jest tylko między słowem
`def` a nazwą funkcji. Gdyby funkcja miała wiele argumentów oddzielonych
przecinkami, to moglibyśmy wstawić spacje obok przecinków, aby poprawić
czytelność kodu. Poza tymi dwoma przypadkami, w nagłówku nie powinno więcej
spacji.

W kolejnych linijkach po nagłówku mamy **ciało funkcji**.  Są to po prostu
instrukcje, które zostaną wykonane kiedy użyjemy funkcji.  W powyższym
przykładzie ciało zawiera dwie operacje: podniesienie do kwadratu wartości
zmiennej `liczba` i przypisanie jej do zmiennej `wynik`, oraz zwrócenie
wartości zmiennej `wynik`.  **Zwrócenie** to określenie jaka wartość ma
być wynikiem danej funkcji.  Służy do tego słowo `return`.  Jeżeli wpiszemy
po nim nazwę zmiennej, to jej wartość będzie wynikiem.  Możemy także
zwrócić rezultat nie przypisując do wcześniej do zmiennej:

```python
def kwadrat(liczba):
    return liczba ** 2
```


## Praca z edytorem

Zanim zdefiniujesz swoją pierwszą funkcję, zatrzymajmy się na chwilę.  Jak
dotąd wszystkie operacje wykonywaliśmy w trybie interaktywnym, gdzie
wpisywaliśmy kod, wciskaliśmy Enter i dostawaliśmy wynik.  Gdy zaczniemy
pracować z funkcjami takie podejście może okazać się uciążliwe.  Dużo
wygodniej będzie teraz przejść do **edytora**.

Od tej pory każdy przykład, który nie będzie zaczynał się od `>>>` należy
rozumieć jako kod wpisany w edytorze i uruchomiony przyciskiem "run".


## Definicja i wywołanie funkcji

Przepisz teraz do edytora kod funkcji zapisany poniżej.  Zwróć szczególną
uwagę na **wcięcia**.  Każda linijka ciała funkcji musi zaczynać się od
wcięcia.  Co istotne, wszystkie te wcięcia **muszą mieć taką samą
szerokość**.  Oznacza to, że jeżeli w pierwszej linijce zrobisz wcięcie
na dwie spacje, to wszystkie pozostałe linijki aż do końca funkcji też
muszą mieć wcięcie na dwie spacje.  Jak zauważysz, edytor sam zrobi
wcięcie kiedy po wpisaniu nagłówka wciśniesz Enter.  Jeżeli by tego nie
zrobił, wtedy najłatwiej jest robić wcięcia klawiszem Tab.

```python
def kwadrat(liczba):
    wynik = liczba ** 2
    return wynik
```

Wciśnij teraz przycisk "run".  Jeżeli w oknie trybu interaktywnego nie
zauważysz żadnego błędu, będzie to oznaczało, że funkcja została prawidłowo
zdefiniowana.  Teraz możemy ja wywołać w trybie interaktywnym:

```python
>>> kwadrat(5)
25
>>> kwadrat(3) + kwadrat(1)
10
```

Jak widzisz, aby wywołać funkcję, wystarczy wpisać jej nazwę, po czym
w nawiasach wpisać wartość argumentu.  Jeżeli argumentów jest wiele, to
należy je oddzielić przecinkami.

:snake: Zdefiniuj funkcję o nazwie `pole_kola`, która przyjmuje argument
`promien` i zwraca wartość równania `3.14 * (promien ** 2)`.  Wywołaj ją
w oknie trybu interaktywnego.

:snake: Wywołaj funkcję `pole_kola` bez argumentu: `pole_kola()`. Czy
rozumiesz treść wyjątku jaki został rzucony?

:snake: Wywołaj funkcję `pole_kola` z dwoma argumentami: `pole_kola(2, 3)`.
Porównaj treść wyjątku do błędu z poprzedniego zadania.


## Argumenty

Funkcja nie musi posiadać żadnych argumentów, w takim wypadku nawiasy
w nagłówku zostawiamy puste:

```python
def funkcja_bez_argumentow():
    return 123
```

Jak już wspomnieliśmy, funkcje mogą przyjmować więcej niż jeden argument:

```python
def suma(a, b):
    return a + b


def osoba(imie, nazwisko, tytul):
    imie_nazwisko = imie + ' ' + nazwisko
    return tytul + ' ' + imie_nazwisko.title()
```

Takie funkcje wywołujemy podobnie jak te z jednym argumentem:

```python
>>> funkcja_bez_argumentow()
123
>>> suma(100, 45)
145
>>> suma(100, -20)
80
>>> osoba('jan', 'KOWALSKI', 'doktor')
'doktor Jan Kowalski'
```

:snake: Napisz funkcję `cena_brutto`, która przyjmuje argumenty
`cena_netto` oraz `vat` i zwraca wartość brutto obliczoną według wzoru
`netto * (1 + vat)`.

:snake: Napisz funkcję `imie_nazwisko`, która przyjmuje argumenty `imie`
oraz `nazwisko` i zwraca stringa z imieniem i nazwiskiem oddzielonymi
spacją.  Upewnij się, że każde słowo w stringu zaczyna się od wielkiej
litery (użyj metody `title`).  Następnie napisz funkcję `lubi`,
z argumentami `imie`, `nazwisko` oraz `co` i wywołana w ten sposób:
`lubi('jan', 'kowalski', 'KALAFIORY')` zwróci stringa
`'Jan Kowalski lubi kalafiory'`.  Pisząc funkcję `lubi` użyj funkcji
`imie_nazwisko`.


## Funkcje wbudowane

Poza funkcjami, które sami możemy zdefiniować, istnieją funkcje, które
zawsze są dostępne w interpreterze Pythona.  Nazywamy je **funkcjami
wbudowanymi**.  Przykładem jest funkcja `len`, o której mówiliśmy w jednym
z poprzednich rozdziałów:

```python
>>> len('python')
6
```

Poza tym mamy jeszcze [67 innych funkcji wbudowanych](https://docs.python.org/3/library/functions.html).
Część z nich poznasz w kolejnych rozdziałach, a kilka innych opisaliśmy
poniżej.

### `str`

Przyjmuje jako argument dowolny obiekt i zwraca jego reprezentację jako
string:

```python
>>> str(2017)
'2017'
```

:snake: Zamień na string liczbę ujemną.

:snake: Zobacz co się stanie, jeżeli jako argument przekażesz do `str`
tekst.


### `int`

Przyjmuje jako argument dowolny obiekt i zamienia go na integer:

```python
>>> int(' 123 ')
123
```

:snake: Zobacz co się stanie, gdy przekażesz do funkcji `int` liczbę
z częścią ułamkową (float), np. `3.14`.

:snake: Zobacz co się stanie, jeśli przekażesz do `int` stringa, w którym
nie ma żadnej liczby.

:snake: Zobacz co się stanie, kiedy przekażesz do `int` stringa, w którym
są zarówno litery jak i cyfry, np. `Ala ma 2 koty`.


### `float`

Przyjmuje jako argument dowolny obiekt i zamienia go na float:

```python
>>> float('3.14')
3.14
```

:snake: Zobacz jak zachowa się funkcja `float`, gdy wywołasz ją z:
integerem, stringiem z samymi literami, stringiem z samymi cyframi.


## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się czym jest funkcja, jak ją definiować i wywoływać,
* poznaliśmy funkcje wbudowane `str`, `int` oraz `float`.

---

:checkered_flag: Następny rozdział: [Funkcja `print`](./08_funkcja_print.md) :checkered_flag:
