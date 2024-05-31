import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    password_length = int(length_entry.get())  
    password = generate_password(password_length)
    password_label.config(text=f"Generated password: {password}")


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Create a button to generate a password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()


root.mainloop()
