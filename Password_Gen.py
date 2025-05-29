from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("400x400")

my_password = chr(randint(33, 126))

# Generate random Strong Password
def new_rand():
    # Clear the entry box
    pw_entry.delete(0, END)  

    # Get PW Length and convert to integer
    pw_length = int(my_entry.get())

    # Create a variable to hold the password
    my_password = ""

    # Loop through the range of the password length
    for x in range(pw_length):
        # Generate a random character and add it to the password
        my_password += chr(randint(33, 126))
        
    # Output the password to the screen
    pw_entry.insert(0, my_password)


# Copy to Clipboard
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    
    # Copy the password to the clipboard
    root.clipboard_append(pw_entry.get())
    

# Label Frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

# Create Box To Designate Number of Characters
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create Entry Box For Our Returned Password
pw_entry = Entry(root, text=' ', font=("Helvetica", 24), bd=0, bg="systembuttonface")

pw_entry.pack(pady=20)

# Create a frame for our Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)


clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()