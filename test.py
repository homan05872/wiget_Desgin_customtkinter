import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode('dark')
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0)
        
        self.textentry = customtkinter.CTkEntry(master=self.frame, width=400)
        self.textentry.grid(row=0, column=0, padx=20, pady=30)
        
        self.textbox = customtkinter.CTkTextbox(master=self.frame, padx=50, width=400)
        self.textbox.grid(row=1, column=0, pady=(0, 30), sticky="nsew")


app = App()
app.mainloop()