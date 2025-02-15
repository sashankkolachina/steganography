import cv2
import os

# Character encoding and decoding dictionaries
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def encrypt_image(image_path, msg, password, output_path="encryptedImage.jpg"):
    img = cv2.imread(image_path)  # Load the image
    if img is None:
        print("Error: Could not load image.")
        return

    n, m, z = 0, 0, 0

    # Encoding message into the image
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite(output_path, img)  # Save the encrypted image
    os.system(f"start {output_path}")  # Open the image (Windows only)
    print("Encryption completed! Encrypted image saved as", output_path)

def decrypt_image(image_path, msg_length, password, correct_password):
    if password != correct_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    img = cv2.imread(image_path)  # Load the encrypted image
    if img is None:
        print("Error: Could not load image.")
        return

    n, m, z = 0, 0, 0
    message = ""

    # Decoding message from the image
    for _ in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    print("Decryption message:", message)

# -------- Main Program --------
image_path = "mypic.jpg"  # Replace with correct image path
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

encrypt_image(image_path, msg, password)

# Decryption
pas = input("Enter passcode for Decryption: ")
decrypt_image("encryptedImage.jpg", len(msg), pas, password)
