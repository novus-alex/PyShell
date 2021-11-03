import os

class filehandler:
	def __init__(self):
		if os.path.exists("src/etc/users"):
			pass
		else:
			with open("src/etc/users", "a") as f:
				f.write("root\n")

		if os.path.exists("src/etc/passwd"):
			pass
		else:
			with open("src/etc/passwd", "a") as f:
				f.write("root:root\n")

		if os.path.exists("src/etc/last_login"):
			pass
		else:
			with open("src/etc/last_login", "a") as f:
				f.write("")

		if os.path.exists("src/etc/version"):
			pass
		else:
			with open("src/etc/version", "a") as f:
				f.write("")

		if os.path.exists("src/etc/shell_style"):
			pass
		else:
			with open("src/etc/shell_style", "a") as f:
				f.write("simple")

		if os.path.exists("home"):
			pass
		else:
			os.mkdir("home")
