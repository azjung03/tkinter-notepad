from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("notepad")
window.geometry("400*400")
window.resizable(False,False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일")
menu_1.add_command(label="저장")
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destory)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이")
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)
window.gird_rowconfigure(0, weight=1)
text_area.grid(sticky = N + E + s + w)


window.config(menu=menu)

window.mainloop()