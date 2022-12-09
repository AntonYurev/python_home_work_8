import csv

def record():
    print('запись:')
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    position = input('Введите должность: ')
    s = surname+ ',' +name+','+phone+','+position
    print(f'Вы ввели: {s}')
    s = s.split()
    vibor = input('Если все верно нажмите 1, если исправить - 2: ')
    if vibor == '1':
        with open('catalog.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(s)
    else :
        record()


def search(n):
    count=0
    if n == 1:
        print('поиск по фамилии: ')
        surname = input('Введите фамилию: ')
        for i in open('catalog.csv', encoding='utf-8'):
            if surname in i:
                print('Искомые данные: ' + i)
                count +=1
        if count == 0:
            print('Такой фамилии нет.')
    elif n == 2:
        print('поиск по имени: ')
        surname = input('Введите имя: ')
        for i in open('catalog.csv', encoding='utf-8'):
            if surname in i:
                print('Искомые данные: ' + i)
                count +=1
        if count == 0:
            print('Такого имени нет.')
    else : search(1)
