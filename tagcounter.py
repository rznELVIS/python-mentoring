import sys
from guiService import guiService
import tkinter

"""
	Parsing of command line args to structured list.
"""
def parseCommnadLineArguments():
	if (len(sys.argv) == 1):
		return {}

	commands = {}
	for i in range(1, len(sys.argv), 2):
		if (i+1 < len(sys.argv)):
			commands[sys.argv[i]] = sys.argv[i+1]
			print(f"let's process {i} argument")

	return commands

"""
	Main function of the program.
"""
def main():
	print("hello mentoring")

	commands = parseCommnadLineArguments()
	print(commands)
	if len(commands) == 0:
		print("Run GUI")
		service = guiService()
	else:
		print("run console")

main()