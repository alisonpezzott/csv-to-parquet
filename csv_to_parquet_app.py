import os
import sys
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
from tkinter import ttk


def convert_files(input_dir, output_dir, extension, encoding, sep, header):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    sep_map = {
        'tab': '\t',
        ';': ';',
        ',': ',',
        '|': '|',
        'space': ' ',
        'Other': sep
    }
    sep = sep_map.get(sep, sep)

    header_map = {
        'None': None,
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        'Other': int(header) if header.isdigit() else header
    }
    header = header_map.get(header, header)

    for filename in os.listdir(input_dir):
        if filename.endswith(extension):
            csv_path = os.path.join(input_dir, filename)
            try:
                df = pd.read_csv(csv_path, encoding=encoding, sep=sep, header=header, low_memory=False)
                parquet_path = os.path.join(output_dir, filename.replace(extension, '.parquet'))
                df.to_parquet(parquet_path)
                print(f"Processed file {csv_path}")
            except Exception as e:
                print(f"Error processing file {csv_path}: {e}")

    print("Conversion completed!")

def browse_input():
    input_dir.set(filedialog.askdirectory())

def browse_output():
    output_dir.set(filedialog.askdirectory())

def start_conversion():
    convert_files(input_dir.get(), output_dir.get(), extension.get(), encoding.get(), sep.get(), header.get())
    messagebox.showinfo("Info", "Conversion completed!")

def on_option_change(var, entry):
    if var.get() == 'Other':
        entry.grid()
    else:
        entry.grid_remove()

def create_rounded_button(canvas, text, command, width, height, radius, bg_color, hover_color, fg_color, font=('Helvetica', 10, 'bold')):
    def _round_rectangle(x1, y1, x2, y2, radius=16, **kwargs):
        points = [x1+radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    canvas.update_idletasks()
    canvas_width = canvas.winfo_width()
    x = (canvas_width - width) // 2

    button_bg = _round_rectangle(x, 0, x + width, height, radius=radius, fill=bg_color, outline="#000000", width=2)
    button_text = canvas.create_text(x + width // 2, height // 2, text=text, fill=fg_color, font=font)

    def on_enter(event):
        canvas.itemconfig(button_bg, fill=hover_color)
        canvas.config(cursor="hand2")

    def on_leave(event):
        canvas.itemconfig(button_bg, fill=bg_color)
        canvas.config(cursor="")

    canvas.tag_bind(button_bg, '<Button-1>', lambda e: command())
    canvas.tag_bind(button_text, '<Button-1>', lambda e: command())
    canvas.tag_bind(button_bg, '<Enter>', on_enter)
    canvas.tag_bind(button_bg, '<Leave>', on_leave)
    canvas.tag_bind(button_text, '<Enter>', on_enter)
    canvas.tag_bind(button_text, '<Leave>', on_leave)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = tk.Tk()
app.title("CSV to Parquet by Alison Pezzott")

bg_color = "#f2f2f2"
fg_color = "#212121"
entry_bg_color = "#3e3e3e"
entry_fg_color = "#ffffff"
button_bg_color = "#333333"
button_hover_color = "#222222"
button_fg_color = "#ffffff"

app.configure(bg=bg_color)

icon_path = resource_path("icon.png")
app_icon = PhotoImage(file=icon_path)
app.iconphoto(False, app_icon)

input_dir = tk.StringVar()
output_dir = tk.StringVar()
extension = tk.StringVar(value='.csv')
encoding = tk.StringVar(value='utf-8')
sep = tk.StringVar(value=';')
header = tk.StringVar(value='0')

tk.Label(app, text="Input Directory:", anchor="w", bg=bg_color, fg=fg_color).grid(row=3, column=0, padx=8, pady=4, sticky="w"),
ttk.Entry(app, textvariable=input_dir, width=50).grid(row=3, column=1, padx=8, pady=4)
ttk.Button(app, text="Browse", command=browse_input).grid(row=3, column=2, padx=8, pady=4)

tk.Label(app, text="Output Directory:", anchor="w", bg=bg_color, fg=fg_color).grid(row=4, column=0, padx=8, pady=4, sticky="w")
ttk.Entry(app, textvariable=output_dir, width=50).grid(row=4, column=1, padx=8, pady=4)
ttk.Button(app, text="Browse", command=browse_output).grid(row=4, column=2, padx=8, pady=4)

tk.Label(app, text="Extension:", anchor="w", bg=bg_color, fg=fg_color).grid(row=5, column=0, padx=8, pady=5, sticky="w")
ttk.OptionMenu(app, extension, '.csv', '.csv', '.txt').grid(row=5, column=1, padx=8, pady=5)

tk.Label(app, text="Encoding:", anchor="w", bg=bg_color, fg=fg_color).grid(row=6, column=0, padx=8, pady=5, sticky="w")
encoding_entry = ttk.Entry(app, textvariable=encoding, width=8)
ttk.OptionMenu(app, encoding, 'utf-8', 'utf-8', 'latin1', 'cp1252', 'ascii', 'utf-16', 'utf-32', 'Other').grid(row=6, column=1, padx=8, pady=5)
encoding.trace('w', lambda *args: on_option_change(encoding, encoding_entry))
encoding_entry.grid(row=6, column=2, padx=8, pady=5)
encoding_entry.grid_remove()

tk.Label(app, text="Separator:", anchor="w", bg=bg_color, fg=fg_color).grid(row=7, column=0, padx=8, pady=5, sticky="w")
sep_entry = ttk.Entry(app, textvariable=sep, width=8)
ttk.OptionMenu(app, sep, 'Tab', ';', ',', '|', 'Space', 'Other').grid(row=7, column=1, padx=8, pady=5)
sep.trace('w', lambda *args: on_option_change(sep, sep_entry))
sep_entry.grid(row=7, column=2, padx=8, pady=5)
sep_entry.grid_remove()

tk.Label(app, text="Header:", anchor="w", bg=bg_color, fg=fg_color).grid(row=8, column=0, padx=8, pady=5, sticky="w")
header_entry = ttk.Entry(app, textvariable=header, width=8)
ttk.OptionMenu(app, header, 'None', 'None', '0', '1', '2', '3', '4', '5', 'Other').grid(row=8, column=1, padx=8, pady=5)
header.trace('w', lambda *args: on_option_change(header, header_entry))
header_entry.grid(row=8, column=2, padx=8, pady=5)
header_entry.grid_remove()

canvas = tk.Canvas(app, bg=bg_color, highlightthickness=0, width=300, height=60)
canvas.grid(row=9, column=0, columnspan=3, pady=20)

create_rounded_button(
    canvas,
    "🚀 Start Conversion",
    start_conversion,
    width=200,
    height=50,
    radius=25,
    bg_color=button_bg_color,
    hover_color=button_hover_color,
    fg_color=button_fg_color,
    font=('Helvetica', 12, 'bold')
)

github_link = tk.Label(app, text="GitHub: https://github.com/alisonpezzott/csv-to-parquet", fg="blue", cursor="hand2", bg=bg_color)
github_link.grid(row=10, column=0, columnspan=3)
github_link.bind("<Button-1>", lambda e: os.system("start https://github.com/alisonpezzott/csv-to-parquet"))

version_label = tk.Label(app, text="CSV to Parquet Version: 1.0.0", bg=bg_color, fg=fg_color)
version_label.grid(row=11, column=0, columnspan=3, pady=5)

app.mainloop()