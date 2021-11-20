from processing import expResolver
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Calculator")
    #window.attributes('-alpha', 0.5)
    window.resizable(0,0)
    window.geometry("620x340")
    
    input_frame = tk.Frame(window, width=620, height=50, bd=0,bg="grey", highlightbackground="black", highlightcolor="black", highlightthickness=2)
    input_frame.pack(side= tk.TOP)
    
    
    window.mainloop()
    
    
    
    

if __name__ == "__main__":
    main()