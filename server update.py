#!/bin/bash
import os
import webbrowser
import subprocess
from tkinter import messagebox
os.system('./ngrok tcp 25565')
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
messagebox.showinfo(title='Go!', message='Starting server!')
os.system('cd server ; java -Xmx1024M -Xms1024M -jar papper.jar')
