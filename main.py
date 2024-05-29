#!/user/bin/env python3

from func import *
import tkinter as tk
from tkinter import filedialog
from os.path import exists

def verify(operation, key, source):
    # Verify Key Size
    error = False
    if len(key) not in [16, 24, 32]:
        key_dynamic_warning_var.set("Error: Invalid Key Size. Only sizes 16, 24, & 32 accepted.")
        error = True
    else:
        key_dynamic_warning_var.set("")

    # Verify Operation input
    if operation not in ["Encrypt", "Decrypt"]:
        radio_warning_var.set("Missing operation.")
        error = True
    else:
        radio_warning_var.set("")

    # Verify file path
    if len(source) == 0:
        file_path_var.set('File not selected.')
        file_path_label.config(fg='red')
    else:
        file_path_label.config(fg='')

    return error

def encrypt_decrypt():

    # Get operation, key, and file path
    operation = operation_var.get()
    key = key_entry.get().encode()
    source = file_path_var.get()


    error = verify(operation, key, source)

    # Return if error exist
    if error:
        return

    # Encrypt or Decrypt the file
    if operation == "Encrypt":
        encrypt_file(source, key)
    elif operation == "Decrypt":
        decrypt_file(source, key)

def select_file():
    file_path = filedialog.askopenfilename()
    file_path_var.set(file_path)
    file_path_label.config(fg='black')

root = tk.Tk()
root.title('Local-File-Encryption Tool')

# Title
title = tk.Label(root, text="Local-File-Encryption Tool")
title.grid(row=0, column=0)
spacer = tk.Label(root).grid(row=1, column=0)

# Radio buttons for operation
operation_var = tk.StringVar()
operation_label = tk.Label(root, text="Select Operation:")
operation_label.grid(row=2, column=0, sticky='w')
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=operation_var, value="Encrypt")
encrypt_radio.grid(row=3, column=0, sticky='w')
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=operation_var, value="Decrypt")
decrypt_radio.grid(row=4, column=0, sticky='w')
radio_warning_var = tk.StringVar()
radio_warning = tk.Label(root, textvariable=radio_warning_var, fg='red')
radio_warning.grid(row=5, column=0, sticky='w')

# Key input
key_label = tk.Label(root, text="Enter key:")
key_label.grid(row=6, column=0, sticky='w')
key_entry = tk.Entry(root)
key_entry.grid(row=7, column=0, sticky='w')
key_static_warning = tk.Label(root, text="Key must be size 16, 24, or 32.")
key_static_warning.grid(row=8, column=0, sticky='w')
key_dynamic_warning_var = tk.StringVar()
key_dynamic_warning = tk.Label(root, textvariable=key_dynamic_warning_var, fg='red')
key_dynamic_warning.grid(row=9, column=0)

# File Selection
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.grid(row=10, column=0, sticky='w')
file_path_var = tk.StringVar()
file_path_label = tk.Label(root, textvariable=file_path_var)
file_path_label.grid(row=11, column=0, sticky='w')

# Submit
submit_button = tk.Button(root, text="Submit", command=encrypt_decrypt)
submit_button.grid(row=12, column=0, sticky='w')

root.mainloop()

