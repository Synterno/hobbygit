# регистрация и авторизация юзера
import sqlite3

db = sqlite3.connect('users.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT

)""")

db.commit()


class User():

	def reg(self, login, password):
		self.login = login
		self.password = password
		if len(password) < 8:
			raise ValueError('password mismatch, less than 8 characters')

		else:

			sql.execute(f"SELECT login FROM users WHERE login = '{login}'")
			if sql.fetchone() is None:

				sql.execute(f'INSERT INTO users VALUES (?, ?)', (login, password))
				db.commit()
				print(login + ' user created')

			else:
				raise ValueError('user with this login already exists')

	def auth(self, login, password):
		self.login = login
		self.password = password
		sql.execute(f"SELECT login FROM users WHERE login = '{login}'")
		if sql.fetchone() is None:
			raise ValueError('no such user exists')

		else:
			print('success authorization')

	def user_info(self):
		print("user info: \n" + "login: " + self.login + "\n" + "password: " + self.password)


a = User()
a.reg("qwerty", "qwertypassword")
a.auth("qwerty", "qwertypassword")
a.user_info()

