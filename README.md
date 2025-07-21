# 🎬 Episode Renamer - by Jam Amjad Rasheed

A GUI-based Python tool to rename episode files with:
- Preview before renaming
- Support for multi-part episodes (e.g. `Episode 05 Part 02`)
- Checkboxes to select/unselect files
- Clean output like: `ep05_part02.mp4`

## 🧰 How to Use (Python Version)

1. Install Python 3.10+
2. Save this file as `episode_renamer.py`
3. Run with:
   ```bash
   python episode_renamer.py

## 💾 How to Use as .EXE (No Python Required on Target PC)

To run on Windows without needing Python:

1. Install [Python](https://python.org) and then install PyInstaller:
pip install pyinstaller


2. Save this file as `episode_renamer.py` on your computer.

3. Open **Command Prompt** in that folder and run:
python -m PyInstaller --onefile --windowed episode_renamer.py


4. This will generate a standalone `.exe` file in the `dist/` folder.

---

## 📌 Notes

- ✅ Rename logic supports:  
`Episode 01`, `Ep_02`, `episode-03 part 01`, etc.

- ✅ Only files with supported extensions are included:  
`.mp4`, `.mkv`, `.avi`, `.mov`, `.mp3`, `.srt`

- ✅ Fully offline & portable – no internet needed after creating `.exe`

