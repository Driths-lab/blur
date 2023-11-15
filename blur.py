import os
import io
import fleep
from PIL import Image

def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension

def check_output_dir() -> bool:
    #TODO
    return True

def get_file_path_from_user(prompt):
    while True:
        file_path = input(prompt).strip()
        
        # Check if the file path is valid
        if os.path.isfile(file_path):
            return file_path
        else:
            print("Invalid file path. Please try again.")

def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def identify_file(content):
    try:
        info = fleep.get(content)
        ex = None
        if len(info.extension) > 0:
            ex = info.extension[0]
        return ex
    except Exception as e:
        print(f"An error occurred: {e}")
    

def encode_jpg(file_path, image_path):
    file_content = bytearray()
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
        print("File Content as String:")
        print(file_content)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
    try:
        temp_path = os.getcwd() + "/blur.jpg"
        original_image = Image.open(image_path)

        # Save a copy of the image
        original_image.save(temp_path)

        with open(temp_path, 'ab') as image:
            image.write(file_content)
        

    except Exception as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decode_jpg(image_path):
    try:
        with open(image_path, 'rb') as file:
            content = file.read()  
            jpg_offest = content.index(bytes.fromhex('FFD9'))
            file.seek(jpg_offest + 2)
            data = file.read()
            extension = identify_file(data)

            temp_path = os.getcwd() + "/output/blur_decode."

            if extension is not None:
                temp_path += extension
               
            else:
                print("Unable to detect file type")
                print("outputing content to .txt file")
            temp_path += "txt"
            with open(temp_path, 'wb') as decoded_file:
                    decoded_file.write(data)
    except Exception as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")

def encode_text(image_path, data):
    try:
        temp_path = os.getcwd() + "/output/blur.jpg"
        original_image = Image.open(image_path)

        # Save a copy of the image
        original_image.save(temp_path)

        with open(temp_path, 'ab') as image:
            image.write(bytearray(data, 'utf-8'))
        

    except Exception as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
    """         
             _____ _
            | ___ \ |           
            | |_/ / |_   _ _ __ 
            | ___ \ | | | | '__|
            | |_/ / | |_| | |   
            \____/|_|\__,_|_|"""
        )
    while True:
        print()
        print("Version 1.0.0")
        print("Please select an option:")
        print()
        print("[1] Hide a file in an image")
        print("[2] Reveal a hidden file in an image")
        print("[3] Hide text with an image")
        print("[4] Exit")
        print()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                file_path = get_file_path_from_user("Enter the file path: ")
                image_path = get_file_path_from_user("Enter the image path: ")
                encode_jpg(file_path, image_path)
                print("The file has been concealed!")
            case "2":
                image_path = get_file_path_from_user("Enter the path to the image: ")
                decode_jpg(image_path)
            case "3":
                print("If you would like to encode a large text block, use a .txt file and option 1")
                print("Otherwise...")
                user_input = get_input("Enter the text you would like to encode: ")
                image_path = get_file_path_from_user("Enter the image path: ")
                encode_text(image_path, user_input)
                print("File encoded and writen to /output")
            case "4":
                print("Exiting...")
                exit()
            case _:
                print("Invalid choice.")





if __name__ == '__main__':
    main()