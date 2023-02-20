import tkinter as tk

exp = ""

def addToExp(digit, txtExp):
    global exp
    exp += str(digit)
    txtExp.delete(1.0,"end")
    txtExp.insert(1.0, exp)

def evaluateExp(txtExp):
    global exp
    try:
        result = str(eval(exp))
        exp = ""
        txtExp.delete(1.0, "end")
        txtExp.insert(1.0, result)
    except:
        clearExp(txtExp)
        txtExp.insert(1.0,"Err")


def clearExp(txtExp):
    global exp
    exp = ""
    txtExp.delete(1.0,"end")


def main():

    window = tk.Tk()
    window.geometry("320x320")

    txtExp = tk.Text(window, height=2, width=15, font=("Consolas",24))
    txtExp.grid(columnspan=12)


    btn_1 = tk.Button(window, text="1", command=lambda : addToExp(1,txtExp), width=5, font=("Consolas", 14))
    btn_1.grid(row=2, column=1)
    btn_2 = tk.Button(window, text="2", command=lambda : addToExp(2,txtExp), width=5, font=("Consolas", 14))
    btn_2.grid(row=2, column=2)
    btn_3 = tk.Button(window, text="3", command=lambda : addToExp(3,txtExp), width=5, font=("Consolas", 14))
    btn_3.grid(row=2, column=3)
    btn_4 = tk.Button(window, text="4", command=lambda : addToExp(4,txtExp), width=5, font=("Consolas", 14))
    btn_4.grid(row=3, column=1)
    btn_5 = tk.Button(window, text="5", command=lambda : addToExp(5,txtExp), width=5, font=("Consolas", 14))
    btn_5.grid(row=3, column=2)
    btn_6 = tk.Button(window, text="6", command=lambda : addToExp(6,txtExp), width=5, font=("Consolas", 14))
    btn_6.grid(row=3, column=3)
    btn_7 = tk.Button(window, text="7", command=lambda : addToExp(7,txtExp), width=5, font=("Consolas", 14))
    btn_7.grid(row=4, column=1)
    btn_8 = tk.Button(window, text="8", command=lambda : addToExp(8,txtExp), width=5, font=("Consolas", 14))
    btn_8.grid(row=4, column=2)
    btn_9 = tk.Button(window, text="9", command=lambda : addToExp(9,txtExp), width=5, font=("Consolas", 14))
    btn_9.grid(row=4, column=3)
    btn_0 = tk.Button(window, text="0", command=lambda : addToExp(0,txtExp), width=5, font=("Consolas", 14))
    btn_0.grid(row=5, column=2)

    btn_add = tk.Button(window, text=" + ", command=lambda: addToExp(" + ", txtExp), width=5, font=("Consolas", 14))
    btn_add.grid(row=2, column=4)
    btn_subtract = tk.Button(window, text=" - ", command=lambda: addToExp(" - ", txtExp), width=5, font=("Consolas", 14))
    btn_subtract.grid(row=3, column=4)
    btn_divide = tk.Button(window, text=" / ", command=lambda: addToExp(" / ", txtExp), width=5, font=("Consolas", 14))
    btn_divide.grid(row=4, column=4)
    btn_multiply = tk.Button(window, text=" x ", command=lambda: addToExp(" * ", txtExp), width=5, font=("Consolas", 14))
    btn_multiply.grid(row=5, column=4)

    btn_leftBracket = tk.Button(window, text= "(", command=lambda: addToExp(" ( ", txtExp), width=5, font=("Consolas", 14))
    btn_leftBracket.grid(row=5, column=1)
    btn_rightBracket = tk.Button(window, text=")", command=lambda: addToExp(" ) ", txtExp), width=5, font=("Consolas", 14))
    btn_rightBracket.grid(row=5, column=3)

    btn_equals = tk.Button(window, text="=",command=lambda: evaluateExp(txtExp), width=10, font=("Consolas", 14))
    btn_equals.grid(row=6, column=1,columnspan=2)
    btn_clear = tk.Button(window, text="C",command=lambda: clearExp(txtExp), width=10, font=("Consolas", 14))
    btn_clear.grid(row=6, column=3,columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    main()