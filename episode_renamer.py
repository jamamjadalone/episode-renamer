# episode_renamer.py
# Episode Renamer - by Jam Amjad Rasheed
# A GUI tool to rename episode files with preview, checkbox selection, and optional part support

import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

APP_TITLE = "Episode Renamer - by Jam Amjad Rasheed"
SUPPORTED_EXTENSIONS = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.mp3', '.srt')

def show_preview_and_confirm():
    folder_path = filedialog.askdirectory(title="Select Folder with Episodes")
    if not folder_path:
        return

    rename_list = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if not os.path.isfile(full_path):
            continue

        ext = os.path.splitext(filename)[1].lower()
        if ext not in SUPPORTED_EXTENSIONS:
            continue

        match = re.search(r'(?:ep|episode)[ _-]*(\d+)', filename, re.IGNORECASE)
        part_match = re.search(r'part[ _-]*(\d+)', filename, re.IGNORECASE)

        if match:
            episode_num = match.group(1).zfill(2)
            new_name = f"ep{episode_num}"
            if part_match:
                new_name += f"_part{part_match.group(1).zfill(2)}"
            new_name += ext
            rename_list.append((filename, new_name))

    if not rename_list:
        messagebox.showinfo(APP_TITLE, "No matching episode files found!")
        return

    preview_win = tk.Toplevel()
    preview_win.title(APP_TITLE + " | Select Files to Rename")
    preview_win.geometry("750x600")
    preview_win.grab_set()

    canvas = tk.Canvas(preview_win)
    frame = tk.Frame(canvas)
    scrollbar = tk.Scrollbar(preview_win, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    file_vars = []
    for idx, (old, new) in enumerate(rename_list, 1):
        var = tk.IntVar(value=1)
        file_vars.append((var, old, new))
        cb = tk.Checkbutton(frame, text=f"{idx:03d}. {old} → {new}", variable=var, anchor="w", width=100, justify="left")
        cb.pack(anchor="w", padx=10, pady=2)

    def set_all(val):
        for var, _, _ in file_vars:
            var.set(val)

    toggle_frame = tk.Frame(preview_win)
    toggle_frame.pack(pady=5)
    tk.Button(toggle_frame, text="Select All", command=lambda: set_all(1)).pack(side=tk.LEFT, padx=5)
    tk.Button(toggle_frame, text="Unselect All", command=lambda: set_all(0)).pack(side=tk.LEFT, padx=5)

    def on_confirm():
        selected = [(old, new) for var, old, new in file_vars if var.get() == 1]
        if not selected:
            messagebox.showwarning(APP_TITLE, "No files selected to rename!")
            return
        preview_win.destroy()
        renamed = 0
        for old, new in selected:
            try:
                os.rename(
                    os.path.join(folder_path, old),
                    os.path.join(folder_path, new)
                )
                renamed += 1
            except Exception as e:
                print(f"Failed to rename {old}: {e}")
        messagebox.showinfo(APP_TITLE, f"✅ Renamed {renamed}/{len(selected)} files.")

    btn_frame = tk.Frame(preview_win)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="✅ Rename Selected", command=on_confirm, bg="#4CAF50", fg="white", padx=10).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="❌ Cancel", command=preview_win.destroy, bg="#f44336", fg="white", padx=10).pack(side=tk.LEFT)

    footer = tk.Label(preview_win, text="Developed by Jam Amjad Rasheed", font=("Arial", 9), fg="gray")
    footer.pack(side=tk.BOTTOM, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_preview_and_confirm()
    root.mainloop()
