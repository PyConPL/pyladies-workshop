`mkdir` tworzenie folder
`git clone [https://github.com/Misiek01/pyladies-workshop.git]` klonowanie repozytorium na Maku
`git clone 'https://github.com/Misiek01/pyladies-workshop.git' Klonowanie na Win

`git add` add Add file contents to the index. Files to add content from. Fileglobs (e.g. *.c) can be given to add all matching files. 

`git commit` Record changes to the repository. Important to use -m option and provide commitment message. Othervise terminal will be blocked

Metody operacji na Stringach 

`'Kubuś Puchatek'.lower()` funkcja zamieniajaca duze litery `string` na male
* `upper` - przeciwieństwo `lower`,
* `title` - zamienia każdą pierwszą literę każdego wyrazu z małej na
wielką,
* `strip` - usuwa spacje z lewej i prawej strony stringa (jeżeli
istnieją).
* `find` - wyszukuje w stringu podany łańcuch i zwraca numer znaku
(mówimy: indeks znaku), w którym ten łańcuch się zaczyna.  Zwróć uwagę,
że znaki numerowane są od zera
jako argument przyjmuje string i szuka go w stringu na jakim wywołaliśmy operację. Jeżeli łańcuch zostanie znaleziony, otrzymujemy numer znaku, od którego się zaczyna. W przeciwnym wypadku dostaniemy -1
Wielkość liter ma znaczenie. Pomylona duza z mala daje `-1`
Nalezy pamiętać, ze początek pozycjonowania to `0` dlatego literka `r` tak naprawdę ma pozycję 24 nie 23. Wazna jest interpretacja uzyskanych wyników 

* `replace`- przyjmuje dwa argumenty: stringi a i b. Kiedy wywołamy tę metodę na jakimś stringu, to wszystkie wystąpienia łacucha a w tym stringu zostaną zastąpione łańcuchem b.
Mozna `zastępować znaki: 'Ala ma kota'.replace(' ', '-')`, `zastąpić całe wyrazy: 'Ala ma kota'.replace('kota', 'psa')` lub `usunięcie ze stringa jakiegoś znaku 'Jan Kowalski'.replace('Kowalski', '')`

* `count`- przyjmuje jeden string jako argument i zwraca liczbę wystąpień tego łańcucha w stringu na jakim wykonaliśmy operację.
Metoda ta przydaje się, kiedy na przykład chcemy sprawdzić czy jakaś fraza powtarza się więcej niż raz w danym stringu:
`'Ala ma kota'.count('ma')` wynik `1`
`'Ala ma kota, a Ola ma psa'.count('ma')` wynik `2`

* `len`- Jedną z najbardziej przydatnych operacji, jaką możemy wykonać na stringu, jest sprawdzenie jego długości. Przykładowo, chcemy sprawdzić czy nie jest zbyt długi, albo chcemy sprawdzić który z dwóch stringów jest dłuższy. Długość stringa:`len('Kubuś Puchatek')`. `Len` nie jest metodą, czyli nie stosujemy notacji obiekt.metoda(). Jest tak, ponieważ sprawdzenie długości jakiegoś obiektu (w tym przypadku: stringa) jest na tyle popularną operacją, że w Pythonie stworzono osobną funkcję, która ją wykonuje

* `help`- Każda metoda zdefiniowana w Pythonie posiada dokumentację, która w kilku słowach opisuje jej działanie. Aby przeczytać tę dokumentację, należy wywołać funkcję help. Przykład: `help('jakiś string'.find)`

* liczby całkowite `integer` - `**` potęgowanie, `//` dzielenie całkowite, `%` reszta z dzielenia (modulo). Wynik operacji na liczbach całkowitych, moze dac wynik w liczbach rzeczywistych

* liczby rzeczywiste `float` - liczby "zmiennoprzecinkowe"

* operatory i kolejnosc: 
    1. `**` potegowanie 
    2. `*`, `/`, `//`, `%`	Mnożenie, dzielenie, dzielenie całkowite, modulo
    3. `+`. `-` Dodawanie i odejmowanie

`Błędy`:

`SyntaxError`   - Błąd składni 

`EOL`           - End Of Line, Komunikat sugeruję na miejsce błędu

`traceback`     - Pomaga zlokalizować miejsce problemu w kodzie. Uważnie przeczytać komunikat linijka po linijce. Wtedy dojdę co jest nie tak


`ZMIENNE`:

Aby poradzić sobie z problemem przechowania wyniku operacji, używamy zmiennych

Operację zmienna = wartość nazywamy przypisaniem. W wyniku przypisania Python tworzy zmienną, która otrzymuje wartość. Jeżeli wartość jest operacją (np. dodawaniem), to najpierw jest obliczany jej rezultat, a następnie zostaje on przypisany do zmiennej

Ograniczenia na znaki użyte do nazwania zmiennej:

*   litery od a do z (małe) oraz od A do Z (wielkie)
*   cyfry
*   znak (podłoga)

Wszystkie pozostałe znaki są niedozwolone. Co istotne, nazwa nie może zaczynać się od cyfry
#1abc = 0
#print(1abc) # SyntaxError: invalid syntax

W każdej chwili możemy zmienić wartość zmiennej:

>>> x = 'Ala ma kota'
>>> x
'ala ma kota'
>>> x = 'kot ma Alę'
>>> x

Na zmiennych można zastosować metody (zpoprzednich cw) takie jak `find`, `upper`, `title` itp

`FUNKCJE`




