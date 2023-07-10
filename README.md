# Python3-Base64-Encode-Decode

These are two functions I have created that allow a user to encode or decode a string with Base64 with Python. 
To use them, see [raw-functions.py](raw-functions.py) and paste them into your code like so:

`File: main.py in selected workspace`:
```py
CHARACTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]

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

string = input("Enter a string to encode")
b64 = encode_base64string(string)
print(f"Your B64 String: {b64}")
```
-> This will print a Base 64 encoded version of `string`.

**[!] WARNING [!]**
The `CHARACTERS` variable should not be changed and should always be equal to this list:
```py
CHARACTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
```