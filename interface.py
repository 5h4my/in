from tkinter import *
from tkinter import messagebox, ttk


class Interface():
    def __init__(self):
        self.root = Tk()

        self.root.title('Ipscaner')
        # Заголовок

        self.root.geometry('600x600')
        # Разрешение

        self.root['bg'] = '#000000'
        # Цвет фона

        self.FirstFrame()
        self.SecondFrame()
        self.Button(self.firstFrame)
        self.Entry(self.firstFrame)

        if True:
            self.root.resizable(width=False, height=False)

        self.root.mainloop()

    def FirstFrame(self):
        self.firstFrame = Frame(self.root, bg='#ffffff')
        # bg- цвет фона фрейма

        self.firstFrame.place(relx=0.05, rely=0.05,
                              relwidth=0.9, relheight=0.4)
        # по оси х; по оси у; ширина; высота

    def SecondFrame(self):
        self.secondFrame = Frame(self.root, bg='#222222')
        self.secondFrame.place(relx=0.05, rely=0.5,
                               relwidth=0.9, relheight=0.4)

    def Button(self, frame):
        self.button = Button(
            frame, text='Click to continue...', command=self.Processing)
        self.button.place(relx=0.4, rely=0.7, )

    def Entry(self, frame):
        self.inPut = Entry(frame, )
        self.inPut.place(relx=0.4, rely=0.6)

    def Processing(self):
        self.data = self.inPut.get()
        self.MessageInfo(self.data)
        self.MessageError(self.data)

    def MessageInfo(self, text, title=None):
        messagebox.showinfo(title=title, message=text)

    def MessageError(self, text, title=None):
        messagebox.showerror(title=title, message=text)


if __name__ == '__main__':
    InFace = Interface()
