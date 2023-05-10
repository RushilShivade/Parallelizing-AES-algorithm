from Crypto.Cipher import AES
from Crypto.Util import Counter
import time

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


# Take user input for option of encryption or decryption
option = input("Enter 'e' for encryption or 'd' for decryption: ")

# Take user input for the text or ciphertext to be processed
input_text = input("Enter the text or ciphertext to be processed: ")

# Take user input for the encryption key
key = input("Enter the encryption key (must be 16, 24, or 32 bytes long): ")

# Convert the key string to bytes
key = bytes.fromhex(key)

# Check if the key length is valid
if len(key) not in [16, 24, 32]:
    print("Error: Invalid key length.")
else:
    # Measure the execution time
    start_time = time.time()

    # Process the input based on the selected option
    if option == 'e':
        ciphertext = encrypt(key, input_text)
        print("Encrypted text:", ciphertext)
    elif option == 'd':
        plaintext = decrypt(key, input_text)
        print("Decrypted text:", plaintext)
    else:
        print("Error: Invalid option.")

    end_time = time.time()

    # Calculate the execution time and print it
    execution_time = end_time - start_time
    print("Execution time: {:.5f} seconds".format(execution_time))