# 🎬 影片轉ASCII藝術

> Video to ASCII Art Converter — 一款基於 Python 的影片轉 ASCII 藝術轉換器，能夠將 MP4 影片檔案即時轉換為酷炫的 ASCII 字元動畫，帶有友好的圖形介面。

**Language / 语言 / 言語:** [简体中文](./README.md) · [English](./README.en.md) · [日本語](./README.ja.md) · [繁體中文](./README.zh-TW.md)

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge)](https://github.com/huqingyuan-Python/Video-to-ASCII-art)
[![License](https://img.shields.io/badge/license-BSL--1.0-orange?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/huqingyuan-Python/Video-to-ASCII-art?style=for-the-badge)](https://github.com/huqingyuan-Python/Video-to-ASCII-art/stargazers)

---

## ✨ 功能特點

- 🎬 **影片格式支援** — 支援 MP4 格式影片檔案的轉換
- 🔄 **即時轉換** — 根據影片實際幀率即時生成 ASCII 藝術動畫
- 🖥️ **圖形使用者介面** — 簡潔易用的 GUI 介面，點擊即可開始轉換
- 🎨 **擴展字元集** — 使用擴展 ASCII 字元集，呈現更細膩的畫面效果
- ⌨️ **命令列支援** — 同時提供命令列模式，方便整合和自動化

## 🚀 快速開始

### 環境需求

- Python 3.8+
- Windows / macOS / Linux

### 安裝依賴

```bash
pip install opencv-python numpy pillow
```

### 執行程式

```bash
python main.py
```

### 使用方法

1. 執行程式後，點擊「選擇影片」按鈕選擇 MP4 檔案
2. 等待影片載入完成
3. 點擊「開始轉換」按鈕開始 ASCII 藝術轉換
4. 按 `Q` 鍵退出預覽視窗

## 🔧 技術棧

| 技術 | 說明 |
|------|------|
| Python 3.8+ | 核心程式語言 |
| Tkinter | 圖形使用者介面 |
| OpenCV (cv2) | 影片讀取與影像處理 |
| NumPy | 數值計算與陣列操作 |
| Pillow (PIL) | 影像處理庫 |

## 📂 專案結構

```
Video-to-ASCII-art/
├── main.py          # 主程式檔案
├── README.md        # 專案說明文件
└── LICENSE          # 開源許可證
```

## ⚠️ 使用聲明

- **禁止商業用途** — 本程式不得用於任何商業目的
- **必須署名** — 使用時需標注來源：「哔哩哔哩@玩摄影的程序猿」

## 🤝 參與貢獻

歡迎提交 [Issue](https://github.com/huqingyuan-Python/Video-to-ASCII-art/issues) 或 Pull Request！

## 📄 許可證

本專案採用 [BSL-1.0 (Boost Software License)](LICENSE) 開源。