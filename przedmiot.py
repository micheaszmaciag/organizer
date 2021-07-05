from abc import ABC, abstractmethod


class przedmiot(ABC):

    def __init__(self, typ, priorytet):
        self.typ = typ
        self.priorytet = priorytet

    @abstractmethod
    def __str__(self):
        pass


class notatka(przedmiot):

    def __init__(self, priorytet, tytul, tresc, id):
        super().__init__('notatka', priorytet)
        self.tytul = tytul
        self.tresc = tresc
        self.id = id

    def __str__(self):
        info = self.typ + '\n' + 'Priorytet: ' + self.priorytet + '\n'
        info += self.tytul + '\n'
        info += self.tresc + '\n'
        info += self.id + '\n'
        return info


class wizytowka(przedmiot):

    def __init__(self, priorytet, imie, nazwisko, telefon):
        super().__init__('wizytowka', priorytet)
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def __str__(self):
        info = self.typ + 'Priorytet' + self.priorytet + '\n'
        info += self.imie + ' ' + self.nazwisko + '\n'
        info += self.telefon + '\n'
        return info


class kuponRabatowy(przedmiot):
    def __init__(self, imie, nazwisko, telefon, wartosc, priorytet):
        super().__init__('kuponrabatowy', priorytet)
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.wartosc = wartosc

    def __str__(self):
        info = self.typ + '\n' + 'Priorytet:' + self.priorytet + '\n'
        info += self.imie + ' ' + self.nazwisko + '\n'
        info += self.telefon + '\n'
        info += self.wartosc + '\n'
        return info
