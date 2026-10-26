# episode_renamer.py
# Episode Renamer - by Jam Amjad Rasheed
# A GUI tool to rename episode files with preview, checkbox selection, and optional part support
# v2.0 - Added animations, hover effects, animated progress bar

import os
import re
import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox, ttk

APP_TITLE = "Episode Renamer - by Jam Amjad Rasheed"
APP_VERSION = "2.0"
SUPPORTED_EXTENSIONS = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.mp3', '.srt')

AUTHOR_NAME = "Jam Amjad Rasheed"
AUTHOR_YOUTUBE = "https://www.youtube.com/@jamamjadrasheed"
AUTHOR_GITHUB = "https://github.com/jamamjadalone"
REPO_URL = "https://github.com/jamamjadalone/episode-renamer"

# ---------- Animation helpers ----------

def fade_in(window, target_alpha=1.0, step=0.08, delay=15):
    """Smoothly fade in a Toplevel window."""
    try:
        window.attributes("-alpha", 0.0)
    except tk.TclError:
        return

    def _step(alpha=0.0):
        alpha += step
        if alpha >= target_alpha:
            window.attributes("-alpha", target_alpha)
            return
        window.attributes("-alpha", alpha)
        window.after(delay, lambda: _step(alpha))

    _step()


def slide_in(window, start_offset=-40, delay=8, steps=15):
    """Slide window in vertically for a subtle entrance effect."""
    window.update_idletasks()
    x = window.winfo_x()
    final_y = window.winfo_y()
    start_y = final_y + start_offset
    window.geometry(f"+{x}+{start_y}")

    def _step(i=0):
        if i > steps:
            window.geometry(f"+{x}+{final_y}")
            return
        progress = i / steps
        eased = 1 - (1 - progress) ** 3  # ease-out cubic
        new_y = int(start_y + (final_y - start_y) * eased)
        window.geometry(f"+{x}+{new_y}")
        window.after(delay, lambda: _step(i + 1))

    _step()


def add_hover_animation(widget, normal_bg, hover_bg):
    """Add a smooth color hover effect to a button."""
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg))


def flash_widget(widget, color="#4CAF50", original="#2b2b2b", times=2, delay=120):
    """Flash a widget briefly - used as success feedback."""
    def _toggle(n):
        if n <= 0:
            widget.config(bg=original)
            return
        current = widget.cget("bg")
        widget.config(bg=color if current == original else original)
        widget.after(delay, lambda: _toggle(n - 1))
    _toggle(times * 2)


# ---------- About dialog ----------

def open_link(url):
    webbrowser.open_new_tab(url)


def show_about_dialog(parent):
    about = tk.Toplevel(parent)
    about.title("About")
    about.geometry("380x420")
    about.configure(bg="#1e1e1e")
    about.resizable(False, False)
    about.grab_set()

    fade_in(about)
    slide_in(about, start_offset=-25)

    # Avatar circle with initials
    avatar_canvas = tk.Canvas(about, width=90, height=90, bg="#1e1e1e", highlightthickness=0)
    avatar_canvas.pack(pady=(28, 10))
    avatar_canvas.create_oval(5, 5, 85, 85, fill="#4CAF50", outline="")
    avatar_canvas.create_text(45, 45, text="JA", fill="white", font=("Segoe UI", 24, "bold"))

    tk.Label(
        about, text=AUTHOR_NAME, font=("Segoe UI", 14, "bold"),
        bg="#1e1e1e", fg="#ffffff"
    ).pack()

    tk.Label(
        about, text="Creator of Episode Renamer", font=("Segoe UI", 9),
        bg="#1e1e1e", fg="#9e9e9e"
    ).pack(pady=(2, 4))

    tk.Label(
        about, text=f"Episode Renamer v{APP_VERSION}", font=("Segoe UI", 9),
        bg="#1e1e1e", fg="#4CAF50"
    ).pack(pady=(0, 16))

    tk.Frame(about, bg="#333333", height=1).pack(fill=tk.X, padx=30, pady=(0, 16))

    def link_button(text, url, icon):
        btn = tk.Label(
            about, text=f"{icon}  {text}", font=("Segoe UI", 10),
            bg="#1e1e1e", fg="#e0e0e0", cursor="hand2", pady=8
        )
        btn.pack(fill=tk.X, padx=40)
        btn.bind("<Button-1>", lambda e: open_link(url))
        btn.bind("<Enter>", lambda e: btn.config(fg="#4CAF50"))
        btn.bind("<Leave>", lambda e: btn.config(fg="#e0e0e0"))
        return btn

    link_button("YouTube Channel", AUTHOR_YOUTUBE, "▶")
    link_button("GitHub Profile", AUTHOR_GITHUB, "🐙")
    link_button("Star this Repo", REPO_URL, "⭐")

    tk.Frame(about, bg="#333333", height=1).pack(fill=tk.X, padx=30, pady=(16, 12))

    close_btn = tk.Button(
        about, text="Close", command=about.destroy,
        bg="#333333", fg="white", activebackground="#444444", activeforeground="white",
        relief="flat", padx=20, pady=6, font=("Segoe UI", 9, "bold"), cursor="hand2", bd=0
    )
    close_btn.pack(pady=(0, 20))
    add_hover_animation(close_btn, "#333333", "#444444")


# ---------- Core logic ----------

def build_rename_list(folder_path):
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
    return rename_list


def show_preview_and_confirm():
    folder_path = filedialog.askdirectory(title="Select Folder with Episodes")
    if not folder_path:
        return

    rename_list = build_rename_list(folder_path)

    if not rename_list:
        messagebox.showinfo(APP_TITLE, "No matching episode files found!")
        return

    preview_win = tk.Toplevel()
    preview_win.title(APP_TITLE + " | Select Files to Rename")
    preview_win.geometry("750x650")
    preview_win.configure(bg="#1e1e1e")
    preview_win.grab_set()

    # Entrance animation
    fade_in(preview_win)
    slide_in(preview_win)

    header = tk.Label(
        preview_win,
        text=f"📂 {len(rename_list)} file(s) ready to rename",
        font=("Segoe UI", 12, "bold"),
        bg="#1e1e1e", fg="#4CAF50", pady=8
    )
    header.pack(fill=tk.X)

    list_frame_outer = tk.Frame(preview_win, bg="#1e1e1e")
    list_frame_outer.pack(fill=tk.BOTH, expand=True, padx=10)

    canvas = tk.Canvas(list_frame_outer, bg="#1e1e1e", highlightthickness=0)
    frame = tk.Frame(canvas, bg="#1e1e1e")
    scrollbar = tk.Scrollbar(list_frame_outer, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Mouse wheel scroll support
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    file_vars = []
    for idx, (old, new) in enumerate(rename_list, 1):
        var = tk.IntVar(value=1)
        file_vars.append((var, old, new))
        row = tk.Frame(frame, bg="#1e1e1e")
        row.pack(fill=tk.X, padx=5, pady=1)
        cb = tk.Checkbutton(
            row, text=f"{idx:03d}. {old}  →  {new}",
            variable=var, anchor="w", justify="left",
            bg="#1e1e1e", fg="#e0e0e0", selectcolor="#2b2b2b",
            activebackground="#2b2b2b", activeforeground="#4CAF50",
            font=("Consolas", 9), padx=8, pady=3
        )
        cb.pack(fill=tk.X)
        # subtle hover highlight per row
        row.bind("<Enter>", lambda e, r=row, c=cb: (r.config(bg="#292929"), c.config(bg="#292929")))
        row.bind("<Leave>", lambda e, r=row, c=cb: (r.config(bg="#1e1e1e"), c.config(bg="#1e1e1e")))

    def set_all(val):
        for var, _, _ in file_vars:
            var.set(val)

    toggle_frame = tk.Frame(preview_win, bg="#1e1e1e")
    toggle_frame.pack(pady=6)

    def styled_button(parent, text, command, bg, hover_bg, fg="white"):
        b = tk.Button(
            parent, text=text, command=command, bg=bg, fg=fg,
            activebackground=hover_bg, activeforeground=fg,
            relief="flat", padx=14, pady=6, font=("Segoe UI", 9, "bold"),
            cursor="hand2", bd=0
        )
        add_hover_animation(b, bg, hover_bg)
        return b

    styled_button(toggle_frame, "☑ Select All", lambda: set_all(1), "#333333", "#444444").pack(side=tk.LEFT, padx=5)
    styled_button(toggle_frame, "☐ Unselect All", lambda: set_all(0), "#333333", "#444444").pack(side=tk.LEFT, padx=5)

    # Animated progress bar (used during rename)
    progress_frame = tk.Frame(preview_win, bg="#1e1e1e")
    progress_frame.pack(fill=tk.X, padx=20, pady=(0, 4))
    progress = ttk.Progressbar(progress_frame, orient="horizontal", mode="determinate")
    progress.pack(fill=tk.X)
    progress_frame.pack_forget()  # hidden until rename starts

    status_label = tk.Label(preview_win, text="", bg="#1e1e1e", fg="#aaaaaa", font=("Segoe UI", 9))
    status_label.pack(pady=(0, 4))

    def animate_progress(selected, i=0, renamed=0):
        if i >= len(selected):
            progress_frame.pack_forget()
            preview_win.destroy()
            messagebox.showinfo(APP_TITLE, f"✅ Renamed {renamed}/{len(selected)} files.")
            return
        old, new = selected[i]
        try:
            os.rename(os.path.join(folder_path, old), os.path.join(folder_path, new))
            renamed += 1
        except OSError as e:
            print(f"Failed to rename {old}: {e}")
        progress["value"] = ((i + 1) / len(selected)) * 100
        status_label.config(text=f"Renaming {i + 1}/{len(selected)}: {new}")
        preview_win.after(40, lambda: animate_progress(selected, i + 1, renamed))

    def on_confirm():
        selected = [(old, new) for var, old, new in file_vars if var.get() == 1]
        if not selected:
            messagebox.showwarning(APP_TITLE, "No files selected to rename!")
            return
        progress_frame.pack(fill=tk.X, padx=20, pady=(0, 4))
        progress["value"] = 0
        confirm_btn.config(state="disabled")
        cancel_btn.config(state="disabled")
        animate_progress(selected)

    btn_frame = tk.Frame(preview_win, bg="#1e1e1e")
    btn_frame.pack(pady=10)

    confirm_btn = styled_button(btn_frame, "✅ Rename Selected", on_confirm, "#4CAF50", "#5fd66a")
    confirm_btn.pack(side=tk.LEFT, padx=10)

    cancel_btn = styled_button(btn_frame, "❌ Cancel", preview_win.destroy, "#f44336", "#ff6b5e")
    cancel_btn.pack(side=tk.LEFT)

    footer = tk.Label(
        preview_win, text="Developed by Jam Amjad Rasheed  •  About",
        font=("Segoe UI", 8), bg="#1e1e1e", fg="gray", cursor="hand2"
    )
    footer.pack(side=tk.BOTTOM, pady=6)
    footer.bind("<Button-1>", lambda e: show_about_dialog(preview_win))
    footer.bind("<Enter>", lambda e: footer.config(fg="#4CAF50"))
    footer.bind("<Leave>", lambda e: footer.config(fg="gray"))


def launch():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry("420x230")
    root.configure(bg="#1e1e1e")
    root.resizable(False, False)

    fade_in(root)

    tk.Label(
        root, text="🎬 Episode Renamer", font=("Segoe UI", 16, "bold"),
        bg="#1e1e1e", fg="#ffffff"
    ).pack(pady=(24, 4))
    tk.Label(
        root, text=f"v{APP_VERSION}  •  by {AUTHOR_NAME}", font=("Segoe UI", 9),
        bg="#1e1e1e", fg="#9e9e9e"
    ).pack(pady=(0, 20))

    def styled_launch_button(text, command, bg, hover_bg):
        b = tk.Button(
            root, text=text, command=command, bg=bg, fg="white",
            activebackground=hover_bg, activeforeground="white",
            relief="flat", padx=16, pady=8, font=("Segoe UI", 10, "bold"),
            cursor="hand2", bd=0
        )
        add_hover_animation(b, bg, hover_bg)
        return b

    styled_launch_button("📂 Select Folder & Start", show_preview_and_confirm, "#4CAF50", "#5fd66a").pack(pady=4, ipadx=10)
    styled_launch_button("ℹ️  About", lambda: show_about_dialog(root), "#333333", "#444444").pack(pady=4, ipadx=10)

    root.mainloop()


if __name__ == "__main__":
    launch()
