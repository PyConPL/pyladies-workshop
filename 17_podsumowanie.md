# Podsumowanie

Dobiegamy do końca kursu, ale to jeszcze nie koniec warsztatów!  Czekają
na Ciebie jeszcze dodatkowe rozdziały - znajdziesz je w sekcji "Dodatki"
pod spisem treści. Poza tym mentorzy mają dla Ciebie jeszcze garść zadań.
Możesz też skorzystać z okazji i zadać mentorom tyle pytań na ile tylko
starczy czasu - między innymi dlatego zorganizowaliśmy te warsztaty!


## O czym nie powiedzieliśmy

Niestety czas na warsztaty jest ograniczony, więc i zakres tematów, jakie
poruszyliśmy, nie jest wyczerpujący.  Znasz już podstawy Pythona.  Możesz
już samodzielnie pisać własne programy, a czytanie cudzych nie będzie już
takie trudne.  Jednak na tym etapie często trafisz na kod, którego nie
zrozumiesz.  A może już teraz wiesz o tematach, które wydają się
interesujące, ale nie wiesz jak zacząć.  Dlatego przygotowaliśmy dla Ciebie
listę zagadnień, którą możesz potraktować jako kontynuację tych warsztatów.
Lista ta nie jest wyczerpująca, ale na pewno pomoże Ci jeszcze
lepiej poznać Pythona.  W każdym punkcie umieściliśmy odnośnik do strony,
która wyjaśnia dany temat.

* [Jeszcze więcej o wyjątkach i obsługiwaniu ich](https://docs.python.org/3.6/tutorial/errors.html)
* [Klasy, czyli programowanie zorientowane obiektowo](https://docs.python.org/3.6/tutorial/classes.html)
* [Dekoratory](https://docs.python.org/3/glossary.html#term-decorator)
* [Generatory](https://docs.python.org/3/glossary.html#index-17)
* [Listy składane](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Zbiory](https://docs.python.org/3/tutorial/datastructures.html#sets)


## Na koniec... `dir`

Kończąc pokażemy Ci jeszcze jedną, bardzo przydatną funkcję wbudowaną.
Nazywa się `dir`, przyjmuje jako argument dowolny obiekt i zwraca listę
nazw wszystkich metod i atrybutów tego obiektu:

```python
>>> d = {'a': 1}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

W powyższym przykładzie rozpoznasz na pewno kilka znajomych nazw, np.
`items` czy `values`, ale jak widzisz słowniki oferują znacznie więcej.
Zwróć uwagę na nazwy zaczynające i kończące się podwójnym znakiem
podkreślenia.  W taki sposób są nazywane atrybuty i metody, które nie są
przeznaczone dla użytkowników obiektu.  Zazwyczaj są to rzeczy używane
tylko wewnątrz danego obiektu.  Oczywiście tak czy inaczej można z nich
korzystać - po prostu zazwyczaj nie będą dla nas przydatne, więc warto
zainteresować się pozostałymi nazwami.

Co teraz zrobić z taką listą?  Jeżeli jakaś nazwa wydaje się oczywista,
możemy po prostu spróbować jej użyć - w najgorszym wypadku otrzymamy
komunikat o błędzie wyjaśniający co zrobiliśmy źle.  Możemy też - i to
polecamy - użyć funkcji `help`, która wyświetli dokumentację danego
obiektu:

```python
help(d.update)
```


## :checkered_flag: Koniec

Dziękujemy za udział w warsztatach!  Jeszcze raz zachęcamy do rozmowy
z mentorami - chętnie odpowiedzą na wszystkie pytania i wyjaśnią
niezrozumiałe tematy.

Jeżeli masz uwagi do tego kursu, podziel się nimi pisząc do autorów,
albo przekaż je mentorom.  Twoje zdanie jest dla nas bardzo ważne!

![programming is fun again](https://imgs.xkcd.com/comics/python.png)
