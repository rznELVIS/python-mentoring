import tkinter
from tkinter import Text, WORD, TOP, X

"""
	Service for providing gui interface for tag counter logic
"""
class guiService:
	window = None

	def __init__(self):
		self.window = tkinter.Tk()
		self.inintUI()

	def inintUI(self):
		self.window.title("tagcounter")

		self.initTextBox()

		self.centerWindow()
		self.window.mainloop()

	def centerWindow(self):
		w = 390
		h = 200

		sw = self.window.winfo_screenwidth()
		sh = self.window.winfo_screenheight()

		x = (sw - w) / 2
		y = (sh - h) / 2
		self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def initTextBox(self):
		self.window.urlTextBox = Text(height=1, bg="gray50", fg='white', wrap=WORD, font=("Helvetica", 18))
		self.window.urlTextBox.pack(side=TOP, fill=X)