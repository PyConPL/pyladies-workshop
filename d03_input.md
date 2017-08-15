# Dodatek 3. Funkcja `input`

Pisząc program bardzo często oczekujemy, że jego użytkownik poda nam jakieś
dane: swoje imię i nazwisko, parametry liczbowe, czy inne wartości, które
wpłyną na przebieg programu.  Najprostszą metodą na pozyskanie takich
danych jest funkcja wbudowana `input`, która po wywołaniu zatrzymuje
działanie programu, czeka aż użytkownik wpisze coś i wciśnie enter, po
czym zwraca wpisany tekst w postaci stringa:

```python
print('Podaj swój wiek:')
wiek = input()
print('Masz {} lat'.format(wiek))
```

W powyższym przykładzie wypisujemy na ekran komunikat - prośbę o podanie
wieku - następnie pobieramy tę wartość od użytkownika i wypisujemy ją
w kolejnym komunikacie.

Pamiętaj, że tak otrzymana wartość zawsze będzie stringiem.  Jeżeli chcesz
zamienić ją na liczbę, możesz posłużyć się funkcją wbudowaną [`int`](https://docs.python.org/3/library/functions.html#int).

