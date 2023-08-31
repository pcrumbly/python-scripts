import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_csv_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        df = pd.read_csv(filepath)

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        table = tk.Label(scrollable_frame, text=df.to_string(index=False), justify='left')
        
        table.pack(fill='x', expand=True)
        
        filename = os.path.basename(filepath)
        filepath_entry.delete(0, tk.END)
        filepath_entry.insert(0, filename)
        
        #TODO figure out better way to update the root/frame/canvas/scrollbar IDK???
        #this seems like a hack
        root.geometry("600x701")
        

root = tk.Tk()
root.title("CSV Viewer")
root.geometry("600x700")

header_frame = tk.Frame(root, height=50)
header_frame.pack(fill=tk.X)

open_button = tk.Button(header_frame, text="Open CSV", command=open_csv_file)
open_button.pack(side=tk.LEFT, padx=10)

filepath_entry = tk.Entry(header_frame)
filepath_entry.pack(side=tk.LEFT, padx=10, fill='x', expand=True)

main_body_frame = tk.Frame(root)
main_body_frame.pack(fill=tk.BOTH, expand=True, padx=10)

canvas = tk.Canvas(main_body_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(main_body_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = tk.Frame(canvas)
scrollable_frame.pack(fill=tk.BOTH, expand=True)

canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)
canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox(tk.ALL)))

root.mainloop()
