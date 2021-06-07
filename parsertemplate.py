import bs4
import requests
import sqlite3


db = sqlite3.connect('parse.db')
sql = db.cursor()
# СОЗДАНИЕ ТАБЛИЦЫ В БД
sql.execute("""CREATE TABLE IF NOT EXISTS table (
    title TEXT,
    price TEXT,
    game TEXT
)""")
db.commit()

# ПАРСИНГ ФУНКЦИЯ, ЗАПОЛНИ ...
def parse():
    URL = '...'
    HEADERS = {
        'User-Agent':'...'
    }
    response = requests.get(URL, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='...')
    comps = []
    for item in items:
        comps.append({
            'title': item.find('span', class_='...').get_text(strip=True),
            'price': item.find('span', class_='...').get_text(strip=True),
            'game': item.find('span', class_='...').get_text(strip=True)
        })
        for comp in comps:
            print(f"{comp['title']}, {comp['price']}, {comp['game']}")
            sql.execute(f'INSERT INTO table VALUES (?, ?, ?)', (comp['title'], comp['price'], comp['game']))
            db.commit()

# УДАЛЕНИЕ ДУБЛИКАТОВ ИЗ БД
sql.execute('DELETE FROM table WHERE rowid NOT IN (select min(rowid) FROM table GROUP BY title, price, game)')
db.commit()


parse()
