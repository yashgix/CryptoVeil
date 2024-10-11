from core.steganography import encode_message, decode_message, has_hidden_message
from PIL import Image

def test_steganography():
    original_image_path = "Chair.jpeg"
    secret_message = "This is a secret message for testing!"

    print(f"Original message: {secret_message}")

    # Test original image (should not have a hidden message)
    print("\nTesting original image:")
    if has_hidden_message(original_image_path):
        print("Error: False positive - Hidden message detected in the original image.")
    else:
        print("Correct: No hidden message detected in the original image.")

    # Encode the message
    encoded_img = encode_message(original_image_path, secret_message)
    encoded_img.save("encoded_test_image.png")
    print("\nMessage encoded in image.")

    # Check if the encoded image has a hidden message
    print("\nTesting encoded image:")
    if has_hidden_message("encoded_test_image.png"):
        print("Correct: Hidden message detected in the encoded image.")
    else:
        print("Error: No hidden message detected in the encoded image.")

    # Decode the message
    try:
        decoded_message = decode_message("encoded_test_image.png")
        print(f"\nDecoded message: {decoded_message}")

        # Check if the decoded message matches the original
        if secret_message == decoded_message:
            print("Test passed successfully!")
        else:
            print("Test failed. Messages don't match.")
            print(f"Original length: {len(secret_message)}")
            print(f"Decoded length:  {len(decoded_message)}")
    except ValueError as e:
        print(f"Error decoding message: {e}")

if __name__ == "__main__":
    test_steganography()