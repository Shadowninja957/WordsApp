from Categories import *
from Words import *
import tkinter as tk
import ttkbootstrap as ttk

# categories in a list use the index in listbox to identify the object categories in this list
categories = [Anatomy(),People(),Animal(),Place(),Thing(),Movie(),TvShow(),Anime(),Cartoon(),Music(),Art(),Verb(),Adjective(),Food()
,Drink(),CustomWord(),LeagueOfLegends(),Apex(),Overwatch(),Color(),Astrology()]

category = []

client = WordGeneratorClient()
root = ttk.Window(themename="darkly")

canvas = tk.Canvas(root, width=600, height=500)
canvas.grid(columnspan=3, rowspan=8)

'''TOP Labels'''
appName = tk.Label(root, text="Words", font="Raleway")
appName.grid(column=1, row=0)

# instructions = tk.Label(root, text="Generate a .txt file with 25 words or 400 words", font="Raleway")
# instructions.grid(column=1, row=1)
'''TOP Labels'''

# Generate Words
'''Category Select Listbox'''
listbox_frame = tk.Frame(root)
scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")

categoryBox = tk.Listbox(listbox_frame, selectmode="multiple", yscrollcommand=scrollbar.set)

scrollbar.config(command=categoryBox.yview())
scrollbar.pack(side="right", fill="y")
categoryBox.pack()
'''Category Select '''

'''Generator Words Button '''
def generateWords1():
   list = [categories[int(item)] for item in categoryBox.curselection()]
   client.generateSmallWordPack(str(genEntry.get()), list)

def generateWords2():
    list = [categories[int(item)] for item in categoryBox.curselection()]
    client.generateLargeWordPack(str(genEntry.get()), list)

genEntryFrame = tk.Frame(root,width=200, height=400)

packLabel = tk.Label(genEntryFrame, text="Pack Name")
packLabel.grid(column=2, row=2, padx=5, pady=3, ipadx=10)

genEntry = tk.Entry(genEntryFrame)
genEntry.grid(column=2 ,row=3, padx=5, pady=3, ipadx=10)

genEntryFrame.grid(column=2, row=2, padx=10, pady=5)

genButtonsFrame = tk.Frame(root, width=200, height=500)

generateWords1_btn = ttk.Button(genButtonsFrame, text="Generate 25", command=generateWords1)
generateWords1_btn.grid(column=2, row=4, padx=5, pady=3, ipadx=10)

generateWords2_btn = ttk.Button(genButtonsFrame, text="Generate 400", command=generateWords2)
generateWords2_btn.grid(column=3, row=4, padx=5, pady=3, ipadx=10)

genButtonsFrame.grid(column=2, row=3, padx=10, pady=5)
'''Generator Words Button '''

# Add words
'''Add words listbox'''
listbox_frame2 = tk.Frame(root)
scrollbar2 = tk.Scrollbar(listbox_frame2, orient="vertical")

categoryBox2 = tk.Listbox(listbox_frame2, selectmode="single", yscrollcommand=scrollbar2.set)
for item in categories:
    categoryBox.insert(categories.index(item), item.getCategory())
    categoryBox2.insert(categories.index(item), item.getCategory())

scrollbar2.config(command=categoryBox2.yview())
scrollbar2.pack(side="right", fill="y")
categoryBox2.pack()

listbox_frame.grid(column=2, row=1)
listbox_frame2.grid(column=1, row=1)
'''Add words listbox'''

'''Add words textfield'''
entryFrame = tk.Frame(root, width=200, height=500)

entryLabel = tk.Label(entryFrame, text="Enter words")
entryLabel.grid(column=0, row=2)

entry = tk.Entry(entryFrame, bd=5)
entry.grid(column=0, row=3)

entryFrame.grid(column=1, row=2)
'''Add words textfield'''

'''Add words button'''
def addWords():
    for item in categoryBox2.curselection():
        category.append((categories[int(item)], entry.get()))

def saveWords():
    print("saved")
    for item in category:
        client.wordBank.addWordsToCategory(item[1], item[0])
        client.saveWords()

def deleteWords():
    for item in category:
        if entry.get() is item[1]:
            item = None

addWordsFrame = tk.Frame(root, width=300, height=500) 
addWordsbtn = tk.Button(addWordsFrame, text="Add", command=addWords)
addWordsbtn.grid(column=0, row=4, padx=5, pady=3, ipadx=10)

deleteWordsbtn = tk.Button(addWordsFrame, text="Delete", command=deleteWords)
deleteWordsbtn.grid(column=1, row=4, padx=5, pady=3, ipadx=10)

saveWordsbtn = tk.Button(addWordsFrame, text="Save", command=saveWords)
saveWordsbtn.grid(column=0, row=5, padx=5, pady=3, ipadx=10)

addWordsFrame.grid(column=1, row=3, padx=10, pady=5)

'''Add words button'''

client.loadWords()
root.mainloop()
