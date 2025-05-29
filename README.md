<h1>🔐 Password Generator – Tkinter GUI App</h1>

 ### [YouTube Demonstration](https://youtube.com/@KeenenX)

<h2>Description</h2>

This is a simple yet powerful Password Generator built with Python and Tkinter. It allows users to:

🔢 Choose the desired password length

🔁 Generate strong, random passwords using ASCII characters (including letters, numbers, and symbols)

📋 Instantly copy the generated password to the clipboard with one click

The goal is to make secure password creation fast, easy, and user-friendly through an intuitive graphical interface. This project is perfect for beginners learning Python, GUI development, or anyone who needs quick, strong password generation.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python 3.13.3</b> 
- <b>Tkinter</b>

<h2>Environments Used </h2>

- <b>Windows 11</b>

<h2>Program walk-through:</h2>

<p align="center">
📸 Step 1: Importing Libraries and Creating the GUI Window: <br/>
<img src="https://i.imgur.com/BJjxvWX.png" height="80%" width="80%" alt="Password generator Steps"/>
<br /> 💬 "We import tkinter to create the GUI and randint to generate random characters. Then we create the main application window, give it a title, and set its size to 400x400 pixels."
<br />
<br /> 
 
 <br />
📸 Step 2: Defining the Password Generator Function
<br/>
<img src="https://i.imgur.com/uR6dvqq.png" height="80%" width="80%" alt="Password generator Steps"/>
<br /> 💬 "The new_rand() function creates a strong random password by looping through the length entered by the user. It uses ASCII values from 33 to 126 to include letters, numbers, and symbols. The password is then displayed in the output box."
<br />
<br /> 
 


<br />
📸 Step 3: Adding Clipboard Support
<br/>
<img src="https://i.imgur.com/9vD9l97.png" height="80%" width="80%" alt="Password generator Steps"/>
<br /> 💬 "The clipper() function lets the user copy the generated password directly to their clipboard with a single click. Super useful for quickly using the password!"
<br />
<br /> 
 


<br />
📸 Step 4: Input for Password Length
<br/>
<img src="https://i.imgur.com/E6D7in7.png" height="80%" width="80%" alt="Password generator Steps"/>
<br />💬 "We add a label frame asking how many characters the password should have. Below that, an entry box lets the user type in their desired password length."
<br />
<br /> 
 


<br />
📸 Step 5: Output Box for the Generated Password
<br/>
<img src="https://i.imgur.com/NKZ9IXV.png" height="80%" width="80%" alt="Password generator Steps"/>
<br /> 💬 "This entry box is where the generated password will appear after clicking the button. It’s styled with no border and blends into the background."
<br />
<br /> 
 


 <br />
📸 Step 6: Buttons for Generating and Copying Passwords  <br/>
<img src="https://i.imgur.com/NFMQp7Z.png" height="80%" width="80%" alt="Password generator Steps"/>
<br /> 💬 "We create two buttons: one to generate the password and another to copy it to the clipboard. Both are placed neatly inside a frame for better layout."
<br />
<br /> 
 


 <br />
📸 Step 7: Running the App  <br/>
<img src="https://i.imgur.com/FecTYcW.png" height="80%" width="80%" alt="Password generator Steps"/>
<br /> 💬 "Finally, root.mainloop() runs the application and keeps the window open, waiting for user interaction. This is the main loop of our Tkinter app."
<br /> 
<br />
 


<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
