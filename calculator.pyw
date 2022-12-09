from tkinter import *
from tkinter.messagebox import showinfo

def calculate(event = None):
	text = entry.get()
	if text.isdigit():
		showinfo('Ваш рост...', f'Ваш рост {text} см!')
	else:
		showinfo('Ваш рост...', f'Введите цифры!')

root = Tk()

label = Label(root, text = 'Введите ваш рост')
entry = Entry(root)
button = Button(root, text = 'Проверить', command = calculate)

label.grid(row = 0, column = 0, sticky = E)
entry.grid(row = 0, column = 1)
button.grid(row = 1, column = 0)

button.bind('<Button-1>', calculate)

if __name__ == '__main__':
	root.mainloop()