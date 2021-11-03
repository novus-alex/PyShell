from pynput.keyboard import Listener, Key
from cterminal import *

class nano_tool:
	def __init__(self, path):
		self.file_content = ""
		self.ctrl = False
		self.shift = False
		self.path = path[0]
		self._init()

		with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
			listener.join()

	def _init(self):
		cmd.clear()
		cprint(f"{style.REVERSED}[PyShell]...Nano...v1.0")

	def on_press(self, key):
		if not self.ctrl:
			if key == Key.enter:
				self.file_content += "\n"
				char = ""
			elif key == Key.backspace:
				self.file_content = self.file_content[:-1]
				splited_content = self.file_content.split("\n")
				cmd.movecursor(len(splited_content) + 3, len(splited_content[len(splited_content) - 1]) + 1)
				print(" ", end="\r")
				char = ""
			elif key == Key.space:
				self.file_content += " "
				char = " "
			elif key == Key.ctrl_l:
				self.ctrl = True
				char = ""
			elif key == Key.tab:
				self.file_content += "    "
				char = "    "
			elif key == Key.shift_l:
				self.shift = True
				char = ""
			elif key.char == "\x03":
				quit()
			else:
				if not self.shift:
					self.file_content += key.char
					char = key.char
				else:
					self.file_content += key.char.capitalize()
					char = key.char.capitalize()

			splited_content = self.file_content.split("\n")
			cmd.movecursor(len(splited_content) + 3, len(splited_content[len(splited_content) - 1]))
			print(char, end="\r")

		elif key.char == "\x18":
			with open(self.path, "a") as f:
				f.write(self.file_content)
			cmd.clear()
			quit()
		else:
			print(key.char)

	def on_release(self, key):
		if key == Key.ctrl_l:
			self.ctrl = False
		if key == Key.shift_l:
			self.shift = False
