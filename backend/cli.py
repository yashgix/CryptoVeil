import argparse
from core.steganography import encode_message, decode_message
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="CryptoVeil: A steganography tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode a message into an image")
    encode_parser.add_argument("input_image", help="Path to the input image")
    encode_parser.add_argument("message", help="Message to encode")
    encode_parser.add_argument("output_image", help="Path to save the output image")
    encode_parser.add_argument("-p", "--password", help="Encryption password", required=True)

    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Decode a message from an image")
    decode_parser.add_argument("input_image", help="Path to the input image")
    decode_parser.add_argument("-p", "--password", help="Decryption password", required=True)

    args = parser.parse_args()

    if args.command == "encode":
        try:
            img = Image.open(args.input_image)
            encoded_img = encode_message(img, args.message, args.password)
            encoded_img.save(args.output_image)
            print(f"Message encoded successfully. Output saved to {args.output_image}")
        except Exception as e:
            print(f"Error encoding message: {str(e)}")

    elif args.command == "decode":
        try:
            decoded_message, message_size = decode_message(args.input_image, args.password)
            print(f"Decoded message: {decoded_message}")
            print(f"Size of encrypted data: {message_size} bytes")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()