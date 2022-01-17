"""
Very Very Very simple calculator

Program by @rodzpm - https://github.com/Rodzpm

This program is a very simple calculator in python with tkinter.
"""

from tkinter import *       #Imports
from tkinter import messagebox
from functools import partial

class App:      #Tkinter App Class
    def __init__(self, width, height):
        self.w = width      #Width and Height of the window
        self.h = height
        self.btn = [        #Defines the calculator buttons
            ["7","8","9","x"],
            ["4","5","6","÷"],
            ["1","2","3","+"],
            ["=","0",",","-"],
        ]
  
    def run(self):      #application's run function
        window = Tk()       #Basic window configurations
        window.title("Very Very Very simple calculator")
        window.geometry(str(self.w)+'x'+str(self.h))
        window.resizable(False, False) 
        self.calcul = list()        #List with all user's entries
        self.text_label = StringVar()
        self.text_label.set("Enter your calculation...")
        #Label to display result
        result_label = Label(window, textvariable= self.text_label, background="grey", font=("Courier", 10), width=45, height=5).grid(column = 0, row = 0, columnspan=10) 
        for i in range(4):      #Loop to create the calculator buttons
            for j in range(4):
                Button(window, text=self.btn[i][j], width=10, height=5, font=("Courier", 10), command=partial(self.click, i, j)).grid(column = j, row = i+1)
        #Label to diplay credits
        credit_label = Label(window, text= "By Rodz", width=45, height=5, font=("Courier", 10)).grid(column = 0, row = 5, columnspan=10)
        window.mainloop()

    def click(self, i, j):      #Button's clicked function
        button = self.btn[i][j]     #retrieves information from the button
        if button == "=":       #If "=" button, show result
            self.result()
        else:       #Else, add it in the calculation and update the screen
            new = ""
            self.calcul.append(button)
            for elt in self.calcul:
                new += elt + " "
            self.text_label.set(new) 
        
    def error(self):        #Error function with messagebox
        messagebox.showerror(title="Error", message="Please enter a valid calculation...")

    def operator(self,nb1,nb2,op):      #Function that does the calculations between two numbers
        calcul_temp = 0
        if op == "+":
            calcul_temp = float(nb1) + float(nb2)
        elif op == "-":
            calcul_temp = float(nb1) - float(nb2)            
        elif op == "x":
            calcul_temp = float(nb1) * float(nb2) 
        elif op == "÷":
            calcul_temp = float(nb1) / float(nb2)
        return calcul_temp

    def result(self):       #Function that will run through the whole calculation and solve it
        number = ["1","2","3","4","5","6","7","8","9","0"]
        operator = ["x","+","-","÷"] 
        temp_result = 0
        operation = False
        nb1 = ""
        nb2 = ""
        op = ""
        for elt in self.calcul:
            if elt in number and not operation:
                nb1 += elt
            elif elt in number and operation:
                nb2 += elt
            elif elt in operator and not operation:
                op = elt
                operation = True
            elif elt in operator and operation:
                nb1 = self.operator(nb1, nb2, op)
                nb2 = ""
                op = elt
            elif elt == "," and not operation and nb1[-1] != ",":
                nb1 += "."
            elif elt == "," and operation and nb2[-1] != ",":
                nb2 += "."
            else:
                self.error()
                self.calcul = list()
        if op == "":
            self.calcul = list()
            self.txt_label(nb1)
        else:
            self.calcul = list()
            self.txt_label(self.operator(nb1,nb2,op))             
        

    def txt_label(self, txt):       #Function that updates the text
        self.text_label.set(txt)     



window = App(360,530)       #Create an window object
window.run()        #Run the tkinter window
