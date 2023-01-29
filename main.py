from io import DEFAULT_BUFFER_SIZE
from tkinter.font import BOLD
from processing import add, compute
import tkinter as tk

LARGE_FONT_STYLE = ("Helvetica", 40,BOLD)
SMALL_FONT_STYLE = ("Helvetica",16)
DIGITS_FONT_STYLE = ("Helvetica",24,BOLD)
DEFAULT_FONT_SIZE =("Helvetica", 20)
OFF_WHITE = ("#F8FAFF")
WHITE = ("#FFFFFF")
LIGHT_BLUE =("#CCEDFF")
LABEL_COLOR = "#25265E"
LIGHT_GRAY = "#F5F5F5"


def main():
    window = tk.Tk()
    window.geometry("375x667")
    window.title("Calculator")
    window.resizable(0,0)
    
    totalSum = "0"
    currentSum = "0"
    
    display_frame = create_display_frame(window)
    
    digits = {
        7:(1,1), 8:(1,2), 9:(1,3),
        4:(2,1), 5:(2,2), 6:(2,3),
        1:(3,1), 2:(3,2), 3:(3,3),
        0:(4,2), '.':(4,1)
    }
    
    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    
    buttons_frame = create_buttons_frame(window)
    
    total_label,label = create_display_labels(display_frame,totalSum,currentSum)
    
    buttons_frame.rowconfigure(0,weight=1)
    for x in range (1,5):
        buttons_frame.rowconfigure(x,weight=1)
        buttons_frame.columnconfigure(x,weight=1)
        
    create_digit_buttons(digits, buttons_frame)
    create_special_button(buttons_frame)
    create_operator_buttons(operations,buttons_frame)
    
    
    window.mainloop()
    
def create_display_labels(display_frame,totalSum,currentSum):
    total_label =tk.Label(display_frame, text=totalSum, anchor= tk.E, bg = LIGHT_GRAY,
                          fg= LABEL_COLOR, padx=24, font = SMALL_FONT_STYLE)
    total_label.pack(expand=True, fill='both')
    
    label =tk.Label(display_frame, text=currentSum, anchor= tk.E, bg = LIGHT_GRAY,
                          fg= LABEL_COLOR, padx=24, font = LARGE_FONT_STYLE)
    label.pack(expand=True, fill='both')
    
    return total_label,label

def create_special_button(buttons_frame):
    create_clear_button(buttons_frame)
    create_equals_button(buttons_frame)

def create_operator_buttons(operations,buttons_frame):
    i = 0
    for operator,symbol in operations.items():
        button = tk.Button(buttons_frame, text=symbol, bg =OFF_WHITE, fg =LABEL_COLOR,font=DEFAULT_FONT_SIZE,borderwidth= "0")
        button.grid(row=i , column=4, sticky=tk.NSEW)
        i += 1
        
def create_digit_buttons(digits, buttons_frame):
    for digit,grid_value in digits.items():
        button = tk.Button(buttons_frame, text=str(digit), bg =WHITE, fg =LABEL_COLOR,font=DIGITS_FONT_STYLE,borderwidth= "0")
        button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
    
def create_clear_button(buttons_frame):
    button = tk.Button(buttons_frame, text="C", bg =OFF_WHITE, fg =LABEL_COLOR,font=DEFAULT_FONT_SIZE,borderwidth= "0")
    button.grid(row=0 , column=1, columnspan= 3,sticky=tk.NSEW)

def create_equals_button(buttons_frame):
    button = tk.Button(buttons_frame, text="=", bg =LIGHT_BLUE, fg =LABEL_COLOR,font=DEFAULT_FONT_SIZE,borderwidth= "0")
    button.grid(row=4 , column=3, columnspan= 2,sticky=tk.NSEW)
    
def create_display_frame(window):
    frame = tk.Frame(window, height=221,bg = LIGHT_GRAY)
    frame.pack(expand =True, fill='both')
    return frame
    
def create_buttons_frame(window):
    frame = tk.Frame(window)
    frame.pack(expand =True, fill='both')
    return frame 
     
if __name__ == "__main__":
    main() 