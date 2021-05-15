import sys

"""
	Parsing of command line args to structured list.
"""
def parseCommnadLineArguments():
	if (len(sys.argv) == 1):
		print("No commands")
		return {}

	commands = {}
	for i in range(1, len(sys.argv), 2):
		if (i+1 < len(sys.argv)):
			commands[sys.argv[i]] = sys.argv[i+1]
			print(f"let's process {i} argument")

	return commands

def main():
	print("hello mentoring")

	commands = parseCommnadLineArguments()
	print(commands)
	if len(commands) == 0:
		print("Run GUI")
	else:
		print("run console")

main()