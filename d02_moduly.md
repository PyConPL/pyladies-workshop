# Dodatek 2. Moduły

Jak wspomnieliśmy w rozdziale ["Biblioteka standardowa"](./16_biblioteka_standardowa.md),
każdy może utworzyć własny moduł (bibliotekę) do Pythona i udostępniać
go innym, lub po prostu używać go w różnych projektach.  Poniżej
przeczytasz jak tworzyć moduły i w jaki sposób z nich korzystać.


## Pisanie modułu

Jeżeli masz na swoim komputerze [program IDLE](./d01_instalacja_pythona.md'),
to pewnie wiesz już, że kod programów napisanych w Pythonie jest zapisywany
w plikach z rozszerzeniem `.py`.  Jest to konwencja, która pozwala w łatwy
sposób odróżnić kod Pythona od innych plików, które go nie zawierają.

Każdy plik z rozszerzeniem `.py` jest jednocześnie programem, który możemy
uruchomić w Pythonie.  Innymi słowy: jeżeli uruchomimy Pythona i otworzymy
w nim plik z rozszerzeniem `.py`, to kod zawarty w tym pliku zostanie
wykonany.

Równocześnie każdy plik z rozszerzeniem `.py` jest też modułem.  Oznacza
to, że możemy go zaimportować w innym pliku instrukcją `import` i w ten
sposób uzyskać dostęp do wszystkich obiektów w nim zdefiniowanych: funkcji,
zmiennych itd.

Podsumowując: aby napisać moduł wystarczy umieścić dowolny kod w pliku
z rozszerzeniem `.py`.  Każdy taki plik może być potencjalnie wykorzystany
jako moduł.


## Importowanie modułów

Gotowy moduł możemy wykorzystać w dowolnym innym programie lub module,
importując go tam.  Ważne jest, aby oba pliki znajdowały się **w tym
samym katalogu**, w przeciwnym wypadku Python rzuci wyjątek `ImportError`.

Moduł importujemy instrukcją `import`, w której podajemy jego nazwę, która
jest taka sama jak nazwa pliku w którym go zapisaliśmy, ale bez
rozszerzenia `.py`.

Załóżmy, że utworzyliśmy plik o nazwie `funkcje.py` i zapisaliśmy w nim
taki kod:

```python
def suma(a, b):
    return a + b
```

Teraz w tym samym katalogu możemy utworzyć plik `obliczenia.py` i wpisać
w nim następujący kod:

```python
import funkcje

print(funkcje.suma(2000, 17))
```

Jeżeli uruchomimy program `obliczenia.py`, to na ekran zostanie wypisana
liczba `2017`.


## Zastosowanie modułów

Moduły to jeden z najpotężniejszych mechanizmów w Pythonie.  Pozwalają
podzielić programy na logicznie odseparowane fragmenty.  Przykładowo,
w jednym module możemy umieścić wszystkie funkcje odpowiedzialne za
obliczenia matematyczne, w drugim funkcje wypisujące dane na ekran,
a w trzecim połączyć wszystko w całość korzystając z dwóch pozostałych
modułów.

Pisząc programy zawsze miej na uwadze, że podział na moduły zwiększa
czytelność Twojego kodu.  Również Tobie łatwiej będzie wrócić do programu,
którego kod został w taki sposób uporządkowany.

