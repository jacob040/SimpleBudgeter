# budgeting.py

import tkinter as tk
from tkinter import ttk
import controller

window = tk.Tk()
window.title('Budgeting')
window.geometry('1080x1920')

#title
title_label = ttk.Label(master = window, text = 'Budgeting software', font = 'Elephant 36 bold')
title_label.pack()

#calculated label
calculated_label = ttk.Label(master = window, text = 'Max amount of money that can be spent every day without going broke: ', font = 'Elephant 18')
calculated_label.pack(padx = 10, pady = 300)

#Input
input_frame = ttk.Frame(master = window)
input_frame.pack()

entry = ttk.Entry(master = input_frame)
entry.pack(side = 'left', padx = 10)

button = ttk.Button(master = input_frame, text = 'Calculate budget', command=lambda: controller.calculate_daily((entry.get()), calculated_label))
button.pack(side = 'right')

#run
window.mainloop()
