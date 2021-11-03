import getpass
from datetime import datetime
from src.users import *
from src.cmd import *

class login:
	def __init__(self, name):
		self.logged = False
		self.name = name

	def _login(self):
		users = list(open("src/etc/users", "r").readlines())
		passwds = {}

		for u in range(len(users)):
			if "\n" in users[u]:
				users[u] = users[u].replace("\n", "")
			else:
				pass

		for p in list(open("src/etc/passwd", "r").readlines()):
			splited = p.replace("\n", "").split(":")
			if not splited[0] in users:
				pass
			else:
				passwds[splited[0]] = splited[1]

		login_try = 0

		while not self.logged:
			if login_try < 3:
				print(f"login for {self.name}: ", end="")
				user = input()
				if user in users:
					if getpass.getpass(f"password for {user}: ") == passwds.get(user):
						self.logged = True
						with open("src/etc/last_login", "w") as log:
							now = datetime.now()
							log.write(now.strftime("%d/%m/%Y %H:%M:%S"))

							commands.path = UserHandler(user).check_user_dir()
							self.user = user
					else:
						print("wrong password")
						login_try += 1
				else:
					print(f"user {user} does not exist")
					login_try += 1
			else:
				print("Permission denied")
				quit()

	def getuser(self):
		return self.user