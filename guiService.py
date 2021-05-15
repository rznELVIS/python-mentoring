import tkinter

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