from processing import add, compute
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Calculator")
    window.resizable(0,0)

    
    #InputFrame
    inputFrame = tk.Label(window, width=81, height =3, bg = "black")
    
    #Operation Buttons
    divide = tk.Button(window,text = "÷", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    multiply = tk.Button(window,text = "x", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    bracketleft = tk.Button(window,text = "(", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2") 
    bracketright = tk.Button(window,text = ")", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    dot = tk.Button(window,text = ".", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    percent = tk.Button(window,text = "%", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    plus = tk.Button(window,text = "+", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    equals = tk.Button(window,text = "=", fg = "white", width = 25, height = 3, bg = "#000000", cursor = "hand2")
    minus = tk.Button(window,text = "-", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    squareRoot = tk.Button(window,text = "√", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    square = tk.Button(window,text = "x²", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    clearEntry = tk.Button(window,text = "CE", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    clear = tk.Button(window,text = "C", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    
    
    #Number Buttons by row
    #Row 2
    seven = tk.Button(window,text = "7", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    eight = tk.Button(window,text = "8", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    nine = tk.Button(window,text = "9", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    #Row 3
    four = tk.Button(window,text = "4", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    five = tk.Button(window,text = "5", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    six = tk.Button(window,text = "6", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    #Row 4
    one = tk.Button(window,text = "1", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    two = tk.Button(window,text = "2", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    three = tk.Button(window,text = "3", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    
    #Row 5
    zero = tk.Button(window,text = "0", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    
    inputFrame.grid(row = 0, column = 0, columnspan = 7, padx = 1, pady = 1 )
    
    seven.grid(row = 2, column = 0, columnspan = 1, padx = 1, pady = 1)
    eight.grid(row = 2, column = 1, columnspan = 1, padx = 1, pady = 1)
    nine.grid(row = 2, column = 2, columnspan = 1, padx = 1, pady = 1)
    divide.grid(row = 2, column =3, columnspan = 1, padx = 1, pady = 1)
    clear.grid(row = 2, column = 4, columnspan = 1, padx = 1, pady = 1)
    clearEntry.grid(row = 2, column = 5, columnspan = 1, padx = 1, pady = 1)
  
    four.grid(row = 3, column = 0, columnspan = 1, padx = 1, pady = 1)
    five.grid(row = 3, column = 1, columnspan = 1, padx = 1, pady = 1)
    six.grid(row = 3, column = 2, columnspan = 1, padx = 1, pady = 1)
    multiply.grid(row = 3, column = 3, columnspan = 1, padx = 1, pady = 1)
    bracketleft.grid(row =3, column = 4, columnspan = 1, padx = 1, pady = 1)
    bracketright.grid(row = 3, column = 5, columnspan = 1, padx = 1, pady = 1)
    
    one.grid(row = 4, column = 0, columnspan = 1, padx = 1, pady = 1)
    two.grid(row = 4, column = 1, columnspan = 1, padx = 1, pady = 1)
    three.grid(row = 4, column = 2, columnspan = 1, padx = 1, pady = 1)
    minus.grid(row = 4, column = 3, columnspan = 1, padx = 1, pady = 1)
    squareRoot.grid(row = 4, column = 4, columnspan = 1, padx = 1, pady = 1)
    square.grid(row = 4, column = 5, columnspan = 1, padx = 1, pady = 1)
    
    zero.grid(row = 5, column = 0, columnspan = 1, padx = 1, pady = 1)
    dot.grid(row = 5, column = 1, columnspan = 1, padx = 1, pady = 1)
    percent.grid(row = 5, column = 2, columnspan = 1, padx = 1, pady = 1)
    plus.grid(row = 5, column = 3, columnspan = 1, padx = 1, pady = 1)
    equals.grid(row = 5, column = 4, columnspan = 3, padx = 1, pady = 1)  
    
    window.mainloop()
    
    
    
    

if __name__ == "__main__":
    main()