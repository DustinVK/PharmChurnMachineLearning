import tkinter as tk
from joblib import load

lr = load('lr-model.joblib')
print(lr.predict([[0.0,0.0,2.0,0.0,0.0,1.0,2.0,2.0,0.0,0.0,0.0,17.2,0.0,0.0,0.0,0.0,0.0,15.48,1,0.0,1.0,0.0]]))


window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="black",
)

label.pack()
entry.pack()
button.pack()


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    name = entry.get()
    print(name)
    print(event.char)

def handle_button(event):
    name = entry.get()
    print(name)

button.bind("<Button-1>", handle_button)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()
print(lr.predict([[0.0,0.0,2.0,0.0,0.0,1.0,2.0,2.0,0.0,0.0,0.0,17.2,0.0,0.0,0.0,0.0,0.0,15.48,1,0.0,1.0,0.0]]))

