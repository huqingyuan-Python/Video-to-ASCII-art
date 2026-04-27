# 🎬 動画からASCIIアートへの変換ツール

> Pythonベースの動画からASCIIアートへの変換ツール — MP4動画ファイルをリアルタイムでクールなASCIIキャラクターアニメーションに変換。ユーザーフレンドリーなGUI付き。

**Language / 语言 / 言語:** [简体中文](./README.md) · [English](./README.en.md) · [日本語](./README.ja.md) · [繁體中文](./README.zh-TW.md)

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge)](https://github.com/huqingyuan-Python/Video-to-ASCII-art)
[![License](https://img.shields.io/badge/license-BSL--1.0-orange?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/huqingyuan-Python/Video-to-ASCII-art?style=for-the-badge)](https://github.com/huqingyuan-Python/Video-to-ASCII-art/stargazers)

---

## ✨ 機能特徴

- 🎬 **動画フォーマット対応** — MP4動画ファイルの変換に対応
- 🔄 **リアルタイム変換** — 実際の動画フレームレートに基づいてリアルタイムでASCIIアートアニメーションを生成
- 🖥️ **グラフィカルユーザーインターフェース** — シンプルで使いやすいGUI、クリックだけで変換開始
- 🎨 **拡張キャラクターセット** — 拡張ASCIIキャラクターセットを使用して、より詳細なビジュアルを表現
- ⌨️ **コマンドラインサポート** — 統合と自動化のためのコマンドラインモードも提供

## 🚀 クイックスタート

### 動作環境

- Python 3.8+
- Windows / macOS / Linux

### 依存関係のインストール

```bash
pip install opencv-python numpy pillow
```

### プログラムの実行

```bash
python main.py
```

### 使い方

1. プログラムを実行後、「動画を選択」ボタンをクリックしてMP4ファイルを選択
2. 動画の読み込みが完了するのを待つ
3. 「変換開始」ボタンをクリックしてASCIIアート変換を開始
4. `Q` キーを押してプレビューウィンドウを終了

## 🔧 技術スタック

| 技術 | 説明 |
|------|------|
| Python 3.8+ | コアプログラミング言語 |
| Tkinter | グラフィカルユーザーインターフェース |
| OpenCV (cv2) | 動画読み込みと画像処理 |
| NumPy | 数値計算と配列操作 |
| Pillow (PIL) | 画像処理ライブラリ |

## 📂 プロジェクト構造

```
Video-to-ASCII-art/
├── main.py          # メインプログラムファイル
├── README.md        # プロジェクトドキュメント
└── LICENSE          # オープンソースライセンス
```

## ⚠️ 使用に関する注意

- **商用利用禁止** — このプログラムはいかなる商用目的にも使用できません
- **クレジット表示必須** — 使用時は「哔哩哔哩@玩摄影的程序猿」と明記してください

## 🤝 コントリビュート

IssueまたはPull Request大歓迎！

## 📄 ライセンス

このプロジェクトは [BSL-1.0 (Boost Software License)](LICENSE) でオープンソース公開されています。