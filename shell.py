from cterminal import *
import os
from datetime import datetime
from src.cmd import *
from src.users import *
import sys, getpass
from src.cmd import *
from src.file_handler import *
from src.login import *

class Shell:
	def __init__(self, name):
		self.name = name
		self.user = ""
		self.logo = "PʏSʜᴇʟʟ"
		self.path = ""
		self.horiz = '─'
		self.vert = '│'
		self.ul = '┌'
		self.ll = '└'
		self.logged = False
		commands.parent = self

		cmd.clear()
		filehandler()
		cmd.setname(self.name)
		self.shell_login()
		cmd.clear()
		self.cmds = self._getCommands()
		self._shell_handler()

	def shell_login(self):
		self.getInfos()
		login_ = login(self.name)
		login_._login()
		self.user = login_.getuser()

	def _getCommands(self):
		cmds = {}
		cmd_str = [f for f in dir(commands) if not f.startswith("__")]
		for cmd in cmd_str:
			cmds[cmd] = commands.__dict__.get(cmd)
		return cmds

	def _shell_handler(self):
		while True:
			#cprint(f"{style.GREEN}{self.ul}{self.horiz*2}({style.CYAN}{self.user}@{self.name}{style.GREEN})-[{style.RESET}~{commands.path}{style.GREEN}]\n{style.GREEN}{self.ll}{self.horiz}{style.CYAN}$",
			#	end=" ")

			cprint(get_shell_style(), end=" ")
			self._parse(input())
			print()

	def _parse(self, cmd):
		if cmd != "":
			cmd = cmd.split(" ")

			if len(cmd) > 1:
				if cmd[0] in self.cmds:
					self.cmds.get(cmd[0])(cmd[1:])
				else:
					print(f"{cmd[0]} :command not found")
			else:
				if cmd[0] in self.cmds:
					self.cmds.get(cmd[0])()
				else:
					print(f"{cmd[0]} :command not found")
		else:
			pass

	def getInfos(self):
		last_login = open("src/etc/last_login", "r").read()
		cprint(f"{self.ul}{self.horiz}{style.YELLOW} {self.logo}\n{style.RESET}{self.vert}\n{self.vert} Made by Alex\n{self.vert} v1.0\n{self.vert}\n{self.vert} last login: {last_login}\n{self.ll}{self.horiz}\n")


if __name__ == "__main__":
	Shell("PyShell")