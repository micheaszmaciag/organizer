from organizer import organizer


mojorganizer = organizer('Foo')
while True:

    print('Co chcesz zrobić?:')
    print('1- Dodać Notatkę')
    print('2- Dodać Wizytówkę')
    print('3- Dodać Kupon Rabatowe')
    print('4- Wyświetlić notatki')
    print('5- Wyświetlić wizytówki')
    print('6- Wyświetlić Kupony Rabatowe')
    print('7- Usuń Notatkę')
    print('8- Usuń Wizytówkę')
    print('9- Usuń Kupon Rabatowy')
    print('0- Zamknąć organizer')

    x = input('Twój Wybór: ')

    if x == '0':
        break
    if x == '1':
        mojorganizer.dodajNotatke()
    if x == '2':
        mojorganizer.dodajWizytowke()
    if x == '3':
        mojorganizer.dodajKupon()
    if x == '4':
        mojorganizer.wyswietlNotatke()
    if x == '5':
        mojorganizer.wyswietlWizytowki()
    if x == '6':
        mojorganizer.wyswietlKupon()
    if x == '7':
        mojorganizer.usunNotatke()
    if x == '8':
        mojorganizer.usunWizytowke()
    if x == '9':
        mojorganizer.usunKupon()