import tkinter as tk
from tkinter import messagebox

def text_to_binary(text):
    binary = ' '.join(format(ord (char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    text = ''.join(chr(int(byte, 2)) for byte in binary.split())
    return text

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END))

def clear_history():
    history_text.delete(1.0, tk.END)

def add_to_history(text):
    history_text.insert(tk.END, text + '\n')

def convert_text_to_binary():
    text = input_text.get(1.0, tk.END)
    binary = text_to_binary(text)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, binary)
    add_to_history(f'Text to Binary: {text} -> {binary}')

def convert_binary_to_text():
    binary = input_text.get(1.0, tk.END)
    text = binary_to_text(binary)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, text)
    add_to_history(f'Binary to Text: {binary} -> {text}')

root = tk.Tk()
root.title('binary babel ')


input_frame = tk.Frame(root)
input_frame.pack(fill='x')

input_label = tk.Label(input_frame, text='Input:')
input_label.pack(side='left')

input_text = tk.Text(input_frame, width=40, height=5)
input_text.pack(side='left')

option_frame = tk.Frame(root)
option_frame.pack(fill='x')

option_label = tk.Label(option_frame, text='Select an option:')
option_label.pack(side='left')

option_var = tk.StringVar()
option_var.set('Text to Binary')

text_to_binary_radio = tk.Radiobutton(option_frame, text='Text to Binary', variable=option_var, value='Text to Binary')
text_to_binary_radio.pack(side='left')

binary_to_text_radio = tk.Radiobutton(option_frame, text='Binary to Text', variable=option_var, value='Binary to Text')
binary_to_text_radio.pack(side='left')

convert_button = tk.Button(option_frame, text='Convert', command=lambda: convert_text_to_binary() if option_var.get() == 'Text to Binary' else convert_binary_to_text())
convert_button.pack(side='left')

output_frame = tk.Frame(root)
output_frame.pack(fill='x')

output_label = tk.Label(output_frame, text='Output:')
output_label.pack(side='left')

output_text = tk.Text(output_frame, width=40, height=5)
output_text.pack(side='left')

copy_button = tk.Button(output_frame, text='Copy', command=copy_output)
copy_button.pack(side='left')

history_frame = tk.Frame(root)
history_frame.pack(fill='x')

history_label = tk.Label(history_frame, text='History:')
history_label.pack(side='left')

history_text = tk.Text(history_frame, width=40, height=5)
history_text.pack(side='left')

clear_history_button = tk.Button(history_frame, text='Clear History', command=clear_history)
clear_history_button.pack(side='left')

root.mainloop()