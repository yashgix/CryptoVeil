from PIL import Image
import numpy as np
from scipy import stats
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password: str) -> bytes:
    salt = b'salt_'  # In a real application, use a random salt and store it
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_message(message: str, password: str) -> str:
    key = generate_key(password)
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()

def decrypt_message(encrypted_message: str, password: str) -> str:
    key = generate_key(password)
    f = Fernet(key)
    decrypted_message = f.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode()

def encode_message(image, message, password):
    if isinstance(image, str):
        img = Image.open(image)
    elif isinstance(image, Image.Image):
        img = image
    else:
        raise ValueError("Input must be a file path or a PIL Image object")

    encrypted_message = encrypt_message(message, password)
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)
    binary_message += '0000000000000001'  # Delimiter

    img_array = np.array(img)

    if img_array.size < len(binary_message):
        raise ValueError("Image is too small to hold this message")

    index = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB channels
                if index < len(binary_message):
                    img_array[i, j, k] = int(bin(img_array[i, j, k])[2:9] + binary_message[index], 2)
                    index += 1
                else:
                    break
            if index >= len(binary_message):
                break
        if index >= len(binary_message):
            break

    encoded_img = Image.fromarray(img_array)
    return encoded_img

def decode_message(image, password):
    if isinstance(image, str):
        img = Image.open(image)
    elif isinstance(image, Image.Image):
        img = image
    else:
        raise ValueError("Input must be a file path or a PIL Image object")

    img_array = np.array(img)
    binary_message = ""
    delimiter_found = False

    for i in range(img_array.shape[0]):
        if delimiter_found:
            break
        for j in range(img_array.shape[1]):
            if delimiter_found:
                break
            for k in range(3):  # RGB channels
                binary_message += bin(img_array[i, j, k])[-1]
                if len(binary_message) % 8 == 0:
                    if binary_message[-16:] == '0000000000000001':
                        binary_message = binary_message[:-16]
                        delimiter_found = True
                        break

    if not delimiter_found:
        raise ValueError("No hidden message found in the image")

    encrypted_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        encrypted_message += chr(int(byte, 2))

    try:
        decrypted_message = decrypt_message(encrypted_message, password)
        return decrypted_message, len(encrypted_message)
    except Exception as e:
        raise ValueError(f"Failed to decrypt the message: {str(e)}")
    


