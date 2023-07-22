import tkinter as tk
import pyperclip

def decimal_to_binary(decimal_ip):
    binary_parts = []
    for part in decimal_ip.split('.'):
        binary_parts.append(format(int(part), '08b'))
    binary_ip = '.'.join(binary_parts)
    return binary_ip

def binary_to_decimal(binary_ip):
    decimal_parts = []
    for part in binary_ip.split('.'):
        decimal_parts.append(str(int(part, 2)))
    decimal_ip = '.'.join(decimal_parts)
    return decimal_ip

def convert_to_binary():
    decimal_ip = decimal_entry.get()
    if decimal_ip:
        binary_result = decimal_to_binary(decimal_ip)
        result_label.config(text="Decimal IP to Binary IP: " + binary_result)
        pyperclip.copy(binary_result)

def convert_to_decimal():
    binary_ip = decimal_entry.get()
    if binary_ip:
        decimal_result = binary_to_decimal(binary_ip)
        result_label.config(text="Binary IP to Decimal IP: " + decimal_result)
        pyperclip.copy(decimal_result)

def clear_input():
    decimal_entry.delete(0, tk.END)
    result_label.config(text="")


window = tk.Tk()
window.title("IP Address Converter")
window.geometry("450x200")
window.configure(bg='#b3e6ff') 


window.resizable(False, False)


label_font = ('Helvetica', 12, 'bold')

decimal_label = tk.Label(window, text="Enter Decimal IP:", font=label_font, bg='#b3e6ff')
decimal_label.pack(pady=10)

decimal_entry = tk.Entry(window, font=label_font)
decimal_entry.pack(pady=(0, 5))

button_frame = tk.Frame(window, bg='#b3e6ff')
button_frame.pack(pady=10)

convert_to_binary_button = tk.Button(button_frame, text="Convert to Binary", font=label_font, command=convert_to_binary)
convert_to_binary_button.pack(side=tk.LEFT, padx=10)

convert_to_decimal_button = tk.Button(button_frame, text="Convert to Decimal", font=label_font, command=convert_to_decimal)
convert_to_decimal_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=label_font, command=clear_input)
clear_button.pack(side=tk.LEFT, padx=10)

# Dönüşüm sonucu için etiket
output_font = ('Helvetica', 12)

result_label = tk.Label(window, text="", font=output_font, wraplength=350, bg='#b3e6ff')
result_label.pack(pady=10)

window.mainloop()
