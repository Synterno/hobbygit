# SmartBeekeeper v.0.5, ПО для мониторинга пасеки
import sqlite3
from colorama import init, Fore, Style

init(autoreset=True)
db = sqlite3.connect('hive.db')
sql = db.cursor()

# СОЗДАНИЕ ТАБЛИЦЫ В БД
sql.execute("""CREATE TABLE IF NOT EXISTS beehive (
    hive_number INT,
    breed TEXT,
    str TEXT,
    queen_exist TEXT,
    queen_age INT,
    queen_breed TEXT,
    bee_dis TEXT,
    last_work TEXT,
    coming_work TEXT,
    comment TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS hivenote(
    hive_number INT,
    last_work TEXT
)""")

db.commit()


# ДОБАВИТЬ НОВЫЙ УЛЕЙ
def add_hive():
    try:
        hive_number = int(input(Style.BRIGHT +
        '''Номер пчелосемьи: 
        555 - для отмены: '''))
        if hive_number == 555:
            print(Fore.YELLOW + 'Операция отменена.')
            run()
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        add_hive()
    sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{hive_number}'")
    if sql.fetchone() is None:
        hive_breed = input(Style.BRIGHT + 'Порода пчелосемьи: ')
        hive_str = input(Style.BRIGHT + 'Сила пчелосемьи: ')
        queen_exist = input(Style.BRIGHT + 'Наличие матки: ')
        queen_age = input(Style.BRIGHT + 'Возраст матки: ')
        queen_breed = input(Style.BRIGHT + 'Порода матки: ')
        bee_dis = input(Style.BRIGHT + 'Заболевания: ')
        last_work = input(Style.BRIGHT + 'Проделанная работа: ')
        coming_work = input(Style.BRIGHT + 'Предстоящая работа: ')
        comment = input(Style.BRIGHT + 'Комментарий: ')

        sql.execute(f"INSERT INTO beehive VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (hive_number, hive_breed, hive_str, queen_exist, queen_age, queen_breed, bee_dis, last_work, coming_work, comment))
        sql.execute(f'INSERT INTO hivenote VALUES (?, ?)', (hive_number, last_work))
        db.commit()
        print(Fore.GREEN + 'База данных успешно обновлена!')
        for values in sql.execute('SELECT * FROM beehive'):
            print(values)
        next_step = int(input(Fore.YELLOW +
            """Введите: 
             1 - Добавить,
             2 - Редактировать,
             3 - Удалить, 
             4 - Выход: """))
        if next_step == 1:
            add_hive()
        elif next_step == 2:
            change()
        elif next_step == 3:
            delete()
        elif next_step == 4:
            print(Fore.GREEN + 'Всего доброго!')
        else:
            print(Fore.RED + 'Некорректный ответ')
            run()
    else:
        print(Fore.RED + 'Такая запись уже имеется!')
        for values in sql.execute('SELECT * FROM beehive'):
            print(values)
        false_add = int(input(Fore.YELLOW +
            """Введите:
             1 - Другой номер,
             2 - Редактировать,
             3 - Выход: """))
        if false_add == 1:
            add_hive()
        elif false_add == 2:
            change()
        elif false_add == 3:
            print(Fore.GREEN + 'Всего доброго!')
        else:
            print(Fore.RED + 'Некорректный ответ.')
            run()


# ОБНОВЛЕНИЕ ПОСЛЕДНЕЙ РАБОТЫ
def update_last_work():
    try:
        hive_numb = int(input(Fore.YELLOW +
        '''Укажите номер улья для редактирования: 
        555 - для отмены: '''))
        if hive_numb == 555:
            print(Fore.YELLOW + 'Операция отменена.')
            run()
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        update_last_work()
    sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{hive_numb}'")
    if sql.fetchone() is None:
        print(Fore.RED + 'Улей с таким номером не существует.')
        add = int(input(Fore.YELLOW +
            """Добавить улей в базу?:
             1 - Да,
             2 - Нет, 
             3 - Выход: """))
        if add == 1:
            add_hive()
        elif add == 2:
            print(Fore.RED + 'Введите существующий номер улья.')
            update_last_work()
        elif add == 3:
            print(Fore.GREEN + 'Всего доброго!')
        else:
            print(Fore.RED + 'Некорректный ответ.')
            run()
    else:
        lw = input(Fore.YELLOW + 'Проделанная работа: ')
        cw = input(Fore.YELLOW + """Предстоящая работа: """)
        comm = input(Fore.YELLOW + """Комментарий: """)
        sql.execute(f"UPDATE beehive SET last_work = '{lw}' WHERE hive_number = '{hive_numb}'")
        sql.execute(f"UPDATE beehive SET coming_work = '{cw}' WHERE hive_number = '{hive_numb}'")
        sql.execute(f"UPDATE beehive SET comment = '{comm}' WHERE hive_number = '{hive_numb}'")
        sql.execute(f"UPDATE hivenote SET last_work = last_work || ' - ' ||'{lw}' WHERE hive_number = '{hive_numb}'")
        db.commit()
        print(Fore.GREEN + 'Запись успешно обновлена!')
        for values in sql.execute('SELECT * FROM beehive'):
            print(values)
        run()

# ОБНОВЛЕНИЕ СИЛЫ СЕМЬИ И ИНФЫ ПО МАТКЕ
def update_str():
    try:
        hive_numb = int(input(Fore.YELLOW +
        '''Укажите номер улья для редактирования: 
        555 - для отмены: '''))
        if hive_numb == 555:
            print(Fore.YELLOW + 'Операция отменена.')
            run()
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        update_str()
    sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{hive_numb}'")
    if sql.fetchone() is None:
        print(Fore.RED + 'Улей с таким номером не существует.')
        add = int(input(Fore.YELLOW +
            """Добавить улей в базу?:
             1 - Да,
             2 - Нет, 
             3 - Выход: """))
        if add == 1:
            add_hive()
        elif add == 2:
            print(Fore.RED + 'Введите существующий номер улья.')
            update_last_work()
        elif add == 3:
            print(Fore.GREEN + 'Всего доброго!')
        else:
            print(Fore.RED + 'Некорректный ответ.')
            run()
    else:
        str = input(Fore.YELLOW + """Сила семьи: """)
        qe = input(Fore.YELLOW + """Наличие матки: """)
        qa = input(Fore.YELLOW + """Возраст матки: """)
        qb = input(Fore.YELLOW + """Порода матки: """)
        sql.execute(f"UPDATE beehive SET str = '{str}' WHERE hive_number = '{hive_numb}'")
        sql.execute(f"UPDATE beehive SET queen_exist = '{qe}' WHERE hive_number = '{hive_numb}'")
        sql.execute(f"UPDATE beehive SET queen_age = '{qa}' WHERE hive_number = '{hive_numb}'")
        sql.execute(f"UPDATE beehive SET queen_breed = '{qb}' WHERE hive_number = '{hive_numb}'")
        db.commit()
        print(Fore.GREEN + 'Запись успешно обновлена!')
        for values in sql.execute('SELECT * FROM beehive'):
            print(values)
        run()


# УДАЛЕНИЕ ЗАПИСЕЙ ИЗ БД
def delete():
    try:
        delete_hive = int(input(Fore.YELLOW +
        '''Укажите номер улья, который хотите удалить: 
        555 - для отмены: '''))
        if delete_hive == 555:
            print(Fore.YELLOW + 'Операция отменена.')
            run()
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        delete()
    sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{delete_hive}'")
    if sql.fetchone() is None:
        print(Fore.RED + 'Такого улья не существует.')
        delete_return = int(input(Fore.YELLOW +
            """Введите: 1 - Удалить другой, 
             2 - Отмена: """))
        if delete_return == 1:
            delete()
        elif delete_return == 2:
            run()
        else:
            print(Fore.RED + 'Некорректный ответ')
            run()
    else:
        delete_confirm = int(input(Fore.RED +
            """Вы уверены что хотите удалить улей?: 
             1 - Да, 
             2 - Нет: """))
        if delete_confirm == 1:
            sql.execute(f'DELETE FROM beehive WHERE hive_number = {delete_hive}')
            sql.execute(f'DELETE FROM hivenote WHERE hive_number = {delete_hive}')
            db.commit()
            print(Fore.GREEN + 'Запись успешно удалена')
            for values in sql.execute('SELECT * FROM beehive'):
                print(values)
            next_step = int(input(Fore.YELLOW +
                """Введите: 
                 1 - Удалить ещё, 
                 2 - Назад, 
                 3 - Выход: """))
            if next_step == 1:
                delete()
            elif next_step == 2:
                run()
            elif next_step == 3:
                print(Fore.GREEN + 'Всего хорошего!')
            else:
                print(Fore.RED + 'Некорректный ответ.')
                run()
        elif delete_confirm == 2:
            print(Fore.RED + 'Удаление отменено.')
            run()
        else:
            print(Fore.RED + 'Некорректный ответ.')
            run()


# ЗАБОЛЕВАНИЯ
def dis():
    try:
        hive_dis = int(input(Fore.YELLOW +
        '''Укажите номер улья с заболеванием: 
        555 - для отмены: '''))
        if hive_dis == 555:
            print(Fore.YELLOW + 'Операция отменена.')
            run()
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        dis()
    sql.execute(f"SELECT bee_dis FROM beehive WHERE hive_number = '{hive_dis}'")
    if sql.fetchone() is None:
        print(Fore.RED + 'Улей с таким номером не существует.')
        add = int(input(Fore.YELLOW +
            """Добавить улей в базу?:
             1 - Да,
             2 - Нет, 
             3 - Выход: """))
        if add == 1:
            add_hive()
        elif add == 2:
            print(Fore.RED + 'Введите существующий номер улья.')
            dis()
        elif add == 3:
            print(Fore.GREEN + 'Всего доброго!')
        else:
            print(Fore.RED + 'Некорректный ответ.')
            run()
    else:
        bee_diseas = input(Fore.YELLOW + 'Укажите заболевание: ')
        sql.execute(f"UPDATE beehive SET bee_dis = '{bee_diseas}' WHERE hive_number = '{hive_dis}'")
        print(Fore.GREEN + 'Запись успешно обновлена!')
        for values in sql.execute('SELECT * FROM beehive'):
            print(values)
        db.commit()
        run()


def change():
    try:
        what = int(input(Fore.YELLOW + """
        Что будем редактировать:
        1 - Силу семьи и информацию о матке;
        2 - Работу в улье;
        3 - Назад: """))
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        change()
    if what == 1:
        update_str()
    elif what == 2:
        update_last_work()
    elif what == 3:
        run()
    else:
        print(Fore.RED + 'Некорректный ответ.')
        change()


# ЗАПУСК
def run():
    try:
        start = int(input(Fore.YELLOW +
            """Введите:
             1 - Добавить, 
             2 - Редактировать,
             3 - Удалить,
             4 - Заболевания,
             5 - Дневник, 
             6 - Выход: """))
    except:
        print(Fore.RED + 'Некорректный ответ, введите числовое значение.')
        run()
    if start == 1:
        add_hive()
    elif start == 2:
        change()
    elif start == 3:
        delete()
    elif start == 4:
        dis()
    elif start == 5:
        for values in sql.execute(f'SELECT * FROM hivenote'):
            print(values)
        run()
    elif start == 6:
        print(Fore.GREEN + 'Всего доброго!')
    else:
        print(Fore.RED + 'Некорректный ответ')
        false_start = int(input(Fore.YELLOW +
            """Введите:
             1 - Вернуться, 
             2 - Выход: """))
        if false_start == 1:
            run()
        elif false_start == 2:
            print(Fore.GREEN + 'Всего доброго!')
        else:
            print(Fore.RED + 'Некорректный ответ')
            run()


for values in sql.execute('SELECT * FROM beehive'):
    print(values)
run()
