import tkinter as tk
from tkinter import ttk
import os

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def run_calculator():
  gui = tk.Tk()
  gui.configure(background="light green")
  gui.title("Simple Calculator")
  gui.geometry("270x150")

  global equation
  equation = tk.StringVar()
  expression_field = tk.Entry(gui, textvariable=equation)
  expression_field.grid(columnspan=4, ipadx=70)

  button1 = ttk.Button(gui, text=' 1 ', command=lambda: press(1), width=7)
  button1.grid(row=2, column=0)

  button2 = ttk.Button(gui, text=' 2 ', command=lambda: press(2), width=7)
  button2.grid(row=2, column=1)

  button3 = ttk.Button(gui, text=' 3 ', command=lambda: press(3), width=7)
  button3.grid(row=2, column=2)

  button4 = ttk.Button(gui, text=' 4 ', command=lambda: press(4), width=7)
  button4.grid(row=3, column=0)

  button5 = ttk.Button(gui, text=' 5 ', command=lambda: press(5), width=7)
  button5.grid(row=3, column=1)

  button6 = ttk.Button(gui, text=' 6 ', command=lambda: press(6), width=7)
  button6.grid(row=3, column=2)

  button7 = ttk.Button(gui, text=' 7 ', command=lambda: press(7), width=7)
  button7.grid(row=4, column=0)

  button8 = ttk.Button(gui, text=' 8 ', command=lambda: press(8), width=7)
  button8.grid(row=4, column=1)

  button9 = ttk.Button(gui, text=' 9 ', command=lambda: press(9), width=7)
  button9.grid(row=4, column=2)

  button0 = ttk.Button(gui, text=' 0 ', command=lambda: press(0), width=7)
  button0.grid(row=5, column=0)

  plus = ttk.Button(gui, text=' + ', command=lambda: press("+"), width=7)
  plus.grid(row=2, column=3)

  minus = ttk.Button(gui, text=' - ', command=lambda: press("-"), width=7)
  minus.grid(row=3, column=3)

  multiply = ttk.Button(gui, text=' * ', command=lambda: press("*"), width=7)
  multiply.grid(row=4, column=3)

  divide = ttk.Button(gui, text=' / ', command=lambda: press("/"), width=7)
  divide.grid(row=5, column=3)

  equal = ttk.Button(gui, text=' = ', command=equalpress, width=7)
  equal.grid(row=5, column=2)

  clear=10
  clear = ttk.Button(gui, text='Clear', command=clear, width=7)
  clear.grid(row=5, column='1')

  gui.mainloop()

if __name__ == "__main__":
    run_calculator()
    run_programs()