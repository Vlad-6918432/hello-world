import tkinter

def handler1(event):
    print('hello world x= ', event.x, 'y=', event.y)
def handler2(event):
    exit()

root = tkinter.Tk()
text = tkinter.Text()
hello_label = tkinter.Label(root, text = "Hello world",font = "times 16")
hello_label.pack()

hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-2>',handler2)

root.mainloop()
print('End')