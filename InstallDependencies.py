import subprocess 
from sys import platform 

if platform == "win32":
	subprocess.call('pip install progressbar'.split())
	subprocess.call('pip install intelhex'.split())
	
elif platform == "linux" or platform == "linux2":
	subprocess.call('sudo pip install progressbar'.split())
	subprocess.call('sudo pip install intelhex'.split())
