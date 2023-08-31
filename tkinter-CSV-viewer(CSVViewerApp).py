import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

class CSVViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("600x700")

        self.create_ui()

    def create_ui(self):
        self.create_header()
        self.create_main_body()

    def create_header(self):
        header_frame = tk.Frame(self.root, height=50)
        header_frame.pack(fill=tk.X)

        open_button = tk.Button(header_frame, text="Open CSV", command=self.open_csv_file)
        open_button.pack(side=tk.LEFT, padx=10)

        self.filepath_entry = tk.Entry(header_frame)
        self.filepath_entry.pack(side=tk.LEFT, padx=10, fill='x', expand=True)

    def create_main_body(self):
        main_body_frame = tk.Frame(self.root)
        main_body_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        self.canvas = tk.Canvas(main_body_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(main_body_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor=tk.NW)
        self.canvas.bind("<Configure>", self.configure_canvas_scroll)

    def open_csv_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            df = pd.read_csv(filepath)

            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            table = tk.Label(self.scrollable_frame, text=df.to_string(index=False), justify='left')
            table.pack(fill='x', expand=True)

            filename = os.path.basename(filepath)
            self.filepath_entry.delete(0, tk.END)
            self.filepath_entry.insert(0, filename)
            root.geometry("600x701")

    def configure_canvas_scroll(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()
