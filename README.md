# 🎬 Episode Renamer - by Jam Amjad Rasheed

A GUI-based Python tool to rename episode files with:
- Preview before renaming
- Support for multi-part episodes (e.g. `Episode 05 Part 02`)
- Checkboxes to select/unselect files
- Clean output like: `ep05_part02.mp4`

---

## 🧰 How to Use (Python Version)

1. ✅ Install [Python 3.10+](https://www.python.org/downloads/)
   - During installation, **make sure to check the box**:  
     ✅ **"Add Python to PATH"**  
     This is important to avoid `'python' is not recognized` errors.

2. ✅ Save this script as:
   ```
   episode_renamer.py
   ```

3. ✅ Run it by opening **Command Prompt** and typing:
   ```bash
   python episode_renamer.py
   ```

---

## 💾 How to Create `.EXE` (No Python Needed Later)

You can create a `.exe` that runs on any Windows PC, even if Python isn't installed.

### 🔧 Steps:

1. ✅ Make sure Python is installed (see above)

2. ✅ Open **Command Prompt** and install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

3. ✅ In the same folder as `episode_renamer.py`, run:
   ```bash
   python -m PyInstaller --onefile --windowed episode_renamer.py
   ```

4. ✅ Your `.exe` will be created in the `dist/` folder:
   ```
   dist/episode_renamer.exe
   ```

---

## 🖥️ Running the EXE

- Just double-click `episode_renamer.exe` to launch
- No need to install anything else
- Works fully offline
- You can share or move it anywhere

---

## 📌 Features

- ✅ Rename formats supported:
  ```
  Episode 01 → ep01.mp4
  Episode 05 Part 02 → ep05_part02.mkv
  Ep_09 → ep09.avi
  ```

- ✅ Supported file types:
  `.mp4`, `.mkv`, `.avi`, `.mov`, `.mp3`, `.srt`

- ✅ Preview window with:
  - Scrollable file list
  - Checkboxes to select/unselect
  - Safe renaming — only selected files are renamed

- ✅ Portable, fast, and beginner-friendly
- 🚫 Does not rename folders or unrelated files

---

## 🛠️ Troubleshooting

| Problem                              | Solution                                                                 |
|--------------------------------------|--------------------------------------------------------------------------|
| `'python' is not recognized`         | Reinstall Python and **check "Add to PATH"** during setup                |
| `Permission denied` errors           | Try running Command Prompt as **Administrator**                         |
| `.exe` not opening                   | Make sure `--windowed` flag was used in PyInstaller to hide console     |
| GUI doesn't show / closes instantly  | Run `.py` file first to test; check for file permission or crash issues |

---

**✨ Developed by Jam Amjad Rasheed**  
Fork, contribute, or improve — feedback welcome!


