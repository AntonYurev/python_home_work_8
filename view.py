import operation


def start():
    while True:
        start = input("Справочник сотрудников фирмы. Продолжить или завершить? (Y/N): ")
        if start == "Y" or start == "y":
            print("1 - Сделать запись.  2 - Поиск.")
            vibor = int(input("Ваш выбор: "))
            if vibor == 1:
                operation.record()
            elif vibor == 2:
                print("Поиск по фамилии - 1. Поиск по имени - 2")
                vibor1 = int(input("Ваш выбор: "))
                operation.search(vibor1)
            else : 
                print("Сделайте правильный выбор.") 
        elif start == "N" or start == "n":
            print("Всего хорошего")
            break
        else : 
            print("Сделайте правильный выбор.")