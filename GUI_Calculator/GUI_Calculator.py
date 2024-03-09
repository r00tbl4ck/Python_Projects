import tkinter

calculation = ""

# Adds symbol to calculation
def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

# Evaluates calculation
def evaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        clearField()
        textResult.insert(1.0, "Error!")


# Clears calculation field
def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")

# Removes last character
def eraseLastCharacter():
    global calculation
    calculation = calculation[:-1]
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

# Creating the frame
root = tkinter.Tk()
# Frame size
root.geometry("255x200")
# Frame title
root.title("Simple Calculator")
root.configure(bg="#1C1C1C")

# Text result field
textResult = tkinter.Text(root, height=2, width=35)
textResult.grid(columnspan=5)

# Buttons
btn1 = tkinter.Button(root, text="1", command=lambda: addToCalculation(1), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn2 = tkinter.Button(root, text="2", command=lambda: addToCalculation(2), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn3 = tkinter.Button(root, text="3", command=lambda: addToCalculation(3), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn4 = tkinter.Button(root, text="4", command=lambda: addToCalculation(4), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn5 = tkinter.Button(root, text="5", command=lambda: addToCalculation(5), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn6 = tkinter.Button(root, text="6", command=lambda: addToCalculation(6), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn7 = tkinter.Button(root, text="7", command=lambda: addToCalculation(7), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn8 = tkinter.Button(root, text="8", command=lambda: addToCalculation(8), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn9 = tkinter.Button(root, text="9", command=lambda: addToCalculation(9), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btn0 = tkinter.Button(root, text="0", command=lambda: addToCalculation(0), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnPlus = tkinter.Button(root, text="+", command=lambda: addToCalculation("+"), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnMinus = tkinter.Button(root, text="-", command=lambda: addToCalculation("-"), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnDiv = tkinter.Button(root, text="/", command=lambda: addToCalculation("/"), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnMul = tkinter.Button(root, text="*", command=lambda: addToCalculation("*"), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnMod = tkinter.Button(root, text="%", command=lambda: addToCalculation("%"), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnEqual = tkinter.Button(root, text="=", command=evaluateCalculation, width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnClear = tkinter.Button(root, text="C", command=clearField, width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnOpenParentheses = tkinter.Button(root, text="(", command=lambda: addToCalculation("("), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnCloseParentheses = tkinter.Button(root, text=")", command=lambda: addToCalculation(")"), width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))
btnBackspace = tkinter.Button(root, text="⌫", command=eraseLastCharacter, width=5, bg="#1C1C1C", fg="white", font=("Monospace", 9))

# Button Placements
btn1.grid(row=2, column=1)
btn2.grid(row=2, column=2)
btn3.grid(row=2, column=3)
btn4.grid(row=3, column=1)
btn5.grid(row=3, column=2)
btn6.grid(row=3, column=3)
btn7.grid(row=4, column=1)
btn8.grid(row=4, column=2)
btn9.grid(row=4, column=3)
btn0.grid(row=5, column=2)
btnPlus.grid(row=2, column=4)
btnMinus.grid(row=3, column=4)
btnDiv.grid(row=4, column=4)
btnMul.grid(row=5, column=4)
btnMod.grid(row=6, column=4)
btnEqual.grid(row=6, column=3)
btnClear.grid(row=6, column=2)
btnBackspace.grid(row=6, column=1)
btnOpenParentheses.grid(row=5, column=1)
btnCloseParentheses.grid(row=5, column=3)


root.mainloop()