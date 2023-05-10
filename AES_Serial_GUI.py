from Crypto.Cipher import AES
from Crypto.Util import Counter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from timeit import default_timer as timer
from ttkthemes import ThemedStyle


# Set the block size for AES encryption (in bytes)
BLOCK_SIZE = 16


# Pad the input text to be a multiple of the block size
def pad(text):
    padding = BLOCK_SIZE - len(text) % BLOCK_SIZE
    padding_char = padding.to_bytes(1, byteorder='big')
    return text + padding * padding_char


# Unpad the input text by removing the padding
def unpad(text):
    padding = ord(text[-1])
    return text[:-padding]


# Encrypt the input text using AES in CTR mode with a counter
def encrypt(key, plaintext):
    # Generate a unique counter value
    counter = Counter.new(BLOCK_SIZE * 8)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    ciphertext = cipher.encrypt(pad(plaintext.encode()))
    return ciphertext.hex()


# Decrypt the input ciphertext using AES in CTR mode with a counter
def decrypt(key, ciphertext):
    # Generate a unique counter value
    counter = Counter.new(BLOCK_SIZE * 8)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    plaintext = unpad(cipher.decrypt(bytes.fromhex(ciphertext)).decode())
    return plaintext


# Define a function to handle the encryption/decryption button click
def process_input():
    # Get the input text and key from the GUI
    input_text = input_text_var.get()
    key = key_var.get()

    # Get the selected option from the GUI
    option = option_var.get()

    # Convert the key string to bytes
    key = bytes.fromhex(key)

    # Check if the key length is valid
    if len(key) not in [16, 24, 32]:
        messagebox.showerror("Error", "Invalid key length.")
    else:
        # Measure the execution time of the encryption/decryption
        start_time = timer()

        # Process the input based on the selected option
        if option == 'Encrypt':
            ciphertext = encrypt(key, input_text)
            output_text_var.set(ciphertext)
        elif option == 'Decrypt':
            plaintext = decrypt(key, input_text)
            output_text_var.set(plaintext)
        else:
            messagebox.showerror("Error", "Invalid option.")

        # Calculate the execution time and update the GUI
        end_time = timer()
        execution_time = end_time - start_time
        execution_time_str = f"Execution time: {execution_time:.6f} seconds"
        execution_time_label.config(text=execution_time_str)


# Create the GUI window
root = tk.Tk()
root.title("AES Encryption/Decryption - Serial")
    
# Create a style for the GUI using the ttkthemes module
style = ThemedStyle(root)
style.set_theme("arc")

# Create the input text label and entry widget
input_text_label = ttk.Label(root, text="Input Text:")
input_text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_text_var = tk.StringVar()
input_text_entry = ttk.Entry(root, textvariable=input_text_var, width=40)
input_text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
input_text_entry.focus()

# Create the key label and entry widget
key_label = ttk.Label(root, text="Key:")
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
key_var = tk.StringVar()
key_entry = ttk.Entry(root, textvariable=key_var, width=40, show="*")
key_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

# Create the option label and radio buttons
option_label = ttk.Label(root, text="Option:")
option_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
option_var = tk.StringVar(value="Encrypt")
encrypt_radio = ttk.Radiobutton(
    root, text="Encrypt", variable=option_var, value="Encrypt")
encrypt_radio.grid(row=2, column=1, padx=5, pady=5, sticky="w")
decrypt_radio = ttk.Radiobutton(
    root, text="Decrypt", variable=option_var, value="Decrypt")
decrypt_radio.grid(row=2, column=1, padx=5, pady=5, sticky="e")

# Create the output text label and entry widget
output_text_label = ttk.Label(root, text="Output Text:")
output_text_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
output_text_var = tk.StringVar()
output_text_entry = ttk.Entry(
    root, textvariable=output_text_var, state="readonly", width=40)
output_text_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")

# Create the process button
process_button = ttk.Button(root, text="Process", command=process_input)
process_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the execution time label
execution_time_label = ttk.Label(root, text="")
execution_time_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Set the padding for all widgets
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the GUI main loop
root.mainloop()
