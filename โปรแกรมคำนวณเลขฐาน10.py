import tkinter as tk
from tkinter import Label, font

def decimal_to_binary(decimal):
    return bin(decimal)[2:].upper()

def decimal_to_octal(decimal):
    return oct(decimal)[2:].upper()

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:].upper()

def convert():
    decimal_input = decimal_entry.get()

    # Check if the input is a valid decimal number
    if not decimal_input.isnumeric():
        binary_result.config(text="Error !!!", fg="red")
        octal_result.config(text="โปรดตรวจสอบ", fg="red")
        hexadecimal_result.config(text="ตัวเลขที่กรอก", fg="red")
        return

    decimal = int(decimal_input)
    binary = decimal_to_binary(decimal)
    octal = decimal_to_octal(decimal)
    hexadecimal = decimal_to_hexadecimal(decimal)

    binary_result.config(text=binary)
    octal_result.config(text=octal)
    hexadecimal_result.config(text=hexadecimal)

window = tk.Tk()
window.title("โปรแกรมแปลงเลขฐาน 10".upper())
window.configure(bg="#AFD7F6")
window.geometry("660x300")

# font Thai characters
font_style = font.Font(family="TH Sarabun New", size=16, weight="bold")

# Decimal input
decimal_label = tk.Label(window, text="กรอกตัวเลขฐาน 10 (0-9) ", bg="#D0F0C0", fg="black".upper(), font=font_style)
decimal_label.grid(row=0, column=0, padx=14, pady=14)

decimal_entry = tk.Entry(window)
decimal_entry.grid(row=0, column=1, padx=14, pady=14)

convert_button = tk.Button(window, text="แปลงเป็นฐาน 2 , 8 และ 16 ", command=convert, bg="#D0F0C0", fg="black".upper(), font=font_style)
convert_button.grid(row=0, column=2, padx=14, pady=14)

# Binary result
binary_label = tk.Label(window, text="เลขฐาน 2 ", bg="#D0F0C0", fg="black".upper(), font=font_style)
binary_label.grid(row=1, column=0, padx=14, pady=14)

binary_result = tk.Label(window, text="",bg="#AFD7F6".upper(), font=font_style)
binary_result.grid(row=1, column=1, padx=14, pady=14)

# Octal result
octal_label = tk.Label(window, text="เลขฐาน 8 ", bg="#D0F0C0", fg="black".upper(), font=font_style)
octal_label.grid(row=2, column=0, padx=14, pady=14)

octal_result = tk.Label(window, text="",bg="#AFD7F6".upper(), font=font_style)
octal_result.grid(row=2, column=1, padx=14, pady=14)

# Hexadecimal result
hexadecimal_label = tk.Label(window, text="เลขฐาน 16 ", bg="#D0F0C0", fg="black".upper(), font=font_style)
hexadecimal_label.grid(row=3, column=0, padx=14, pady=14)

hexadecimal_result = tk.Label(window, text="",bg="#AFD7F6".upper(), font=font_style)
hexadecimal_result.grid(row=3, column=1, padx=14, pady=14)

window.mainloop()
