from przedmiot import notatka,wizytowka,kuponRabatowy

class organizer:

    __wlasciel = ''
    __bazaDanych = []

    def __init__(self,wlasciciel):
        self.wlasciel = wlasciciel

    def dodajNotatke(self):
        priorytet = input('Priorytet:')
        tytul = input('Tytuł:')
        tresc = input('Treść:')
        id = input('ID ')

        nowaNotatka = notatka (priorytet,tytul,tresc,id)
        self.__bazaDanych.append(nowaNotatka)

    def usunNotatke(self):

        for i in self.__bazaDanych:
            if i.typ == 'notatka':
                self.__bazaDanych.remove(i)


    def dodajWizytowke(self):
        priorytet = input('Priorytet:')
        imie = input('Imię:')
        nazwisko = input('Nazwisko:')
        telefon = input('Nr Telefonu')

        nowaWizytowka = wizytowka(priorytet,imie,nazwisko,telefon)
        self.__bazaDanych.append(nowaWizytowka)

    def usunWizytowke(self):
        for i in self.__bazaDanych:
            if i.typ == 'wizytowka':
                self.__bazaDanych.remove(i)

    def dodajKupon(self):
        priorytet = input('Priorytet')
        imie = input('imię')
        nazwisko = input('nazwisko')
        telefon = input('nr telefonu')
        wartosc = input('podaj wartosc kuponu')

        nowyKupon = kuponRabatowy(priorytet,imie,nazwisko,telefon,wartosc)
        self.__bazaDanych.append(nowyKupon)

    def usunKupon(self):
        for i in self.__bazaDanych:
            if i.typ == 'kuponrabatowy':
                self.__bazaDanych.remove(i)






    def wyswietlNotatke(self):
        print('lista notatek')
        for i in self.__bazaDanych:
            if i.typ == 'notatka':
                print(i)

    def wyswietlWizytowki(self):
        print('lista wizytówek')
        for i in self.__bazaDanych:
            if i.typ == 'wizytowka':
                print(i)

    def wyswietlKupon(self):
        print('lista kuponów')
        for i in self.__bazaDanych:
            if i.typ == 'kuponrabatowy':
                print(i)







