import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=5)

'''TOP Labels'''
appName = tk.Label(root, text="Words", font="Raleway")
appName.grid(column=1, row=0)

instructions = tk.Label(root, text="Generate a .txt file with 25 words or 400 words", font="Raleway")
instructions.grid(column=1, row=1)
'''TOP Labels'''

'''Category Select Listbox'''
listbox_frame = tk.Frame(root)
scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")

categoryBox = tk.Listbox(listbox_frame, selectmode="multiple", yscrollcommand=scrollbar.set)
categoryBox.insert(1, "Python")
categoryBox.insert(2, "Perl")
categoryBox.insert(3, "C")
categoryBox.insert(4, "PHP")
categoryBox.insert(5, "JSP")
categoryBox.insert(6, "Ruby")
categoryBox.insert(7, "Python")
categoryBox.insert(8, "Perl")
categoryBox.insert(9, "C")
categoryBox.insert(10, "PHP")
categoryBox.insert(11, "JSP")
categoryBox.insert(12, "Ruby")

scrollbar.config(command=categoryBox.yview())
scrollbar.pack(side="right", fill="y")
categoryBox.pack()
listbox_frame.grid(column=1, row=2)
'''Category Select '''

'''Generator Words Button '''
def generateWords1():
    selections = []

    for item in categoryBox.curselection():
        selections.append(str(categoryBox.get(item)))

    print(selections, "\n Generate 25 Words")

def generateWords2():
    selections = []

    for item in categoryBox.curselection():
        selections.append(str(categoryBox.get(item)))

    print(selections, "\n Generate 400 Words")

genButtonsFrame = tk.Frame(root)
generateWords1_btn = tk.Button(genButtonsFrame, text="Generate 25 Words", command=generateWords1, fg="Red")
generateWords1_btn.pack(side="left")

generateWords2_btn = tk.Button(genButtonsFrame, text="Generate 400 Words", command=generateWords2, fg="Blue")
generateWords2_btn.pack(side="right")

genButtonsFrame.grid(column=1, row=3)
'''Generator Words Button '''


root.mainloop()
