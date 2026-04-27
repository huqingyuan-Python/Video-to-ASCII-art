# 🎬 Video to ASCII Art Converter

> Python-based video to ASCII art converter — transforms MP4 video files into cool ASCII character animations in real-time, with a user-friendly GUI.

**Language / 语言 / 言語:** [简体中文](./README.md) · [English](./README.en.md) · [日本語](./README.ja.md) · [繁體中文](./README.zh-TW.md)

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge)](https://github.com/huqingyuan-Python/Video-to-ASCII-art)
[![License](https://img.shields.io/badge/license-BSL--1.0-orange?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/huqingyuan-Python/Video-to-ASCII-art?style=for-the-badge)](https://github.com/huqingyuan-Python/Video-to-ASCII-art/stargazers)

---

## ✨ Features

- 🎬 **Video Format Support** — Supports MP4 video file conversion
- 🔄 **Real-time Conversion** — Generates ASCII art animations in real-time based on actual video frame rate
- 🖥️ **Graphical User Interface** — Clean and easy-to-use GUI, click to start conversion
- 🎨 **Extended Character Set** — Uses extended ASCII character set for more detailed visuals
- ⌨️ **Command Line Support** — Also provides command line mode for integration and automation

## 🚀 Quick Start

### Requirements

- Python 3.8+
- Windows / macOS / Linux

### Install Dependencies

```bash
pip install opencv-python numpy pillow
```

### Run the Program

```bash
python main.py
```

### Usage

1. After running the program, click "Select Video" to choose an MP4 file
2. Wait for the video to load
3. Click "Start Conversion" to begin ASCII art conversion
4. Press `Q` to exit the preview window

## 🔧 Tech Stack

| Tech | Description |
|------|-------------|
| Python 3.8+ | Core programming language |
| Tkinter | Graphical user interface |
| OpenCV (cv2) | Video reading and image processing |
| NumPy | Numerical computation and array operations |
| Pillow (PIL) | Image processing library |

## 📂 Project Structure

```
Video-to-ASCII-art/
├── main.py          # Main program file
├── README.md        # Project documentation
└── LICENSE          # Open source license
```

## ⚠️ Usage Notice

- **No Commercial Use** — This program must not be used for any commercial purposes
- **Attribution Required** — When using, please credit: "Bilibili @玩摄影的程序猿"

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

This project is open source under [BSL-1.0 (Boost Software License)](LICENSE).