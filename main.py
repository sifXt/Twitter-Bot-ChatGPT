import tkinter as tk

from twitter import *

root = tk.Tk()

root.geometry("800x500")

root.iconbitmap('Twitter_Bot/favicon.ico')

root.configure(bg='#1DA1F2')

root.title("Twitter Bot")


btn1 = tk.Button(root, text = "Tweet a fact", font=("Arial",16), command = tweet)
btn1.place(x=325, y=200, height=100, width=150)


root.mainloop()