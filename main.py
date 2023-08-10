from tkinter import messagebox
from customtkinter import *

import os
import json

def commitment(_dir: str, commit : str):
	os.system(f"cd {_dir}")
	if not os.path.exists("setup.py"):
		file =  open("setup.json", "r")
		data = json.loads(file.read())
		if data == "Error":
			messagebox.showerror("ERROR", "Please add your setup file")
		else:
			os.system(f"git config --global user.name \"{data['name']}\"")
			os.system(f"git config --global user.email \"{data['email']}\"")
			os.system(f"git add .")
			os.system(f"git commit -m \"{commit}\"")
			os.system(f"git push origin main")
	else:
		messagebox.showerror("ERROR", "Please add your setup file")

def start():
	base = CTk()
	base.title("Easy committer")
	base.geometry("500x150")

	_d = CTkFrame(base)
	CTkLabel(_d, text="Directory:\t", font=("Times New Roman", 25), justify="center").pack(expand=True, side="left")
	directory = CTkEntry(_d, font=("Courier New", 25))
	directory.pack(expand=True, side="right")
	_d.pack(fill='x')

	_c = CTkFrame(base)
	CTkLabel(_c, text="Commit message:\t", font=("Times New Roman", 25), justify="center").pack(expand=True, side="left")
	commit = CTkEntry(_c, font=("Courier New", 25))
	commit.pack(expand=True, side="right")
	_c.pack(fill='x')

	CTkButton(base, text="Commit", command=lambda: commitment(directory.get(), commit.get())).pack(fill="x")

	base.mainloop()

if __name__ == "__main__":
	start()