import tkinter as tk

# Creating the main Window

window = tk.Tk()

# Setting a Title for The Window

window.title("FaceRec")

# Create a Labeled Widget

label = tk.Label(window, text="Ayubowan")
label.pack()

# Defining a function to change the label text


def change_text():
    label.config(text="ACCESS GRANTED")

    # Create  Button Widget


button = tk.Button(window, text="Click to Proceed", command=change_text)
button.pack()


# Running The Applictation
window.mainloop()

    
