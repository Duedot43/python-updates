#!/bin/bash
import os
cwd = os.getcwd()
#import sys
import webbrowser
import subprocess
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from tkinter import *
master = Tk()
var = IntVar()
var.set(1)

def quit_loop():
    print("Selection:",var.get())
    global selection
    selection = var.get()
    master.quit()

Label(master, text = "Select an Option").grid(row=0, sticky=W)
Radiobutton(master, text = "Reset world", variable=var, value = 1).grid(row=1, sticky=W)
Radiobutton(master, text = "Reset nether", variable=var, value = 2).grid(row=2, sticky=W)
Radiobutton(master, text = "Configure server.prop", variable=var, value = 3).grid(row=3, sticky=W)
Radiobutton(master, text = "Add a plugin", variable=var, value = 4).grid(row=4, sticky=W)
Radiobutton(master, text = "Add a world file", variable=var, value = 5).grid(row=5, sticky=W)
Radiobutton(master, text = "Backup world", variable=var, value = 6).grid(row=5, sticky=W)
#ask the dev
#modded version
Radiobutton(master, text = "Start Server", variable=var, value = 7).grid(row=6, sticky=W)
Button(master, text = "GO!", command=quit_loop).grid(row=8, sticky=W)

master.mainloop()

if selection == 1:
    os.system("cd server ; rm -rf world")
if selection == 2:
    os.system("cd server ; rm -rf world_nether")
if selection == 3:
    os.system("cd server ; open server.properties /System/Applications/TextEdit.app")
if selection == 4:
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    subprocess.call(["cp", file_path, "server/plugins"])
if selection == 5:
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    subprocess.call(["cd", "server", ";", "cp", file_path, "."])
if selection == 6:
    root = tk.Tk()
    root.withdraw()
    box2 = messagebox.askquestion(title='Backup folder', message='please select the folder on what you wish to backup your world file !WARNING! this is a beta feture this will probobly not work use at your own risk do you wish to continue?',icon = 'warning')
    if box2 == 'yes':
        file_path = filedialog.askdirectory()
        print(file_path)
        subprocess.run(["cd", "server", ";", "cp", "-r", "world", file_path])
        os.system("cd server ; cp -r world %s"%file_path)
MsgBox = tk.messagebox.askquestion ('Use Ngrok?','Do you want to use ngrok or be guided to server.properties to configure your server? this will not work if the derectory that this app is in has spaces',icon = 'warning')
if MsgBox == 'yes':
    cwd = os.getcwd()
    quotes = "'"
    cwd2 = quotes + cwd + quotes
    print (cwd2)
    print (cwd)
    #cwd2 = cwd"/start.command"
    #out = subprocess.call(['osascript', '-e', "\'tell", "app", '\"Terminal\"', "to", "do", "script", '\"echo hello\"\''])
    os.system("osascript -e \'tell app \"Terminal\" to do script \"cd %s ; ./ngrok tcp 25565\"\'"%cwd)
    
if MsgBox == 'no':
    os.system("cd server ; open server.properties /System/Applications/TextEdit.app") 
os.system("git clone https://github.com/Duedot43/update.git ; cd update ; cp update.txt ..")
updates = ()
#git hub crap i will add later
update = open('update.txt','r')
for line in update:
    updates = line.strip()
os.system("rm -rf update ; rm update.txt")
if updates == '1':
    messagebox.showinfo(title='Update!', message='there is an update')
    os.system('cd server ; git clone https://github.com/Duedot43/minecraft-update.git ; rm papper.jar ; cd minecraft-update ; cp papper.jar .. ; cd .. ; rm -rf minecraft-update')
box = messagebox.askquestion(title='Start Server?', message='Start The Server?')
if box == 'yes':
    #subprocess.call(["cd", "server", ";", "./start_server.command"])
    os.system("cd server ; java -Xmx2G -Xms2G -jar papper.jar")
    exit()
if box == 'no':
    exit()
