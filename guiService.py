import tkinter
from tkinter import Text, WORD, TOP, LEFT, RIGHT, X, Button, Frame, BOTH, Label, BOTTOM

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
		self.initButtons()
		self.initTagCount()
		self.initStatusLabel()

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

	def initButtons(self):
		frameButtons = Frame(self.window)
		frameButtons.pack(fill=X)

		self.window.loadButton = Button(frameButtons, text="Загрузить", height=3)
		self.window.loadButton.config(command=self.loadButtonClick)
		self.window.loadButton.pack(side=LEFT, expand=True, fill=BOTH)

		self.window.loadButtonFromBase = Button(frameButtons, text="Загрузить из базы", height=3)
		self.window.loadButtonFromBase.config(command=self.initLoadFromBaseClick)
		self.window.loadButtonFromBase.pack(side=LEFT, expand=True, fill=BOTH)

	def loadButtonClick(self):
		self.window.loadButton["text"] = "Загружено"

	def initLoadFromBaseClick(self):
		self.window.loadButtonFromBase["text"] = "Загружено из базы"

	def initTagCount(self):
		self.window.tagCountTextBox = Text(height=4, bg="gray90", fg='black', wrap=WORD, font=("Helvetica", 18))
		self.window.tagCountTextBox.pack(side=TOP, expand=True)


	def initStatusLabel(self):
		self.window.statusLabel = Label(text="Статус", height=1, font=("Helvetica", 18), bg="gray70")
		self.window.statusLabel.pack(side=BOTTOM, expand=True, fill=X)
