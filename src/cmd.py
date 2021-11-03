from cterminal import *
from .updater import *
from src.tools.get import *
import os, requests, getpass
from src.tools.wget import *
from src.tools.register import *
from src.tools.nano import *
from src.tools.nmap import *

class commands:
	'''

	Place of all shell commands

	How to add a new command:
		- simply write your command func into this class
		- the command will be automatically imported into the shell
	usage:
		- class commands:
			...

		  	def test_cmd():
				print("it works!")

	then into the shell:
		- test_cmd
	[output]: it works!

	'''

	path = ""
	user_path = ""
	parent = None
	shell_style = None

	def clear():
		'''@clear

		Use this method to clear the screen buffer
		usage:
			- clear

		'''

		cmd.clear()

	def ls():
		'''@ls

		Use this method to get all of the working directory objects (folders/files)
		usage:
			- ls

		'''

		for path, folders, files in os.walk(os.path.abspath(commands.path.replace("/", "", 1))):
			if len(folders) == 0:
				if len(files) == 0:
					empty = True
					pass
				else:
					empty = False
					for file in files:
						print(file, end=" ")
			else:
				empty = False
				for folder in folders:
					cprint(style.CYAN + folder, end=" ")

		if not empty:
			print()
		else:
			pass

	def cd(path):
		'''@cd

		Use this method to go into a directory
		@params:
			- path: Required (the path where you want to go)
		usage:
			- cd home/test/..
		
		'''

		path = path[0]
		if path == "..":
			if os.path.exists(path):
				path_splited = commands.path.split("/")
				path_splited.remove(path_splited[len(path_splited) - 1])
				if path == None:
						commands.path = ""
				else:
					commands.path = "/".join(path_splited) if len(path_splited) > 1 else ""
		else:
			path = f"{commands.path.replace('/', '', 1)}/{path}"
			if os.path.exists(path):
				commands.path = "/" + path if not path.startswith("/") else path
			else:
				print(f"path '{path}' does not exist")
				print()

	def get(*args, **kwargs):
		'''@get

		Use this method to interface with get commands
		@params:
			- command: Required (at least one)
		usage:
			- get ...

		'''
		
		cmds = get_cmds()
		args = args[0]
		if len(args) == 1:
			cmd = str(args[0])
			if cmd in cmds:
				cmds.get(cmd)()
			else:
				print(f"get {str(args[0])} :command not found")
		elif len(args) > 1:
			cmd = str(args[0])
			args.remove(cmd)
			if cmd in cmds:
				cmds.get(cmd)(args)
			else:
				print(f"get {cmd} :command not found")

	def wget(url):
		'''@wget

		Use this method to get files from urls
		@params:
			- url: Required (max one)
		usage:
			- wget https://...

		'''

		if len(url) == 1:
			dl_url = url[0]
			wget_dl(dl_url, commands.path)
		else:
			print(f"cannot download multiple urls ({len(url)})")

	def cat(file):
		'''@cat

		Use this method to print the content of a file in the terminal
		@params:
			- file: Required (max one)
		usage:
			- cat yourfile.txt

		'''

		if len(file) == 1:
			file = file[0]
			print(open(f"{commands.path.replace('/', '', 1)}/{file}", "r").read())

	def re(username):
		'''@re

		Use this method to register a new user
		@params:
			- username: Required (max one)
		usage:
			- re username

		'''

		if len(username) == 1:
			username = username[0]
			users = open("src/etc/users", "r").readline()
			if not username in users:
				passw = getpass.getpass(f"Create a password for {username}: ")
				passw_check = getpass.getpass("Retype password: ")
				if passw == passw_check:
					register(username, passw)
				else:
					print("Passwords are not the same")
			else:
				print(f"user '{username}' already exists")
		else:
			print(f"Cannot register multiple users at the same time ({len(username)})")

	def mkdir(dirname):
		'''@mkdir

		Use this method to create a folder
		@params:
			- dirname: Required (max one)
		usage:
			- mkdir example
		'''

		if len(dirname) == 1:
			dirname = dirname[0]
			os.mkdir(f"{commands.path.replace('/', '', 1)}/{dirname}")
		else:
			print(f"cannot create multiple folders at the same time ({len(dirname)})")

	def rmdir(*args, **kwargs):
		'''@rmdir

		Use this method to delete a folder
		@params:
			- dirname: Required (max one)
			- -f: Optional (to delete a not empty folder)
		usage:
			- rmdir example (if empty)
			- rmdir -f example (if not empty)
		'''

		args = args[0]
		if len(args) == 1:
			dirname = args[0]
			try:
				os.rmdir(f"{commands.path.replace('/', '', 1)}/{dirname}")
			except OSError as e:
				print(f"{e} :cannot delete the folder")
		elif "-f" in args:
			dirname = args[len(args) - 1]
			for root, dirs, files in os.walk(f"{commands.path.replace('/', '', 1)}/{dirname}", topdown=False):
				for name in files:
					os.remove(os.path.join(root, name))
				for name in dirs:
					os.rmdir(os.path.join(root, name))
			os.rmdir(f"{commands.path.replace('/', '', 1)}/{dirname}")
		else:
			print(f"cannot delete multiple folders at the same time ({len(dirname)})")

	def nano(filename):
		nano_tool(f"{commands.path.replace('/', '', 1)}/{filename[0]}")

	def nmap(host):
		nmap(host[0])

	def ct(shell_style):
		styles = ["simple", "-csimple", "multi", "-cmulti"]
		if len(shell_style) == 1:
			if shell_style[0] in styles:
				with open("src/etc/shell_style", "w") as f:
					f.write(shell_style[0])
			else:
				print(f"{shell_style} :style arguments does not exist")
		else:
			if "".join(shell_style) in styles:
				with open("src/etc/shell_style", "w") as f:
					f.write(" ".join(shell_style))
			else:
				print(f"{shell_style} :style arguments does not exist")
		


	def logout():
		'''@logout

		Use this method to logout from your account
		usage:
			- logout

		'''

		commands.parent.shell_login()

	def exit():
		'''@exit

		Use this method to close the shell
		usage:
			- exit

		'''

		os._exit(0)


def get_shell_style():
	with open("src/etc/shell_style", "r") as f:
		shell_style = f.read()

	if shell_style == "simple":
		return f"{commands.parent.user}@{commands.parent.name}:~{commands.path}$"
	elif shell_style == "multi":
		return f"{commands.parent.ul}{commands.parent.horiz*2}({commands.parent.user}@{commands.parent.name})-[~{commands.path}]\n{commands.parent.ll}{commands.parent.horiz}$"
	elif shell_style == "-c simple":
		return f"{style.GREEN}{commands.parent.user}@{commands.parent.name}{style.RESET}:{style.CYAN}~{commands.path}{style.RESET}$"
	elif shell_style == "-c multi":
		return f"{style.GREEN}{commands.parent.ul}{commands.parent.horiz*2}({style.CYAN}{commands.parent.user}@{commands.parent.name}{style.GREEN})-[{style.RESET}~{commands.path}{style.GREEN}]\n{style.GREEN}{commands.parent.ll}{commands.parent.horiz}{style.CYAN}$"
	else:
		print(f"{commands.shell_style} :style does not exist")