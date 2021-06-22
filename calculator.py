from tkinter import *

class Calculator(Frame):

    def __init__(self,master):
        super(Calculator,self).__init__(master)
        self.task=""
        self.UserIn=StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input=Entry(self,bg="#5BC8AC",bd=29,insertwidth=4,width=24,
        font=("Verdana",20,"bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan = 4)
        self.user_input.insert(0, "0")

        self.button7 = Button(self,bg = "light green", bd=12,text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(7))
        self.button7.grid(row=2, column=0, sticky=W)

        self.button8 = Button(self,bg = "light green", bd=12,text="8", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(8))
        self.button8.grid(row=2, column=1,sticky=W)

        self.button9 = Button(self,bg = "light green", bd=12,text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(9))
        self.button9.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self,bg = "light green", bd=12,text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = Button(self,bg = "light green", bd=12,text="5", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1,sticky=W)

        self.button6 = Button(self,bg = "light green", bd=12,text="6", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button1 = Button(self,bg = "light green", bd=12,text="1", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(1))
        self.button1.grid(row=4, column=0, sticky=W)

        self.button2 = Button(self,bg = "light green", bd=12,text="2", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(2))
        self.button2.grid(row=4, column=1,sticky=W)

        self.button3 = Button(self,bg = "light green", bd=12,text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick(3))
        self.button3.grid(row=4, column=2, sticky=W)

        self.button0 = Button(self, bg= "#98DBC6", bd=12, text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda:self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        self.addButton = Button(self,bg = "#98DBC6", bd=12,text="+", padx=35, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick("+"))
        self.addButton.grid(row=2, column=3, sticky=W)

        self.subButton = Button(self,bg = "#98DBC6", bd=12,text="-", padx=39, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick("-"))
        self.subButton.grid(row=3, column=3,sticky=W)

        self.multButton = Button(self,bg = "#98DBC6", bd=12,text="*", padx=38, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick("*"))
        self.multButton.grid(row=4, column=3, sticky=W)

        self.divButton = Button(self,bg = "#98DBC6", bd=12,text="/", padx=39, pady=25, font=("Helvetica", 20, "bold"),command=lambda: self.buttonClick("/"))
        self.divButton.grid(row=5, column=3,sticky=W)

        self.equalButton = Button(self,bg = "yellow", bd=12,text="=", padx=95, pady=25,  font=("Helvetica", 20, "bold"),command=self.calculateTask)
        self.equalButton.grid(row=5, column=1, sticky=W, columnspan=4)

        self.clearAllButton = Button(self,bg = "yellow", bd=12,text="AC", padx=7, width=28, font=("Helvetica", 20, "bold"),command=self.clearDisplay)
        self.clearAllButton.grid(row=1, sticky=W, columnspan=4)

    def buttonClick(self,number):
            self.task = str(self.task)+str(number)
            self.UserIn.set(self.task)

    def calculateTask(self):
        self.data=self.user_input.get()
        try:
            self.answer=eval(self.data)
            self.displayText(self.answer)
            self.task=self.answer
        except SynthaxError as e:
            self.displayText("Invalid Synthax!")
            self.task=""
    def displayText(self,value):
        self.user_input.delete(0,END)
        self.user_input.insert(0,value)

    def clearDisplay(self):
        self.task=""
        self.user_input.delete(0, END)
        self.user_input.insert(0,"0")

calculator =Tk()

calculator.title("Calculator")
app = Calculator(calculator)

calculator.resizable(width = False, height = False)

calculator.mainloop()
