# Py3 (Installer)

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

# Py3 (Microsodt Store)

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

# Py2 (Global)

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

