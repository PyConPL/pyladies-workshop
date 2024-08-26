# Rozdział 5. Błędy

W tym rozdziale:

* dowiesz się, czym są **wyjątki**,
* nauczysz się czytać komunikaty o błędach.

## Wyjątki

Tworząc programy nigdy nie jesteśmy w stanie przewidzieć wszystkich
sytuacji, jakie mogą się wydarzyć.  Czasami użytkownik poda dane, których
nasz program nie jest w stanie przetworzyć: na przykład spodziewaliśmy
się liczby, a dostaliśmy tekst.  Innym razem pomylimy się i wywołamy
na jakimś obiekcie metodę, która nie istnieje.  Na każdą tego typu sytuację
Python zareaguje zgłaszając błąd.

Kiedy to się zdarzy, działanie programu zostanie przerwane i wyświetlony
zostanie komunikat, dzięki któremu dowiemy się, na czym polegała nasza
pomyłka, co pozwoli nam poprawić kod programu, żeby uniknąć tego samego
problemu w przyszłości.

Słowa "błąd" czy "problem" są bardzo ogólne, ponieważ mogą dotyczyć również
rzeczy, na które jako programiści nie mamy wpływu.  Dlatego posługujemy się
terminem **wyjątek**, który określa tylko te wypadki, jakie język
programowania może obsłużyć - czyli takie, na jakie nasze programy mogą
zareagować.

W praktyce wyjątek to sytuacja, w której Python zatrzymał wykonywanie
programu, ponieważ napotkał *wyjątkową* sytuację, której sam nie potrafił
obsłużyć.  Mówi się, że program **rzucił wyjątek**.  Kiedy tak się stanie,
rolą programisty jest dostosowanie programu w taki sposób, aby
w przyszłości podobna sytuacja nie skutkowała zatrzymaniem.

Czym są wyjątkowe sytuacje o których wspomnieliśmy?  Może to być próba
wykonania operacji, której Python nie potrafi zrealizować, na przykład
dodanie liczby do tekstu.  Albo błąd "za mało miejsca na dysku twardym"
podczas zapisywania jakiegoś pliku.  Nie sposób wymienić wszystkie takie
możliwości - z czasem poznasz zestaw najczęściej występujących wyjątków
i nauczysz się przewidywać, jakie operacje mogły je spowodować.

## Jak czytać komunikaty o błędach i wyjątkach

Spróbujmy wywołać błąd i zobaczyć, jak zachowa się nasz program.
Pamiętasz, jak informowaliśmy o tym, że stringi wstawiamy w pojedynczy lub
podwójny cudzysłów, ale musisz pamiętać, żeby cudzysłów zamykający był taki
sam jak otwierający? Zróbmy eksperyment i sprawdźmy, co się stanie, kiedy
złamiemy tę zasadę.

```python
>>> 'ala ma kota"
  File "<stdin>", line 1
    'ala ma kota"
    ^
SyntaxError: unterminated string literal (detected at line 1)
```

Jak widzisz, zamiast wyświetlić tę frazę, Python zgłosił błąd.
Przeczytajmy go linijka po linijce.

* Na samym początku widzimy zawsze wiadomość
`Traceback (most recent call last):`.  Słowem "traceback" określa się listę
operacji, których wykonanie spowodowało błąd.  W tym przypadku wykonana
została tylko jedna operacja (zwrócenie wpisanej frazy), ale w przyszłości
spotkasz się z sytuacjami, w których wyjątek czy błąd został rzucony wskutek
wykonania całego ciągu poleceń.  Python zawsze pokazuje cały traceback, aby
programista mógł zrozumieć, co poszło nie tak.  Tekst `most recent call last`
informuje, że ostatnia operacja na liście została wykonana najpóźniej
spośród wszystkich.
* `File "python", line 1` to właśnie traceback. W naszym
przypadku jest to tylko jedna linijka.  Widzimy tutaj opis miejsca,
w którym wystąpił błąd.
* Ostatnia linijka zawiera najważniejszą informację, czyli bezpośrednią
przyczynę błędu.  Zaczyna się od typu wyjątku.  W tym przypadku to
`SyntaxError` - błąd składni.  Typ błędu można rozumieć jako kategorię: nie
mówi on, czego dokładnie dotyczył błąd, ale pozwala zaklasyfikować różne
wyjątki, aby łatwiej było je zrozumieć.  `SyntaxError` oznacza błąd w składni
ciągu znaków, które powinny po sobie następować zgodnie ze składnią języka.
Rozszyfrujmy jeszcze skrót EOL - end of line, koniec linii. Po takim
komunikacie wiemy trochę więcej na temat tego, któremu fragmentowi naszego kodu się
dokładnie przyjrzeć. Odkrycie powodu, dlaczego nasz kod nie działa, wciąż może
być niełatwą zagadką.

Tworząc bardziej zaawansowane programy spotkasz się z jeszcze dłuższymi
komunikatami o błędach.  Nie zniechęcaj się tym: każdy wyjątek sprowadza
się do tylko jednej niepoprawnej operacji, a traceback, nieważne jak długi,
pomoże Ci zlokalizować przyczynę niepowodzenia.  Jeżeli mimo wszystko nie
będziesz w stanie zrozumieć, dlaczego Twój program przestał działać, wklej
ostatnią linijkę komunikatu do wyszukiwarki internetowej.  Jest bardzo
możliwe, że ktoś już kiedyś spotkał się z takim problemem i znalazł
rozwiązanie.

Często, wyjątki są sposobem komunikacji pomiędzy programem, który piszesz a
użytkownikiem, który go uruchamia.  Dzięki nim użytkownik dowiaduje się, co
poszło nie tak. Poniżej możemy zobaczyć jak pomiędzy wersjami Pythona zmienił się
komunikat o tym samym błędzie.
W wersji 3.7 Python zwracał błąd `SyntaxError: EOL while scanning string literal`,
i bez wiedzy co w żargonie programistycznym oznacza EOL, trudno byłoby zrozumieć
co jest problemem w przekazanym stringu.
W wersji 3.12 Python zwraca błąd
`SyntaxError: unterminated string literal (detected at line 1)`,
co jest bardziej zrozumiałe, bo informuje nas, że po prostu przekazany string nie został
zamknięty.

```python
# Python w wersji 3.7
>>> 'ala ma kota"
Traceback (most recent call last):
  File "python", line 1
    'ala ma kota"
                ^
SyntaxError: EOL while scanning string literal

# Python w wersji 3.12
>>> 'ala ma kota"
  File "python", line 1
    'ala ma kota"
    ^
SyntaxError: unterminated string literal (detected at line 1)
```

:snake: Wywołaj błędy i przeczytaj ze zrozumieniem wyjątki spowodowane
następującymi operacjami: dzielenie przez zero; wywołanie metody lower() na
dowolnej cyfrze; wywołanie na dowolnym stringu metody, która nie istnieje;
wykonanie kodu, który nie ma sensu (możesz wpisać losowy ciąg znaków).

## :pushpin: Podsumowanie

W tym rozdziale:

* dowiedzieliśmy się, czym jest **wyjątek** i jak czytać jego treść.

---

:checkered_flag: Następny rozdział: [Zmienne](./06_zmienne.md) :checkered_flag:
