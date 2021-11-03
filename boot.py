import os, subprocess, sys

def shell_handler():
	if os.path.exists("temp"):
		if os.path.exists("temp/shell.py"):
			if os.path.exists("shell.py"):
				os.remove("shell.py")
				os.rename("temp/shell.py", "shell.py")
				os.rmdir("temp")
			else:
				os.rename("temp/shell.py", "shell.py")
				os.rmdir("temp")
		else:
			os.rmdir("temp")
	else:
		pass

	proc = subprocess.Popen([sys.executable, "shell.py"], shell=True, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
	os._exit(0)

if __name__ == "__main__":
	shell_handler()