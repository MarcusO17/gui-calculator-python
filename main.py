from tkinter.font import BOLD
from processing import add, compute
import tkinter as tk

LARGE_FONT_STYLE = ("Helvetica", 40, BOLD)
SMALL_FONT_STYLE = ("Helvetica",16)
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
    buttons_frame = create_buttons_frame(window)
    total_label,label = create_display_labels(display_frame,totalSum,currentSum)
    
    window.mainloop()
    
def create_display_labels(display_frame,totalSum,currentSum):
    total_label =tk.Label(display_frame, text=totalSum, anchor= tk.E, bg = LIGHT_GRAY,
                          fg= LABEL_COLOR, padx=24, font = SMALL_FONT_STYLE)
    total_label.pack(expand=True, fill='both')
    
    label =tk.Label(display_frame, text=currentSum, anchor= tk.E, bg = LIGHT_GRAY,
                          fg= LABEL_COLOR, padx=24, font = LARGE_FONT_STYLE)
    label.pack(expand=True, fill='both')
    
    return total_label,label
    
    
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