from Categories import *
from Words import *
import tkinter as tk

# categories in a list use the index in listbox to identify the object categories in this list
categories = [Anatomy(),People(),Animal(),Place(),Thing(),Movie(),TvShow(),Anime(),Cartoon(),Music(),Art(),Verb(),Adjective(),Food()
,Drink(),CustomWord(),LeagueOfLegends(),Apex(),Overwatch(),Color(),Astrology()]

client = WordGeneratorClient()
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=6)

'''TOP Labels'''
appName = tk.Label(root, text="Words", font="Raleway")
appName.grid(column=1, row=0)

instructions = tk.Label(root, text="Generate a .txt file with 25 words or 400 words", font="Raleway")
instructions.grid(column=1, row=1)
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

genButtonsFrame = tk.Frame(root)

genEntry = tk.Entry(genButtonsFrame, bd=5)
genEntry.pack(side="top")

generateWords1_btn = tk.Button(genButtonsFrame, text="Generate 25 Words", command=generateWords1, fg="Red")
generateWords1_btn.pack(side="left")

generateWords2_btn = tk.Button(genButtonsFrame, text="Generate 400 Words", command=generateWords2, fg="Blue")
generateWords2_btn.pack(side="right")

genButtonsFrame.grid(column=1, row=3)
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

listbox_frame.grid(column=1, row=2)
listbox_frame2.grid(column=1, row=4)
'''Add words listbox'''

'''Add words textfield'''
entryFrame = tk.Frame(root)

entryLabel = tk.Label(entryFrame, text="Enter words")
entryLabel.pack(side="top")

entry = tk.Entry(entryFrame, bd=5)
entry.pack(side="bottom")

entryFrame.grid(column=1, row=5)
'''Add words textfield'''

'''Add words button'''
def addWords():
    category=" "
    for item in categoryBox.curselection():
        category = categories[int(item)] 
    client.wordBank.addWordsToCategory(entry.get(), category)

addWordsbtn = tk.Button(root, text="Add Words", command=addWords)
addWordsbtn.grid(column=1, row=6)

'''Add words button'''

client.loadWords()
root.mainloop()
