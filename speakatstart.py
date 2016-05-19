import subprocess
def execute_command(str):
	subprocess.Popen(['C:\Program Files (x86)\eSpeak\command_line\espeak.exe', str])

execute_command("Welcome to windows master")