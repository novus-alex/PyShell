import urllib.request as urllib2
from cterminal import *
import os, sys

class wget_dl:
	def __init__(self, url, path):
		self.url = url
		self.path = path.replace("/", "", 1) + "/"
		self.filename = self._getfilename()
		self.dl()

	def _getfilename(self):
		splited_url = self.url.split("/")
		return splited_url[len(splited_url) - 1]

	def dl(self):
		u = urllib2.urlopen(self.url)
		f = open(self.path + self.filename, 'wb')
		file_size = int(u.getheader('Content-Length'))
		file_size_dl = 0
		block_sz = 8192
		cmd.hidecursor()
		print(f"\nGet {self.filename}")
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			print(f"|{int(round((file_size_dl * 100. / file_size), 0)/2)*'█'}{(50 - int(round((file_size_dl * 100. / file_size), 0)/2))*'-'}| {int(round((file_size_dl * 100. / file_size), 0))}% Complete", end="\r")
		cmd.showcursor()
		print()
		f.close()