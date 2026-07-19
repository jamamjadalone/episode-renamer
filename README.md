# 🎬 Episode Renamer — by Jam Amjad Rasheed

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](#-how-to-use-python-version)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)](#-features)
[![Stars](https://img.shields.io/github/stars/jamamjadalone/episode-renamer?style=social)](https://github.com/jamamjadalone/episode-renamer/stargazers)

**A free, open-source Python GUI tool to batch rename TV episodes, anime, and video files** — with a live preview, checkbox selection, multi-part episode support, and smooth animated UI.

Perfect for organizing messy download folders (`Ep_09.mkv`, `Episode 05 Part 02.mp4`, `episode-12.mp3`) into clean, consistent filenames like `ep09.mkv` and `ep05_part02.mp4`.

> 🔑 **Keywords:** episode renamer, batch file renamer, bulk rename tool, anime episode renamer, TV show file organizer, Python GUI renamer, tkinter batch rename, video file renamer, subtitle renamer, media file organizer

---

## 📸 Preview

| Before | After |
|:---:|:---:|
| ![Before renaming](assets/before.png) | ![After renaming](assets/after.png) |

*Messy, inconsistent filenames on the left — clean, standardized episode names on the right.*

---

## ✨ Features Overview

- 🎞️ **Fade-in + slide-in animation** when windows open
- 🖱️ **Hover effects** on all buttons for tactile, responsive feedback
- 📊 **Animated progress bar** with live status text while files are being renamed
- 🌒 **Dark-themed UI** for a modern, easy-on-the-eyes look
- 🖍️ **Row highlight on hover** in the file list for easier scanning
- 🖲️ **Mouse-wheel scrolling** support in the preview list
- 🔒 Safe, reliable renaming — only selected files are ever touched

---

## 🧰 How to Use (Python Version)

1. ✅ Install [Python 3.10+](https://www.python.org/downloads/)
   - During installation, **make sure to check the box**:
     ✅ **"Add Python to PATH"**
     This is important to avoid `'python' is not recognized` errors.

2. ✅ Clone or download this repository:
   ```bash
   git clone https://github.com/jamamjadalone/episode-renamer.git
   cd episode-renamer
   ```

3. ✅ (Optional, only needed if you plan to build a `.exe`) Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
   > No external packages are required just to **run** the app — `tkinter` ships with standard Python on Windows/macOS. On Linux, see [Troubleshooting](#️-troubleshooting) below.

4. ✅ Run it:
   ```bash
   python episode_renamer.py
   ```

---

## 💾 How to Create a `.EXE` (No Python Needed Later)

You can create a `.exe` that runs on any Windows PC, even if Python isn't installed.

### 🔧 Steps

1. ✅ Make sure Python is installed (see above)
2. ✅ Open **Command Prompt** and install PyInstaller:
   ```bash
   pip install -r requirements.txt
   ```
3. ✅ In the same folder as `episode_renamer.py`, run:
   ```bash
   python -m PyInstaller --onefile --windowed episode_renamer.py
   ```
4. ✅ Your `.exe` will be created in the `dist/` folder:
   ```
   dist/episode_renamer.exe
   ```

See [`How to Convert to .EXE.txt`](How%20to%20Convert%20to%20.EXE.txt) for the original step-by-step notes.

---

## 🖥️ Running the EXE

- Just double-click `episode_renamer.exe` to launch
- No need to install anything else
- Works fully offline
- You can share or move it anywhere

---

## 📌 Features

✅ Rename formats supported:

```
Episode 01           → ep01.mp4
Episode 05 Part 02   → ep05_part02.mkv
Ep_09                → ep09.avi
```

- ✅ Supported file types: `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.mp3`, `.srt`
- ✅ Preview window with:
  - Scrollable, animated file list
  - Checkboxes to select/unselect individual files
  - "Select All" / "Unselect All" shortcuts
  - Animated progress bar during renaming
  - Safe renaming — only selected files are renamed
- ✅ Portable, fast, and beginner-friendly
- 🚫 Does not rename folders or unrelated files

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `'python' is not recognized` | Reinstall Python and **check "Add to PATH"** during setup |
| `Permission denied` errors | Try running Command Prompt/Terminal as **Administrator** |
| `.exe` not opening | Make sure `--windowed` flag was used in PyInstaller to hide the console |
| GUI doesn't show / closes instantly | Run the `.py` file first to test; check for file permission or crash issues |
| `ModuleNotFoundError: No module named 'tkinter'` (Linux) | Run `sudo apt-get install python3-tk` (Debian/Ubuntu) or the equivalent for your distro |
| Animations feel slow on older PCs | This is expected on very low-spec hardware; the app still functions normally |

---

## 📂 Project Structure

```
episode-renamer/
├── episode_renamer.py       # Main application (GUI + renaming logic)
├── requirements.txt         # Dependencies (only needed for building .exe)
├── LICENSE                  # MIT License
├── README.md                # This file
├── sitemap.xml              # SEO sitemap
├── robots.txt               # SEO crawler rules
├── How to Convert to .EXE.txt
└── assets/
    ├── before.png            # Screenshot: messy filenames
    └── after.png              # Screenshot: renamed filenames
```

---

## 🗺️ Roadmap

- [ ] Custom rename pattern editor (user-defined templates)
- [ ] Drag-and-drop folder support
- [ ] Undo last rename batch
- [ ] Cross-platform `.app` / `.AppImage` builds

Have an idea? [Open an issue](https://github.com/jamamjadalone/episode-renamer/issues) — contributions welcome!

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

Released under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

## 👤 About the Author

<div align="center">

### Jam Amjad Rasheed

*Tech creator • Building simple tools that save people time*

[![YouTube](https://img.shields.io/badge/YouTube-@jamamjadrasheed-red?logo=youtube&logoColor=white&style=for-the-badge)](https://www.youtube.com/@jamamjadrasheed)
[![GitHub](https://img.shields.io/badge/GitHub-jamamjadalone-181717?logo=github&logoColor=white&style=for-the-badge)](https://github.com/jamamjadalone)

</div>

I run a tech YouTube channel covering flashing guides, how-to solutions, apps, tips & tricks, and general tech help — and I build small practical tools like this one on the side.

- 🎥 **YouTube:** [@jamamjadrasheed](https://www.youtube.com/@jamamjadrasheed) — tech tutorials, tips, and how-to content
- 💻 **GitHub:** [@jamamjadalone](https://github.com/jamamjadalone) — more open-source tools and scripts
- 🌟 If this tool saved you time, consider [starring the repo](https://github.com/jamamjadalone/episode-renamer) or subscribing on YouTube — it genuinely helps!

> 💡 The app itself also has a built-in **About** section — click **"About"** in the launcher window or the preview window footer to open it directly.

---

**✨ Developed by Jam Amjad Rasheed**
Fork, contribute, or improve — feedback welcome!
