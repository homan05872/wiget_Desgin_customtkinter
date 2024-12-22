from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter TextBox')
root.geometry('700x300')

my_entry = customtkinter.CTkEntry(root)
my_entry.pack(pady=20)

# TextBoxの'dark'モードデザイン
dark_text = customtkinter.CTkTextbox(root,
	border_width=2,
	border_color="#565B5E",
	# width=600,
	# height=200,
	# corner_radius=1,
	# border_spacing=2,
	# font=("Helvetica", 18),
	fg_color="#343638",
	text_color="white",
	wrap="word", # Char default, word, none
	activate_scrollbars = True,
	scrollbar_button_color="gray",
	scrollbar_button_hover_color="darkgray",
	)

# TextBoxの'light'モードデザイン
light_text = customtkinter.CTkTextbox(root,
	border_width=2,
	border_color="#979DA2",
	# width=600,
	# height=200,
	# corner_radius=1,
	# border_spacing=2,
	# font=("Helvetica", 18),
	# text_color="white",
	fg_color="white",
	wrap="word", # Char default, word, none
	activate_scrollbars = True,
	scrollbar_button_color="gray",
	scrollbar_button_hover_color="darkgray",
	)

light_text.pack(pady=20)
dark_text.pack(pady=20)


thing = ''

# Functions
def delete():
	dark_text.delete(0.0, 'end')

def copy():
	global thing
	thing = dark_text.get(0.0, 'end')

def paste():
	if thing:
		dark_text.insert('end', thing)
	else:
		dark_text.insert('end', "There is nothing to paste!!")

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_frame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_frame, text="Paste", command=paste)

delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1, padx=10)
paste_button.grid(row=0, column=2)

root.mainloop()