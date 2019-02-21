from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):#默认标题为空
        Frame.__init__(self,master)
        self.pack()
        self.creatWidget()
    def creatWidget(self):
        self.Label_1=Label(self,text='Hello,World!')
        self.Label_1.pack()
        self.Label_2=Label(self,text='世界你好！')
        self.Label_2.pack()
        self.inputLabel_3=Entry(self)
        self.inputLabel_3.pack()
        self.button1=Button(self,text='退出',command=self.quit)
        self.button1.pack()
        self.button2=Button(self,text='取消',command=self.quit)
        self.button2.pack()
        self.alertButton = Button(self, text='弹出按钮', command=self.get_input)
        self.alertButton.pack()
    def get_input(self):
        name=self.inputLabel_3.get() or 'world'
        messagebox.showinfo('Message','hello,%s'%name)

app=Application()
app.master.title('Practice 1')
app.mainloop()


