from tkinter import messagebox
from customtkinter import *

import os, json, datetime

def now():
	today = datetime.datetime.now()
	month = today.month
	day = today.day
	year = int(str(today.year)[2:])
	hour = today.hour
	minute = today.minute
	if month < 10:
		month = f"0{month}"
	if day < 10:
		day = f"0{day}"
	if year < 10:
		year = f"0{year}"
	if hour < 10:
		hour = f"0{hour}"
	if minute < 10:
		minute = f"0{minute}"
	return f"{month}-{day}-{year} {hour}:{minute}"

def commitment(_dir: str, commit : str):
	msg = f"[{commit}]"
	if commit == "":
		msg = ""
	# os.system(f"git config --global --add safe.directory {_dir}")
	os.system(f"cd {_dir}")
	if os.path.exists("setup.json"):
		file =  open("setup.json", "r")
		data = json.loads(file.read())
		if data == "Error":
			messagebox.showerror("ERROR", "Please add your setup file")
		else:
			# execution = f"git config --global user.name \"{data['name']}\" ;"
			# execution += f" git config --global user.email \"{data['email']}\" ;"
			execution = "git add -A"
			os.system(execution)
			execution = f"git commit -m \"{now()} {msg}\" "
			os.system(execution)
			execution = f"git push origin main"
			os.system(execution)
			messagebox.showinfo("SUCCESS", "Done")
	else:
		messagebox.showerror("ERROR", "Please add your setup file")

def start():
	base = CTk()
	base.title("Easy committer")
	base.geometry("500x150")

	_d = CTkFrame(base)
	CTkLabel(_d, text="Directory:\t", font=("Times New Roman", 25), justify="center").pack(side="left")
	directory = CTkEntry(_d, font=("Courier New", 25))
	directory.pack(expand=True, side="left", fill="x")
	_d.pack(fill='x')

	_c = CTkFrame(base)
	CTkLabel(_c, text="Commit message:\t", font=("Times New Roman", 25), justify="center").pack(side="left")
	commit = CTkEntry(_c, font=("Courier New", 25))
	commit.pack(expand=True, side="left", fill="x")
	_c.pack(fill='x')

	CTkButton(base, text="Commit", command=lambda: commitment(directory.get(), commit.get())).pack(fill="x")

	base.mainloop()

if __name__ == "__main__":
	start()