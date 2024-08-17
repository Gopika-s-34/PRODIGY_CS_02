from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")  
    img_array = np.array(img)
    encrypted_array = (img_array + key) % 256
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save("encrypted_image.png")
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")  
    img_array = np.array(img)
    decrypted_array = (img_array - key) % 256

    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save("decrypted_image.png")
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

key = 50 
encrypt_image("input_image.png", key)
decrypt_image("encrypted_image.png", key)
