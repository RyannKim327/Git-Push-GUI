from tkinter import messagebox
from customtkinter import *

import os
import json

def commitment(commit : str):
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

	CTkLabel(base, text="Enter your commit message", font=("Times New Roman", 25), justify="center").pack(fill="x")

	commit = CTkEntry(base, font=("Courier New", 25))
	commit.pack(fill="x")

	CTkButton(base, text="Commit", command=lambda: commitment(commit.get())).pack(fill="x")

	base.mainloop()

if __name__ == "__main__":
	start()