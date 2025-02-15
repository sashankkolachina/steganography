Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import cv2
import os
import numpy as np

# Character encoding and decoding dictionaries
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def encrypt_image(msg, password, input_image="mypic.jpg", output_image="encryptedImage.jpg"):
    img = cv2.imread(input_image)  # Load the image
    if img is None:
        print("Error: Could not load image.")
        return
    
    # Ensure image is writable
    img = img.astype(np.uint8)

    height, width, _ = img.shape
    n, m, z = 0, 0, 0

    # Encoding message into the image
    for char in msg:
        img[n, m, z] = min(d[char], 255)  # Ensure value is within 0-255
        z = (z + 1) % 3  # Cycle through RGB channels
        if z == 0:  # Move to the next pixel
            m += 1
            if m >= width:  # Move to next row
                m = 0
                n += 1
                if n >= height:  # Prevent exceeding image bounds
                    print("Error: Message too long for image size!")
                    return

    cv2.imwrite(output_image, img)  # Save the encrypted image
    os.system(f"start {output_image}")  # Open the image (Windows only)
    print("Encryption completed! Encrypted image saved as", output_image)
... 
... def decrypt_image(msg_length, password, correct_password, input_image="encryptedImage.jpg"):
...     if password != correct_password:
...         print("YOU ARE NOT AUTHORIZED")
...         return
...     
...     img = cv2.imread(input_image)  # Load the encrypted image
...     if img is None:
...         print("Error: Could not load image.")
...         return
... 
...     height, width, _ = img.shape
...     n, m, z = 0, 0, 0
...     message = ""
... 
...     # Decoding message from the image
...     for _ in range(msg_length):
...         message += c.get(img[n, m, z], '?')  # Use get() to avoid KeyError
...         z = (z + 1) % 3  # Cycle through RGB channels
...         if z == 0:  # Move to the next pixel
...             m += 1
...             if m >= width:  # Move to next row
...                 m = 0
...                 n += 1
...                 if n >= height:  # Prevent exceeding image bounds
...                     break
... 
...     print("Decryption message:", message)
... 
... # -------- Main Program --------
... msg = input("Enter secret message: ")
... password = input("Enter a passcode: ")
... 
... encrypt_image(msg, password)
... 
... # Decryption
... pas = input("Enter passcode for Decryption: ")
... decrypt_image(len(msg), pas, password)
