import random
from colorama import Fore
import math
import os

loginbanner = Fore.GREEN + """ ██▓     ▒█████    ▄████  ██▓ ███▄    █ 
▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █ 
▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒ 
░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░░   ░ ▒░
  ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░   ░   ░ ░ 
    ░  ░    ░ ░        ░  ░           ░ 
                                         """ + Fore.RESET

# Display banner
banner = Fore.RED + """██████╗  ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██║████╗  ██║██╔═══██╗
██║  ██║██║   ██║██╔████╔██║██║██╔██╗ ██║██║   ██║
██║  ██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ """ + Fore.RESET

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

def decimal_to_octal(decimal_num):
    return oct(decimal_num)[2:]

def decimal_to_hex(decimal_num):
    return hex(decimal_num)[2:].upper()
    
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()

def decompose_number(decimal_num):
    components = []
    power = 0
    while decimal_num > 0:
        if decimal_num % 2 == 1:
            components.append(2 ** power)
        decimal_num //= 2
        power += 1
    return components[::-1] 

def format_decomposition(decimal_num):
    components = decompose_number(decimal_num)
    terms = ' + '.join(str(comp) for comp in components)
    return f"{decimal_num} = {terms} = " + " + ".join(f"2^{i}" for i in range(len(components) - 1, -1, -1))

def format_binary_output(binary_str):
    return binary_str.zfill(len(binary_str))

def process_binary_input(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    binary_representation = decimal_to_binary(decimal_num)
    octal_representation = decimal_to_octal(decimal_num)
    hex_representation = decimal_to_hex(decimal_num)
    decomposition = format_decomposition(decimal_num)
    formatted_binary = format_binary_output(binary_representation)
    
    print(f"Binary Input: {binary_str}")
    print(f"Decimal Equivalent: {decimal_num}")
    print(f"Decomposition: {decomposition}")
    print(f"Binary Representation: {formatted_binary}")
    print(f"Octal Representation: {octal_representation}")
    print(f"Hexadecimal Representation: {hex_representation}")

def process_decimal_input(decimal_num):
    binary_representation = decimal_to_binary(decimal_num)
    octal_representation = decimal_to_octal(decimal_num)
    hex_representation = decimal_to_hex(decimal_num)
    decomposition = format_decomposition(decimal_num)
    formatted_binary = format_binary_output(binary_representation)
    
    print(f"Decimal Input: {decimal_num}")
    print(f"Binary Representation: {formatted_binary}")
    print(f"Octal Representation: {octal_representation}")
    print(f"Hexadecimal Representation: {hex_representation}")
    print(f"Decomposition: {decomposition}")

def process_octal_input(octal_str):
    decimal_num = int(octal_str, 8)
    binary_representation = decimal_to_binary(decimal_num)
    octal_representation = decimal_to_octal(decimal_num)
    hex_representation = decimal_to_hex(decimal_num)
    decomposition = format_decomposition(decimal_num)
    formatted_binary = format_binary_output(binary_representation)
    
    print(f"Octal Input: {octal_str}")
    print(f"Decimal Equivalent: {decimal_num}")
    print(f"Binary Representation: {formatted_binary}")
    print(f"Hexadecimal Representation: {hex_representation}")
    print(f"Decomposition: {decomposition}")

def process_hex_input(hex_str):
    decimal_num = int(hex_str, 16)
    binary_representation = decimal_to_binary(decimal_num)
    octal_representation = decimal_to_octal(decimal_num)
    hex_representation = decimal_to_hex(decimal_num)
    decomposition = format_decomposition(decimal_num)
    formatted_binary = format_binary_output(binary_representation)
    
    print(f"Hexadecimal Input: {hex_str}")
    print(f"Decimal Equivalent: {decimal_num}")
    print(f"Binary Representation: {formatted_binary}")
    print(f"Octal Representation: {octal_representation}")
    print(f"Decomposition: {decomposition}")

def main():
    os.system("cls")
    print(banner)
    print("")
    print("Made by dominik :)")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    while True:
        command = input("[root@DOMINO] ~ # ").strip()
        
        if command.startswith("bin "):
            binary_str = command[4:]
            if not all(c in '01' for c in binary_str):
                print("Invalid binary string. Please enter only 0s and 1s.")
                continue
            process_binary_input(binary_str)
        
        elif command.startswith("dec "):
            try:
                decimal_num = int(command[4:])
                if decimal_num < 0:
                    print("Please enter a non-negative decimal number.")
                    continue
                process_decimal_input(decimal_num)
                
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")
                continue
        
        elif command.startswith("oct "):
            octal_str = command[4:]
            if not all(c in '01234567' for c in octal_str):
                print("Invalid octal string. Please enter only digits 0-7.")
                continue
            process_octal_input(octal_str)
        
        elif command.startswith("hex "):
            hex_str = command[4:].upper()
            if not all(c in '0123456789ABCDEF' for c in hex_str):
                print("Invalid hexadecimal string. Please enter valid hexadecimal digits.")
                continue
            process_hex_input(hex_str)
            
        elif command == "stvorec":
            a=45
            s=a*a
            print("Obsah stvorca: ", s)
            continue
            
        elif command == "kruh":
            r2 = 10 ** 2
            pi = math.pi
            S = pi * r2
            print("Obsah kruhu:", S)
        elif command == "trojuhelnik":
            full_pyramid(4)
        
        elif command == "q":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid command. Use 'bin <binary_string>' for binary input, 'dec <decimal_number>' for decimal input, 'oct <octal_string>' for octal input, 'hex <hexadecimal_string>' for hexadecimal input, or 'q' to quit.")
            
        print()

def login():
    os.system("cls")
    print(loginbanner)
    user = input("username: ")
    if user == "domino":
        password = input("password: ")
        if password == "1234":
            main()

if __name__ == "__main__":
    login()
