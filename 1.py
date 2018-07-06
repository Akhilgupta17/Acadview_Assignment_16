from tkinter import *
root = Tk()
frame = Frame(root, bg='skyblue')
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(frame, yscrollcommand = scrollbar.set )
dict={"1":8796052341,"2":9568225077,"3":9876543210,"4":987654321,"5":8976543210,"6":79876543210,"7":6098765432,"8":6785904321,"9":1234567890,\
      "10":6789054321 }
for item in dict:
    mylist.insert(END,"Key Is : " + str(item))
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
mainloop()
