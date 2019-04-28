#!/usr/bin/env python3
'''
This tool allows one to enable remote desktop service on a remote machine.
Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar
[+] Python version: 3.6.3
[+] PowerShell version: 5.1
'''
import os, sys
import subprocess
from subprocess import check_output

def logo():
	logo = '''	
        \\\|//		[+] Author: Viral Maniar
        (o o)		[+] Twitter: @ManiarViral
~~~~oOOo~(_)~oOOo~~~~
______         _            ___        ______             
| ___ \       | |          / _ \       | ___ \            
| |_/ /__  ___| | ________/ /_\ \______| |_/ / ___   ___  
|  __/ _ \/ _ \ |/ /______|  _  |______| ___ \/ _ \ / _ \ 
| | |  __/  __/   <       | | | |      | |_/ / (_) | (_) |
\_|  \___|\___|_|\_\      \_| |_/      \____/ \___/ \___/ 
                                                          

'''
	return logo

OPTIONS = '''
1. Set Execution Policy to Unrestricted
2. Enable Remote Desktop Service
3. Disable Remote Desktop Service
4. Exit
'''
	
def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkHostWindows():
	if os.name == "nt":
		print ('[+] All good....')
	else:
		print ('[!] Please run the application on Windows machine')
		sys.exit(0)

def cmd_exectionPolicy():

	process=subprocess.Popen(["powershell","Set-ExecutionPolicy Unrestricted -Scope CurrentUser"], shell=False);
	result=process.communicate()[0]
	print ("[!] Execution Policy is now set to unrestricted.")

def cmd_enableRDP():

	process=subprocess.Popen(["powershell",".\\rdpe.ps1"], shell=False);
	result1=process.communicate()[0]
	print("Port scanning...")
	process=subprocess.Popen(["powershell",".\\testconnection.ps1"], shell=False);
	result3=process.communicate()[0]
	print(result3)
	print ("[!]RDP settings enabled on a remote machine.")
	
	
def cmd_disableRDP():

	process=subprocess.Popen(["powershell",".\\rdpd.ps1"], shell=False);
	result2=process.communicate()[0]
	print(result2)
	process=subprocess.Popen(["powershell",".\\testconnection.ps1"], shell=False);
	result4=process.communicate()[0]
	print(result4)
	print ("[!]RDP settings disbaled on a remote machine.")
	
cmds = {
	"1" : cmd_exectionPolicy,
	"2" : cmd_enableRDP,
	"3" : cmd_disableRDP,
	"4" : lambda: sys.exit(0)
}

def main():
	os.system('cls')
	print (logo())
	checkHostWindows()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
