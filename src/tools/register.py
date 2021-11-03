class register:
	def __init__(self, user, passw):
		self._userhandler(user, passw)

	def _userhandler(self, user, passw):
		with open("src/etc/users", "a") as user_file:
			user_file.write(f"{user}\n")
		with open("src/etc/passwd", "a") as passw_file:
			passw_file.write(f"{user}:{passw}\n")