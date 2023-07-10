import os

def encode_base64string(bin_fractals, padding):
    base64_string = [CHARACTERS[int(bin_fractal, 2)] for bin_fractal in bin_fractals]
    for i in range(len(base64_string) - padding, len(base64_string)):
        base64_string[i].replace("A", "=")
    return "".join(base64_string)

def decode_base64string(base64_string):
    padding = base64_string.count("=")
    base64_string = base64_string.replace("=", "A")
    bin_fractals = [str(bin(CHARACTERS.index(char)))[2:].rjust(6, "0") for char in base64_string]
    return bin_fractals, padding

while(True):
    os.system('clear')
    option = int(input("\n\nWhat do you want to do?\n\n1\tEncode\n2\tDecode\n3\tQuit\n\n>"))
    if(option==1 or option==2):
        text = input("\nEnter the text you want to encode or decode.\n\n>")
        if(option==1):
            print("\nPlaintext:\t{0}\nBase64:\t\t{1}".format(text, base64_encode(text)))
        else:
            print("\nBase64:\t\t{0}\nPlaintext:\t{1}".format(text, base64_decode(text)))
    elif(option==3):
        os.system('clear')
        break
    else:
        print("Invalid input!")
    input("\n\n[Press ENTER to continue]")