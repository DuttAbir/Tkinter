import tkinter as tk

DEFAULT_FONT_STYLE=("Ariel",20)
WHITE = ("#FFFFFF")
OFF_WHITE= ("#F8FAFF")
LIGHT_GRAY = ("#F5F5F5")
LIGHT_BLUE = ("#CCEDFF")
LABEL_COLOUR = ("#25265E")
SMALL_FONT_STYLE= ("Ariel",16)
LARGE_FONT_STYLE = ("Ariel",40,"bold")
DIGITS_FONT_STYLE = ("Ariel",24,"bold")



class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.operatios= {"/":"\u00F7","*": "\u00D7","-":"-", "+":"+"}
        self.button_frame = self.create_button_frame()

        self.button_frame.rowconfigure(0, weight=1)

        for x in range (1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)

        self.create_digits_buttons()
        self.create_operator_buttoms()
        self.create_spacial_buttons()

    def create_spacial_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text= self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOUR, padx=24, font=SMALL_FONT_STYLE )
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text= self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOUR, padx=24, font=LARGE_FONT_STYLE )
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()



    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOUR, font=DIGITS_FONT_STYLE, borderwidth=0, command= lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttoms(self):
        i = 0
        for operator, symbol in self.operatios.items():
            button=tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0 , command= lambda x = operator : self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1


    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_total_label()
        self.update_label()

    def create_clear_button(self):
        button=tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1,columnspan=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression=""
        self.update_label()



    def create_equals_button(self):
        button=tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)


    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame


    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)



    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    calc = calculator()
    calc.run()

