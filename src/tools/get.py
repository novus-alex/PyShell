from src.updater import *
import requests

class get_handler:
	def update():
		'''@update

		Use this method to check/get a shell update
		usage:
			- get update

		'''

		returned = requests.get("https://api.github.com/repos/novus-alex/PyShell/releases/latest")
		lv = str(returned.json()['name'])
		version = open('src/etc/version', 'r').read()

		if version != lv:
			print(f"Upgrading for version: {lv}?", end=" ")
			if input("(y/n): ") == "y":
				update_shell(lv)
			else:
				pass
		else:
			print(f"Already the latest version: {version}")

	def version():
		print(f"[PyShell {open('src/etc/version', 'r').read()}]")


def get_cmds():
	gets = {}
	cmd_str = [f for f in dir(get_handler) if not f.startswith("__")]
	for cmd in cmd_str:
		gets[cmd] = get_handler.__dict__.get(cmd)
	return gets