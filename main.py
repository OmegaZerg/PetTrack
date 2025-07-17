import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def main():
    print("Hello from pettrack!")

    root = tb.Window(themename="vapor")
    root.title("PetTrack")
    root.iconbitmap() #Icon path
    root.geometry('800x600')

    # frame = ttk.Frame(root, padding=10)
    # frame.pack(fill=BOTH, expand=YES)

    #Button Functions
    def button_1():
        pass
    def button_2():
        pass

    #Check Box Functions
    def checker():
        if my_checkbox.get() == True:
            pass #do a thing

    #Toggle button
    def toggle_button():
        pass

    #Check Box
    box1 = False
    my_checkbox = tb.Checkbutton(bootstyle=DEFAULT, text="Enable Feature?", variable=box1, onvalue=True, offvalue=False, command=checker)
    my_checkbox.pack(pady=10)

    #Label for whatever; page/section etc.
    page_title = tb.Label(text="Welcome to Pet-Track!", font=("Helvetica", 28), bootstyle=DEFAULT)
    page_title.pack(pady=25)

    page_subtitle = tb.Label(text="Click button 1", font=("Helvetica", 35), bootstyle=DEFAULT)
    page_subtitle.pack(pady=5)

    #Buttons
    b1 = tb.Button(root, text="Button 1", bootstyle=SUCCESS, command=button_1)
    b1.pack(side=LEFT, padx=5, pady=10)

    b2 = tb.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE), command=button_2)
    b2.pack(side=RIGHT, padx=5, pady=10)

    #Toggle Button
    toggle1 = tb.Checkbutton(bootstyle="success-round-toggle", text="Turn something on/off", onvalue=True, offvalue=False, command=toggle_button)
    toggle1.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
