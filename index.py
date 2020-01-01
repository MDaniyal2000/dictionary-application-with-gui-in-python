from functions import *

# UI Functions

# disable search buttons initially
def disableSearchButtons():
    search_btn.configure(state='disabled')
    advSearch_btn.configure(state='disabled')

# populate list
def populateList():
    try:
        disableSearchButtons()
        clearFields()
        list_box.delete(0, END)
        temp = wordsDictionary.head
        while temp is not None:
            elements = [temp.data['word'], temp.data['meaning']]
            list_box.insert(END, elements)
            temp = temp.next
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# sort list
def sortDictionary():
    try:
        wordsDictionary.sortList()
        populateList()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# add word
def addWord():
    try:
        if w_user.get() == '' or m_user.get() == '':
            messagebox.showinfo('Error', 'Please fill all the fields')
        else:
            if wordsDictionary.simpleSearch(w_user.get()):
                messagebox.showinfo('Error','This word already exists')
                return
            myDict = {}
            myDict['word'] = w_user.get()
            myDict['meaning'] = m_user.get()
            wordsDictionary.insertNode(myDict)
            messagebox.showinfo('Success', 'Added successfully')
            populateList()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# clear text fields
def clearFields():
    try:
        global bool
        bool = False
        w_entry.delete(0, 'end')
        m_entry.delete(0, 'end')
        w_entry.focus_force()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

flagVar = 0

# enable simple search
def enableSimpleSearch():
    try:
        clearFields()

        # popup window
        tempWin = Toplevel(app)
        tempWin.focus_set()
        tempWin.overrideredirect(1)
        x = top_frame.winfo_rootx()
        y = top_frame.winfo_rooty()
        height = top_frame.winfo_height()
        tempWin.geometry('+%d+%d' % (x,y+height))
        tempWin.configure(bg = '#fff')
        tempWin.title('What do you want to search?')

        def forWord():
            global flagVar
            flagVar = 1
            w_entry.configure(state='enabled')
            m_entry.configure(state="disabled")
            tempWin.destroy()
            search_btn.configure(state='normal')
            advSearch_btn.configure(state='disabled')

        def forMeaning():
            global flagVar
            flagVar = 2
            m_entry.configure(state='enabled')
            w_entry.configure(state='disabled')
            tempWin.destroy()
            search_btn.configure(state='normal')
            advSearch_btn.configure(state='disabled')

        lbl_1 = Label(tempWin, text='What do you want to search?', font=('Lato', 12), bg='#fff', width=95)
        lbl_1.pack(side=TOP, pady=(20,10))
        btn_1 = Button(tempWin, text='WORD', font=('Lato', 10), fg='#fff', bg='#3c4245', width=40, command=forWord)
        btn_1.pack(side=LEFT, padx=(70,30), pady=(10, 0), ipady=5)
        btn_2 = Button(tempWin, text='MEANING', font=('Lato', 10), fg='#fff', bg='#3c4245', width=40, command=forMeaning)
        btn_2.pack(side=RIGHT, padx=30, pady=(10, 0), ipady=5)
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# enable advance search
def enableAdvanceSearch():
    try:
        clearFields()

        # popup window
        tempWin = Toplevel(app)
        tempWin.focus_set()
        tempWin.overrideredirect(1)
        x = top_frame.winfo_rootx()
        y = top_frame.winfo_rooty()
        height = top_frame.winfo_height()
        tempWin.geometry('+%d+%d' % (x,y+height))
        tempWin.configure(bg = '#fff')
        tempWin.title('What do you want to advance search?')

        def forWord():
            global flagVar
            flagVar = 1
            w_entry.configure(state='enabled')
            m_entry.configure(state="disabled")
            tempWin.destroy()
            search_btn.configure(state='disabled')
            advSearch_btn.configure(state='normal')

        def forMeaning():
            global flagVar
            flagVar = 2
            m_entry.configure(state='enabled')
            w_entry.configure(state='disabled')
            tempWin.destroy()
            search_btn.configure(state='disabled')
            advSearch_btn.configure(state='normal')

        lbl_1 = Label(tempWin, text='What do you want to advance search?', font=('Lato', 12), bg='#fff', width=95)
        lbl_1.pack(side=TOP, pady=(20,10))
        btn_1 = Button(tempWin, text='WORD', font=('Lato', 10), fg='#fff', bg='#3c4245', width=40, command=forWord)
        btn_1.pack(side=LEFT, padx=(70,30), pady=(10, 0), ipady=5)
        btn_2 = Button(tempWin, text='MEANING', font=('Lato', 10), fg='#fff', bg='#3c4245', width=40, command=forMeaning)
        btn_2.pack(side=RIGHT, padx=30, pady=(10, 0), ipady=5)
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# simple search function
def simpleSearch():
    try:
        global flagVar
        if flagVar == 1:
            searchWord()
        elif flagVar == 2:
            searchMeaning()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# reset fields / enable
def resetFields():
    w_entry.configure(state='enabled')
    m_entry.configure(state='enabled')

# simple search word
def searchWord():
    try:
        if w_user.get() == '':
            messagebox.showinfo('Error', 'Please enter a word to search')
        else:
            list_box.delete(0, END)
            if not wordsDictionary.simpleSearch(w_user.get()):
                messagebox.showinfo('Not Found', 'Sorry the word you are looking for was not found')
            else:
                foundWord = wordsDictionary.simpleSearch(w_user.get())
                elements = [foundWord['word'], foundWord['meaning']]
                list_box.insert(END, elements)
            resetFields()
            disableSearchButtons()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# simple search meaning
def searchMeaning():
    try:
        if m_user.get() == '':
            messagebox.showinfo('Error', 'Please enter the meaning to search')
        else:
            list_box.delete(0, END)
            if not wordsDictionary.simpleSearchMeaning(m_user.get()):
                messagebox.showinfo('Not Found', 'Sorry the meaning you are looking for was not found')
            else:
                foundMeaning = wordsDictionary.simpleSearchMeaning(m_user.get())
                elements = [foundMeaning['word'], foundMeaning['meaning']]
                list_box.insert(END, elements)
            resetFields()
            disableSearchButtons()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# advance search function
def advSearch():
    try:
        global flagVar
        if flagVar == 1:
            advSearchWord()
        elif flagVar == 2:
            advSearchMeaning()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# advance search word
def advSearchWord():
    try:
        if w_user.get() == '':
            messagebox.showinfo('Error', 'Please enter a word to search')
        else:
            list_box.delete(0, END)
            foundedWords = wordsDictionary.advanceSearch(w_user.get())
            if len(foundedWords) < 1:
                messagebox.showinfo('Not Found', 'Sorry the word you are looking for was not found')
            else:
                for foundWord in foundedWords:
                    elements = [foundWord['word'], foundWord['meaning']]
                    list_box.insert(END, elements)
            resetFields()
            disableSearchButtons()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# advance Search Meaning
def advSearchMeaning():
    try:
        if m_user.get() == '':
            messagebox.showinfo('Error', 'Please enter a meaning to search')
        else:
            list_box.delete(0, END)
            foundedMeanings = wordsDictionary.advanceSearchMeaning(m_user.get())
            if len(foundedMeanings) < 1:
                messagebox.showinfo('Not Found', 'Sorry the meaning you are looking for was not found')
            else:
                for foundMeaning in foundedMeanings:
                    elements = [foundMeaning['word'], foundMeaning['meaning']]
                    list_box.insert(END, elements)
            resetFields()
            disableSearchButtons()
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# delete function
def deleteWord():
    try:
        if w_user.get() == '':
            messagebox.showinfo('Error', 'Please enter a word')
        else:
            if wordsDictionary.simpleSearch(w_user.get()):
                result = messagebox.askquestion("Confirmation", "Are you sure you want to delete?", icon='warning')
                if result == 'yes':
                    wordsDictionary.deleteNode(w_user.get())
                    populateList()
            else:
                messagebox.showinfo('Error', 'The word was not found')
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# get selected item from list box
bool = False
def selectedWord(event):
    try:
        global bool
        bool = True
        res = list_box.get(list_box.curselection())
        w_user.set(res[0])
        m_user.set(res[1])
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# update function
def updateWord():
    try:
        global bool
        if bool:
            temp = (w_user.get(), m_user.get())
            if temp[0] == '' or temp[1] == '':
                messagebox.showinfo('Error', 'Please fill all the fields')
            else:
                result = list_box.get(list_box.curselection())
                oldData = (result[0], result[1])
                newData = {'word': w_user.get(), 'meaning': m_user.get()}
                if newData['word'] == oldData[0] and newData['meaning'] == oldData[1]:
                    messagebox.showinfo('Caution', 'You did not make any changes')
                else:
                    current_node = wordsDictionary.head
                    while current_node is not None:
                        if current_node.data['word'] == oldData[0]:
                            current_node.data = newData
                            break
                        current_node = current_node.next
                    bool = False
                    messagebox.showinfo('Success','Data updated successfully')
                    populateList()
        else:
            messagebox.showinfo('Error','Please select data first from the list to make changes')
    except:
        messagebox.showinfo('Exception','Sorry we could not execute this function')

# save to file
def saveToFile():
    try:
        writeToFile()
        messagebox.showinfo('Success', 'Saved in file successfully')
    except:
        messagebox.showinfo('Exception', 'Sorry we could not execute this function')

# UI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
app = Tk()
app.title('Dictionary App')
app.resizable(width=FALSE, height=FALSE)
app.geometry('900x650')

# create all of the main containers
top_frame = Frame(app, bg='#3c4245', pady=20)
middle_frame = Frame(app, bg='#ffffff', pady=20)
list_frame = Frame(app, bg='#eeeeee')
btn_frame = Frame(app, bg='#ffffff', pady=20, padx=10)

# place all the containers
top_frame.pack(side=TOP, fill=X)
middle_frame.pack(side=TOP, fill=X)
list_frame.pack(side=LEFT, fill=Y)
btn_frame.pack(side=LEFT, fill=Y)

# Top Frame

# creating widgets
logo = PhotoImage(file='logo.png')
logo_label = Label(top_frame, image=logo, bg='#3c4245')

heading_label = Label(top_frame, text='Dictionary App', font=('Lato', 32), bg='#3c4245', fg='#ffffff')

# placing widgets
logo_label.pack(side=LEFT, padx=(270,20))
heading_label.pack(side=LEFT)

# Middle Frame

# creating widgets
w_label = Label(middle_frame, text='Word:', bg='#fff', font=('Lato',10))
w_user = StringVar()
w_entry = ttk.Entry(middle_frame, textvariable=w_user, font=('Lato',10), width=55)

m_label = Label(middle_frame, text='Meaning:', bg='#fff', font=('Lato',10))
m_user = StringVar()
m_entry = ttk.Entry(middle_frame, textvariable=m_user, font=('Lato',10), width=65)

add_btn = Button(middle_frame, text='Add Word', bg='#3c4245', fg='#fff', font=('Lato',10), width=16, command=addWord)

# placing widgets
w_label.grid(row=0, sticky='e', padx=(30, 10),pady=(0,6))
w_entry.grid(row=0, column=1, sticky='w', ipady=5, pady=(0,6))
m_label.grid(row=1, sticky='e', padx=(30, 10),pady=(0,6))
m_entry.grid(row=1, column=1, sticky='w', ipady=5, pady=(0,6))
add_btn.grid(row=0, column=2, sticky='e', ipady=6, padx=(80,0))


# ListBox Frame

# creating widgets
list_box = Listbox(list_frame, width=66, height=20, border=0, font=('Lato', 14))
scroll_bar = Scrollbar(list_frame)
scroll_barTwo = Scrollbar(list_frame, orient='horizontal')
list_box.configure(yscrollcommand=scroll_bar.set)
list_box.configure(xscrollcommand=scroll_barTwo.set)
scroll_bar.configure(command=list_box.yview)
scroll_barTwo.configure(command=list_box.xview)

list_box.bind('<<ListboxSelect>>', selectedWord)

# placing widgets
scroll_barTwo.pack(side=TOP, fill=X)
list_box.pack(side=LEFT)
scroll_bar.pack(side=RIGHT, fill=Y)

# Buttons Frame

# creating widgets
read_btn = Button(btn_frame, text='Populate Data', bg='#3c4245', fg='#fff', font=('Lato',10), width=16, command=populateList)
sort_btn = Button(btn_frame, text='Sort Data', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=sortDictionary)
update_btn = Button(btn_frame, text='Update Data', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=updateWord)
save_btn = Button(btn_frame, text='Save To File', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=saveToFile)
mode_btn = Button(btn_frame, text='Enable Search', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=enableSimpleSearch)
mode_btn_Two = Button(btn_frame, text='Enable Adv Search', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=enableAdvanceSearch)
search_btn = Button(btn_frame, text='Search', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=simpleSearch)
advSearch_btn = Button(btn_frame, text='Advance Search', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff', command=advSearch)
delete_btn = Button(btn_frame, text='Delete Data', width=16, font=('Lato', 10), bg='#3c4245', fg='#fff',command=deleteWord)

# placing widgets
read_btn.pack(side=TOP, ipady=(5), pady=(0,3))
sort_btn.pack(side=TOP, ipady=(5), pady=(3))
save_btn.pack(side=TOP, ipady=(5), pady=3)
update_btn.pack(side=TOP, ipady=(5), pady=3)
mode_btn.pack(side=TOP, ipady=(5), pady=3)
search_btn.pack(side=TOP, ipady=(5), pady=3)
mode_btn_Two.pack(side=TOP, ipady=(5), pady=3)
advSearch_btn.pack(side=TOP, ipady=(5), pady=3)
delete_btn.pack(side=TOP, ipady=(5), pady=(3, 0))

readFromFile()
populateList()
app.mainloop()