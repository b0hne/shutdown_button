#!/usr/bin/python3
#based on https://github.com/scruss/shutdown_button
use_button=27

from gpiozero import Button
from signal import pause
from subprocess import check_call
from tkinter import *

held_for=0.0

def rls():
    root = Tk()
    frame = Frame(root)
    label = Label(root, font=("Courier 16 bold"), text="shut down")
    label.pack()
    root.mainloop()


def hld():
    global held_for
    held_for = max(held_for, button.held_time + button.hold_time)
root = Tk()
frame = Frame(root)
label = Label(root, font=("Courier 16 bold"), text="s-hut down")
label.pack()
root.mainloop()

button=Button(use_button, hold_time=0.05, hold_repeat=True)
button.when_held = hld
button.when_released = rls

pause() # wait forever
