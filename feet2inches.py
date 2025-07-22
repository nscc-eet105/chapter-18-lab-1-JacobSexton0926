#Jacob Sexton 7/22/25

import tkinter as tk

class FeetInchesConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Feet and Inches Converter")

        tk.Label(self.window, text="Feet and Inches Converter").grid(row=0, column=0, columnspan=4)

        tk.Label(self.window, text="Feet:").grid(row=1, column=0)
        self.feet_entry = tk.Entry(self.window, width=5)
        self.feet_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Inches:").grid(row=1, column=2)
        self.inches_entry = tk.Entry(self.window, width=5)
        self.inches_entry.grid(row=1, column=3)

        tk.Label(self.window, text="Inches:").grid(row=2, column=0)
        self.output_label = tk.Label(self.window, text="", width=10)
        self.output_label.grid(row=2, column=1)

        tk.Button(self.window, text="Convert", command=self.convert).grid(row=3, column=0)
        tk.Button(self.window, text="Exit", command=self.window.quit).grid(row=3, column=1)

        self.window.mainloop()

    def convert(self):
        try:
            feet = int(self.feet_entry.get())
            inches = int(self.inches_entry.get())
            total_inches = feet * 12 + inches
            self.output_label.config(text=str(total_inches))
        except ValueError:
            self.output_label.config(text="Error")

FeetInchesConverter()
