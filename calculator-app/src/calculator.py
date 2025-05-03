from tkinter import Tk, StringVar, Entry, Button

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.configure(bg="black")

        self.entry_value = ''
        self.equation = StringVar()

        # Configure row and column weights
        for i in range(6):  # 0 to 5 rows
            self.master.rowconfigure(i, weight=1)
        for i in range(4):  # 0 to 3 columns
            self.master.columnconfigure(i, weight=1)

        # Display Entry
        Entry(
            self.master, textvariable=self.equation, font=('Arial', 24),
            bd=0, justify='right', bg="black", fg="white"
        ).grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Buttons layout
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('C', 1, 0, '#a5a5a5', 'black'), ('±', 1, 1, '#a5a5a5', 'black'), ('%', 1, 2, '#a5a5a5', 'black'), ('/', 1, 3, '#ff9500', 'white'),
            ('7', 2, 0, '#333333', 'white'), ('8', 2, 1, '#333333', 'white'), ('9', 2, 2, '#333333', 'white'), ('*', 2, 3, '#ff9500', 'white'),
            ('4', 3, 0, '#333333', 'white'), ('5', 3, 1, '#333333', 'white'), ('6', 3, 2, '#333333', 'white'), ('-', 3, 3, '#ff9500', 'white'),
            ('1', 4, 0, '#333333', 'white'), ('2', 4, 1, '#333333', 'white'), ('3', 4, 2, '#333333', 'white'), ('+', 4, 3, '#ff9500', 'white'),
            ('0', 5, 0, '#333333', 'white'), ('.', 5, 2, '#333333', 'white'), ('=', 5, 3, '#ff9500', 'white')
        ]

        for (text, row, col, bg, fg) in buttons:
            if text == '0':
                Button(
                    self.master, text=text, bg=bg, fg=fg, font=('Arial', 18),
                    relief='flat', command=lambda t=text: self.show(t)
                ).grid(row=row, column=col, columnspan=2, padx=1, pady=1, sticky="nsew")
            elif text == '=':
                Button(
                    self.master, text=text, bg=bg, fg=fg, font=('Arial', 18),
                    relief='flat', command=self.solve
                ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            elif text == 'C':
                Button(
                    self.master, text=text, bg=bg, fg=fg, font=('Arial', 18),
                    relief='flat', command=self.clear
                ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            elif text == '±':
                Button(
                    self.master, text=text, bg=bg, fg=fg, font=('Arial', 18),
                    relief='flat', command=self.toggle_sign
                ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            elif text == '%':
                Button(
                    self.master, text=text, bg=bg, fg=fg, font=('Arial', 18),
                    relief='flat', command=self.percent
                ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            else:
                Button(
                    self.master, text=text, bg=bg, fg=fg, font=('Arial', 18),
                    relief='flat', command=lambda t=text: self.show(t)
                ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set('')

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(str(result))
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

    def toggle_sign(self):
        try:
            if self.entry_value:
                if self.entry_value.startswith('-'):
                    self.entry_value = self.entry_value[1:]
                else:
                    self.entry_value = '-' + self.entry_value
                self.equation.set(self.entry_value)
        except:
            pass

    def percent(self):
        try:
            if self.entry_value:
                result = float(self.entry_value) / 100
                self.entry_value = str(result)
                self.equation.set(self.entry_value)
        except:
            self.equation.set("Error")
            self.entry_value = ''

# Run the app
if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.mainloop()
