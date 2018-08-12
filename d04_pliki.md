# Dodatek 4. Operacje na plikach

Często źródłem danych w programach są pliki.  Jeżeli plik zawiera tekst,
czyli znaki, które możemy wyświetlić na ekranie, to nazywamy go **plikiem
tekstowym**.  Taki plik możemy odczytać w edytorze tekstu, na przykład
w Notatniku.  Istnieją również pliki, których treści nie interpretujemy
jako tekst, na przykład obrazy.  Nazywamy je **plikami binarnymi**.

Oba rodzaje plików możemy odczytywać i zapisywać w Pythonie, jednak
w tym artykule skupimy się na plikach tekstowych.  Kiedy nauczysz się
pracować z nimi, operacje na plikach binarnych nie będą już dla Ciebie
stanowiły żadnego problemu.


## Ścieżka pliku

Najważniejszym atrybutem pliku jest jego **ścieżka**, która mówi w jakim
miejscu w strukturze katalogów i pod jaką nazwą się znajduje.  Przykładowo,
jeżeli w systemie Windows zalogujesz się jako użytkownik "Ala" i utworzysz
plik "kot.txt" w katalogu "Moje Dokumenty", to ścieżka tego pliku będzie
najprawdopodobniej wyglądała tak: `C:\Users\Ala\Documents\kot.txt`.

Ścieżki w Pythonie trzymamy w stringach, na przykład:

```python
>>> sciezka_pliku_kot = 'C:\Users\Ala\Documents\kot.txt'
>>> print(sciezka_pliku_kot)
C:\Users\Ala\Documents\kot.txt
```

W powyższym przykładzie zdefiniowaliśmy **ścieżkę bezwzględną**, czyli
taką, która dokładnie określa katalog w jakim znajduje się plik
(`C:\Users\Ala\Documents`).  Jeżeli odnosimy się do pliku względem
katalogu, w którym znajduje się nasz program, możemy zdefiniować **ścieżkę
względną**.  Na przykład możemy podać tylko nazwę pliku: `kot.txt`.  Wtedy
Python uzna, że szukamy pliku w tym samym katalogu co program.  Możemy też
powiedzieć, że plik znajduje się w katalogu "wyżej": `..\kot.txt`.

Niezależnie od wybranej metody, aby operować na pliku będziemy potrzebowali
jego ścieżki.


## Czytanie pliku

Dostęp do pliku daje nam funkcja wbudowana `open`, która jako argument
przyjmuje ścieżkę:

```python
>>> plik = open(sciezka)
```

Gdy zdefiniujemy sobie plik, możemy odczytać całą jego treść wywołując
metodę `read`:

```python
>>> dane = plik.read()
>>> print(dane)
zawartość pliku
```

Możemy również iterować po pliku, linijka po linijce:

```python
for linia in plik:
    print(linia)
```

Gdy odczytamy plik, ponowna próba odczytu zwróci nam pusty string.  Dzieje
się tak, ponieważ Python trzyma informację o miejscu w którym skończyliśmy
odczyt pliku i kolejne odczyty zaczyna od tego miejsca.  Jeżeli ta pozycja
to koniec pliku, ponowna próba odczytu nic nie zwróci.  Chcąc przeczytać
plik od nowa musimy wywołać metodę `seek` z argumentem `0`, co przestawi
pozycję odczytu na sam początek:

```python
>>> plik = open('kot.txt')
>>> plik.read()
'ala ma kota'
>>> plik.read()
''
>>> plik.seek(0)
>>> plik.read()
'ala ma kota'
>>> plik.read()
''
```


## Pisanie do pliku

Otwierając plik funkcją `open` możemy zdecydować, czy będziemy wykonywali
na nim odczyt czy zapis.  Domyślnie Python zakłada odczyt.  Jeżeli chcemy
wprost określić **tryb** (*mode*) pracy z plikiem, musimy przekazać drugi
argument, który powinien być stringiem.  Jeżeli wybierzemy `'r'` (*read*),
to plik będziemy mogli tylko odczytywać.  Jeżeli `'w'` (*write*),
to możliwy będzie tylko zapis.  Dostępnych trybów jest więcej, o wszystkich
przeczytasz w [dokumentacji metody `open`](https://docs.python.org/3/library/functions.html#open).

Po otwarciu pliku w trybie zapisu, możemy wpisać do pliku tekst metodą
`write`:

```python
>>> plik = open('kot.txt', 'w')
>>> plik.write('ala ma kota')
```

Jeżeli przed otwarciem pliku znajdował się w nim jakiś tekst, to po
wywołaniu metody `write` zostanie on **nadpisany**.  Jednak kolejne zapisy
na już otwartym pliku spowodują, że tekst będzie dopisywany na końcu.

```python
>>> sciezka = 'kot.txt'
>>> open(sciezka).read()
'na początku był taki tekst'
>>> plik = open(sciezka, 'w')
>>> plik.write('teraz nadpiszemy')
>>> plik.write(' tamten tekst')
>>> plik.close()
>>> open(sciezka).read()
'teraz nadpiszemy tamten tekst'
```

Zwróć uwagę, że w powyższym przykładzie po zapisaniu tekstu wywołaliśmy
metodę `close`.  W ten sposób zamknęliśmy plik, powodując zachowanie danych
na dysku.  Gdybyśmy tego nie zrobili, wywołanie metody `read` zwróciłoby
pierwotną zawartość pliku.  Metodę `close` należy stosować jeżeli po
zapisie chcemy ponownie odczytać ten sam plik.  W przeciwnym wypadku Python
sam zadba o zamknięcie pliku: zrobi to jeżeli zakończy się funkcja,
w której otworzyliśmy plik albo gdy program zakończy swoje działanie.


## Znak nowej linii

Operując na plikach tekstowych natkniemy się na **znak nowej linii**,
który w Pythonie jest reprezentowany jako string o treści `\n` (ukośnik
i litera "n").  Oznacza on miejsce, w którym kończy się linia tekstu.
Sam znak nie ma w sobie nic szczególnego, jest po prostu znakiem jak `a`
czy `7`.  Natomiast przyjmuje się, że znak nowej linii ma specjalne
znaczenie, aby umożliwić podział tekstu na osobne linie.  Dlatego też
jest on traktowany inaczej niż inne znaki, np. funkcja `print` zastąpi
go przejściem do nowej linii.  Co istotne, znak ten nie jest bezpośrednio
związany z plikami - może być częścią dowolnego stringa.

```python
>>> s = 'pierwsza linia\ndruga linia'
>>> print(s)
pierwsza linia
druga linia
```

