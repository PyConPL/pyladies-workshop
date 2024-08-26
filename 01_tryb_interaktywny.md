# Rozdział 1. Tryb interaktywny

Warsztaty zaczniemy od wyjaśnienia w jaki sposób będziemy programowali
w Pythonie.

## Zaczynamy!

### Obsługa trybu interaktywnego na replit.com

Jeśli posiadasz lokalnie zainstalowany interpreter Pythona, to możesz pominąć tę sekcję.

Jeśli nie posiadasz zainstalowanego lokalnie interpretera Pythona, to otwórz
[ten link](https://replit.com/languages/python3) w osobnej karcie przeglądarki.

Jeżeli nie posiadasz konta na stronie `replit.com` to będziesz musiał/a je
założyć.

Przejdź do [tego poradnika aby założyć konto](d06_replit.md).

Strona, którą widzisz, jest podzielona na dwie części:

* z lewej strony, na białym tle, jest **edytor** tekstu,
* z prawej strony widać konsolę (**Console**) oraz powłokę (**Shell**).

  ![Konsola i powłoka](obrazy/d06/krok_4.png)

Edytor pozwala stworzyć cały kod programu, a następnie uruchomić go przez
wciśnięcie przycisku "Run" (lub kombinacją klawiszy Ctrl + Enter).
Jeżeli program wypisze jakiś tekst, to zobaczymy go w konsoli.

Tryb interaktywny możemy aktywować przechodząc do zakładki **Shell** i uruchamiając
polecenie `python`. Wtedy zobaczymy znak zachęty `>>>`, który oznacza, że
możemy wpisać polecenie Pythona.

### Tryb interaktywny na własnym komputerze

Tryb interaktywny możemy aktywować uruchamiając w terminalu polecenie `python`.
Wtedy zobaczymy znak zachęty `>>>`, który oznacza, że
możemy wpisać polecenie Pythona.

## Tryb interaktywny - jak działa?

Gdy wpiszesz polecenie i wciśniesz Enter, tryb interaktywny wykonuje je i wypisuje jego wynik.
W ten sposób możesz programować i od razu oglądać rezultaty.

Praca z trybem interaktywnym jest wygodna, kiedy chcesz przetestować
działanie pojedynczej operacji lub kiedy nie masz pewności jakie operacje
chcesz wykonać.  Jeżeli już wiesz jaki program chcesz napisać, wtedy
łatwiej jest skorzystać z edytora.

Jest jeszcze jedna ważna różnica między trybem interaktywnym a edytorem:
tryb interaktywny po wykonaniu operacji zawsze wypisze jej wynik.  Edytor
zrobi to tylko jeżeli mu wydamy takie polecenie (poprzez instrukcję
`print`, o której opowiemy później).

Póki co będziemy korzystali z **trybu interaktywnego**, ponieważ będziemy
uczyli się pojedynczych instrukcji i oglądali ich rezultaty.  Nie bój się
eksperymentować z różnymi wariantami tych poleceń. W najgorszym wypadku
Python poinformuje Cię, że wpisanego kodu nie można wykonać.

## Znak zachęty

W przykładach kodu, które znajdziesz w kolejnych rozdziałach, wielokrotnie
zobaczysz ciąg znaków `>>>`.  Jest to **znak zachęty**.  Używamy go aby
odróżnić tekst, który należy wpisać w trybie interaktywnym od tekstu, który
interpreter Pythona sam wypisuje.  Jeżeli w jakiejś linijce przykładu
zobaczysz znak zachęty, to znaczy, że wszystko co następuje po znaku - aż
do końca linii - należy wpisać w trybie interaktywnym, a następnie wcisnąć
Enter.  Samego znaku zachęty nie wpisujemy!

## :pushpin: Podsumowanie

W tym rozdziale:

* otworzyliśmy stronę `repl.it`, na której możemy programować w **edytorze**
lub w **trybie interaktywnym** Pythona,
* dowiedzieliśmy się jak wygląda **znak zachęty** i że pokazuje nam kod,
który należy wpisać w trybie interaktywnym.

---

:checkered_flag: Następny rozdział: [Tekst](./02_tekst.md) :checkered_flag:
