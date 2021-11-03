import urllib.request as urllib2
from cterminal import *
import os, sys
from zipfile import ZipFile
import time
import subprocess

class update_shell:
	def __init__(self, lv):
		self.url = "https://github.com/novus-alex/PyShell/releases/download/1.0/src.zip"
		self.url_shell = "https://github.com/novus-alex/PyShell/releases/download/1.0/shell.py"
		self.filename = self._getfilename()
		self.filename_shell = self._getfilenameshell()
		self.extension = self._getextension()
		self.lv = lv

		self.updated = False
		self._folderHandler()
		self.update()

	def _folderHandler(self):
		if not self.updated:
			if not os.path.exists("temp"):
				os.mkdir("temp")
			else:
				pass
		else:
			if os.path.exists("temp"):
				os.rmdir("temp")
			else:
				pass

	def _getfilename(self):
		splited_url = self.url.split("/")
		return splited_url[len(splited_url) - 1]

	def _getfilenameshell(self):
		splited_url = self.url_shell.split("/")
		return splited_url[len(splited_url) - 1]

	def _getextension(self):
		splited_name = self.filename.split(".")
		return splited_name[len(splited_name) - 1]

	def update(self):
		u = urllib2.urlopen(self.url)
		f = open("temp/" + self.filename, 'wb')
		file_size = int(u.getheader('Content-Length'))
		file_size_dl = 0
		block_sz = 8192
		cmd.hidecursor()
		print(f"\nInstalling {self.filename}")
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			print(f"|{int(round((file_size_dl * 100. / file_size), 0)/2)*'█'}{(50 - int(round((file_size_dl * 100. / file_size), 0)/2))*'-'}| {int(round((file_size_dl * 100. / file_size), 0))}% Complete", end="\r")
		print("\n")
		f.close()

		u = urllib2.urlopen(self.url_shell)
		f = open("temp/" + self.filename_shell, 'wb')
		file_size = int(u.getheader('Content-Length'))
		file_size_dl = 0
		block_sz = 8192
		cmd.hidecursor()
		print(f"\nInstalling {self.filename_shell}")
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			print(f"|{int(round((file_size_dl * 100. / file_size), 0)/2)*'█'}{(50 - int(round((file_size_dl * 100. / file_size), 0)/2))*'-'}| {int(round((file_size_dl * 100. / file_size), 0))}% Complete", end="\r")
		print("\n")
		f.close()
		cmd.showcursor()
		self._unzip()
		self.updated = True

		with open("src/etc/version") as version_handler:
			version_handler.write(self.lv)

		print("\nRestarting")
		time.sleep(1)
		self._restart()

	def _unzip(self):
		with ZipFile('temp/src.zip', 'r') as zipObj:
			zipObj.extractall()
		os.remove("temp/src.zip")

	def _restart(self):
		proc = subprocess.Popen([sys.executable, "boot.py"], shell=False, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
		os._exit(0)