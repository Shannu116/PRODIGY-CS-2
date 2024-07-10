from PIL import Image
def encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width,height = image.size

    for x in range(width):
        for y in range(height):
            r,g,b = pixels[x,y]
            pixels[x,y]=(r ^ 0xFF,g ^ 0xFF, b ^ 0xFF)
    image.save('encrypted_image.png')
def decryption_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width,height = image.size
    for x in range(width):
        for y in range(height):
            r,g,b = pixels[x,y]
            pixels[x,y]=(r ^ 0xFF,g ^ 0xFF, b ^ 0xFF)
    image.save('decrypted_image.png')
def main():
    print("image encryption tool")
    password = input("enter the password :")

#here you can change the password    
    if password == 'pixel':
        choice = input("enter the 'e' for encrypt and 'd' for decrypt:")
        key = len(password)
        if choice == 'e':
            image_path=input("enter the path of the original image: ")
            encrypt_image(image_path)
            print("image is encrypted")
        elif choice == 'd':
            image_path = input("enter the path of the encrypted image:")
            decryption_image(image_path)
            print("image is decrypted")
        else:
            print("enter the correct option")
    else:
        print("you are not allowed")
if __name__ == "__main__":
    main()
