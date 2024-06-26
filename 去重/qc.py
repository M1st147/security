import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def remove_duplicates(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Remove duplicates while maintaining order
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)

        messagebox.showinfo("成功", f"去重成功!\n输出路径: {output_file_path}")
    except Exception as e:
        messagebox.showerror("错误", str(e))

def select_input_file():
    input_file_path = filedialog.askopenfilename(title="Select Input File")
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file_path)

def select_output_file():
    output_file_path = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file_path)

def process_files():
    input_file_path = input_file_entry.get()
    output_file_path = output_file_entry.get()
    if not input_file_path or not output_file_path:
        messagebox.showerror("错误", "请同时选择输入和输出文件。")
        return
    remove_duplicates(input_file_path, output_file_path)

# Create the main window
root = tk.Tk()
root.title("去重工具")

# Input file selection
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
input_file_button = tk.Button(root, text="Browse...", command=select_input_file)
input_file_button.grid(row=0, column=2, padx=10, pady=10)

# Output file selection
tk.Label(root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
output_file_button = tk.Button(root, text="Browse...", command=select_output_file)
output_file_button.grid(row=1, column=2, padx=10, pady=10)

# Process button
process_button = tk.Button(root, text="开始去重", command=process_files)
process_button.grid(row=2, column=0, columnspan=3, pady=20)

# Start the main loop
root.mainloop()
