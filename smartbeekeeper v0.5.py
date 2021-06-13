# SmartBeekeeper v.0.5
import sqlite3

db = sqlite3.connect('hive.db')
sql = db.cursor()

class Hive():

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

    def add_hive():
        try:
            hive_number = int(input('hive_number: '))
        except:
            raise TypeError
            add_hive()
        sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{hive_number}'")
        if sql.fetchone() is None:
            hive_breed = input('breed: ')
            hive_str = input('str: ')
            queen_exist = input('queen_exist: ')
            queen_age = input('queen_age: ')
            queen_breed = input('queen_breed: ')
            bee_dis = input('bee_dis: ')
            last_work = input('last_work: ')
            coming_work = input('coming_work: ')
            comment = input('comment: ')
            sql.execute(f"INSERT INTO beehive VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (hive_number, hive_breed, hive_str, queen_exist, queen_age, queen_breed, bee_dis, last_work, coming_work, comment))
            sql.execute(f'INSERT INTO hivenote VALUES (?, ?)', (hive_number, last_work))
            db.commit()
            print('database updated successfully')
            for values in sql.execute('SELECT * FROM beehive'):
                print(values)
            next_step = int(input(
                '''input:
                 1 - add hive
                 2 - exit: '''))
            if next_step == 1:
                Hive.add_hive()
            elif next_step == 2:
                print('good buy')
            else:
                raise ValueError
        else:
            print('such a hive already exists')
            for values in sql.execute('SELECT * FROM beehive'):
                print(values)
            false_add = int(input(
                '''input:
                 1 - another hive
                 2 - exit: '''))
            if false_add == 1:
                add_hive()
            elif false_add == 2:
                print('good buy')
            else:
                raise ValueError

class UpdateHive():

    def update_last_work():
        try:
            hive_numb = int(input(
            'hive number: '))
        except:
            raise TypeError
        sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{hive_numb}'")
        if sql.fetchone() is None:
            print('such a hive already exists')
            add = int(input(
                '''add hive in base?:
                 1 - yes
                 2 - no
                 3 - exit: '''))
            if add == 1:
                Hive.add_hive()
            elif add == 2:
                print('enter the existing hive number')
                update_last_work()
            elif add == 3:
                print('good buy')
            else:
                raise ValueError
        else:
            lw = input('last_work: ')
            cw = input('coming_work: ')
            comm = input('comment: ')
            sql.execute(f"UPDATE beehive SET last_work = '{lw}' WHERE hive_number = '{hive_numb}'")
            sql.execute(f"UPDATE beehive SET coming_work = '{cw}' WHERE hive_number = '{hive_numb}'")
            sql.execute(f"UPDATE beehive SET comment = '{comm}' WHERE hive_number = '{hive_numb}'")
            sql.execute(f"UPDATE hivenote SET last_work = last_work || ' - ' ||'{lw}' WHERE hive_number = '{hive_numb}'")
            db.commit()
            print('database updated successfully')
            for values in sql.execute('SELECT * FROM beehive'):
                print(values)
            Run.__init__()

    def update_str():
        try:
            hive_numb = int(input(
                'hive number: '))
        except:
            raise TypeError
        sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{hive_numb}'")
        if sql.fetchone() is None:
            print('enter the existing hive number')
            add = int(input(
                '''add hive in base?:
                 1 - yes
                 2 - no
                 3 - exit: '''))
            if add == 1:
                Hive.add_hive()
            elif add == 2:
                print('enter the existing hive number')
                update_last_work()
            elif add == 3:
                print('good buy')
            else:
                raise ValueError
        else:
            hive_str = input("hive str: ")
            qe = input("queen exist: ")
            qa = input("queen age: ")
            qb = input("queen breed: ")
            sql.execute(f"UPDATE beehive SET str = '{hive_str}' WHERE hive_number = '{hive_numb}'")
            sql.execute(f"UPDATE beehive SET queen_exist = '{qe}' WHERE hive_number = '{hive_numb}'")
            sql.execute(f"UPDATE beehive SET queen_age = '{qa}' WHERE hive_number = '{hive_numb}'")
            sql.execute(f"UPDATE beehive SET queen_breed = '{qb}' WHERE hive_number = '{hive_numb}'")
            db.commit()
            print('database updated successfully')
            for values in sql.execute('SELECT * FROM beehive'):
                print(values)
            Run.__init__()

    def delete():
        try:
            delete_hive = int(input(
            'hive number: '))
        except:
            raise TypeError
        sql.execute(f"SELECT hive_number FROM beehive WHERE hive_number = '{delete_hive}'")
        if sql.fetchone() is None:
            print('enter the existing hive number')
            delete_return = int(input(
                '''input:
                1 - another hive
                2 - exit'''))
            if delete_return == 1:
                delete()
            elif delete_return == 2:
                Run.__init__()
            else:
                raise ValueError
        else:
            delete_confirm = int(input(
                '''are you sure?
                 1 - yes
                 2 - no: '''))
            if delete_confirm == 1:
                sql.execute(f'DELETE FROM beehive WHERE hive_number = {delete_hive}')
                sql.execute(f'DELETE FROM hivenote WHERE hive_number = {delete_hive}')
                db.commit()
                print('database updated successfully')
                for values in sql.execute('SELECT * FROM beehive'):
                    print(values)
                next_step = int(input(
                    '''input: 
                     1 - delete more
                     2 - back
                     3 - exit: '''))
                if next_step == 1:
                    delete()
                elif next_step == 2:
                    Run.__init__()
                elif next_step == 3:
                    print('good buy')
                else:
                    raise ValueError
            elif delete_confirm == 2:
                print('deletion canceled')
                Run.__init__()
            else:
                raise ValueError

    def dis():
        try:
            hive_dis = int(input(
                'hive humber: '))
        except:
            raise TypeError
        sql.execute(f"SELECT bee_dis FROM beehive WHERE hive_number = '{hive_dis}'")
        if sql.fetchone() is None:
            print('enter the existing hive number')
            add = int(input(Fore.YELLOW +
                '''add hive in base?
                 1 - yes
                 2 - no
                 3 - exit: '''))
            if add == 1:
                Hive.add_hive()
            elif add == 2:
                print('enter the existing hive number')
                dis()
            elif add == 3:
                print('good buy')
            else:
                raise ValueError
        else:
            bee_diseas = input('indicate the disease: ')
            sql.execute(f"UPDATE beehive SET bee_dis = '{bee_diseas}' WHERE hive_number = '{hive_dis}'")
            print('database updated successfully')
            for values in sql.execute('SELECT * FROM beehive'):
                print(values)
            db.commit()
            Run.__init__()


    def change():
        try:
            what = int(input("""
            what edit?
            1 - str and queen
            2 - work
            3 - back: """))
        except:
            raise TypeError
        if what == 1:
            update_str()
        elif what == 2:
            update_last_work()
        elif what == 3:
            Run.__init__()
        else:
            raise ValueError

class Run(Hive, UpdateHive):

    def __init__(self):
        for values in sql.execute('SELECT * FROM beehive'):
            print(values)
        try:
            start = int(input(
                '''input:
                 1 - add
                 2 - edit
                 3 - delete
                 4 - diseases
                 5 - note
                 6 - exit: '''))
        except:
            raise TypeError
        if start == 1:
            Hive.add_hive()
        elif start == 2:
            UpdateHive.change()
        elif start == 3:
            UpdateHive.delete()
        elif start == 4:
            UpdateHive.dis()
        elif start == 5:
            for values in sql.execute(f'SELECT * FROM hivenote'):
                print(values)
            Run.__init__()
        elif start == 6:
            print('good buy')
        else:
            raise ValueError

Run()
