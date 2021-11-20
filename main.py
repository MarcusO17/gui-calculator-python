from processing import expResolver
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Calculator")
    #window.attributes('-alpha', 0.5)
    
    
    #btns_frame = tk.Frame(window, width=620, height =320, bg = "black")

    clear = tk.Button(window ,text = "Clear", fg = "white", width = 25, height = 3, bd = 0, bg = "#000000", cursor = "hand2")
    divide = tk.Button(window,text = "÷", fg = "white", width = 25, height = 3, bg = "#000000", cursor = "hand2")
    
    seven = tk.Button(window,text = "7", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    eight = tk.Button(window,text = "8", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    nine = tk.Button(window,text = "9", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    
    four = tk.Button(window,text = "4", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    five = tk.Button(window,text = "5", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    six = tk.Button(window,text = "6", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    
    one = tk.Button(window,text = "1", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    two = tk.Button(window,text = "2", fg = "white", width =12, height = 3, bg = "#000000", cursor = "hand2")
    three = tk.Button(window,text = "3", fg = "white", width = 12, height = 3, bg = "#000000", cursor = "hand2")
    
    
    #clear.grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 1)
    #divide.grid(row = 0, column = 1, columnspan = 1, padx = 1, pady = 1)
    
    seven.grid(row = 1, column = 0, columnspan = 1, padx = 1, pady = 1)
    eight.grid(row = 1, column = 1, columnspan = 1, padx = 1, pady = 1)
    nine.grid(row = 1, column = 2, columnspan = 1, padx = 1, pady = 1)
    
    four.grid(row = 2, column = 0, columnspan = 1, padx = 1, pady = 1)
    five.grid(row = 2, column = 1, columnspan = 1, padx = 1, pady = 1)
    six.grid(row = 2, column = 2, columnspan = 1, padx = 1, pady = 1)
    
    one.grid(row = 3, column = 0, columnspan = 1, padx = 1, pady = 1)
    two.grid(row = 3, column = 1, columnspan = 1, padx = 1, pady = 1)
    three.grid(row = 3, column = 2, columnspan = 1, padx = 1, pady = 1)
    
    window.mainloop()
    
    
    
    

if __name__ == "__main__":
    main()