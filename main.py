from tkinter import *
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0, END)

def save_file():
    f=asksaveasfile(mode = "w", defaultextension)=".txt", filetypes=[('Text files', '.txt')]
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def maker():
    help_view = Toplevel(window)
    help_view.geometry("300*50")    
    help_view.title("만든이")
    lb = Label(help_view, text = "강윤호가 만든 메모자입니다.")
    lb.pack()


    
                                                                   
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