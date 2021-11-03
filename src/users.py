import os

class UserHandler:
	def __init__(self, user):
		self.user = user

	def check_user_dir(self):
		path = f"home/{self.user}"
		if not os.path.exists(path):
			os.mkdir(path)
			return f"/{path}"
		else:
			return f"/{path}"
