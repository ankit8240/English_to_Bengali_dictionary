<div align="center">

# 🔤 Bengali Keyboard Mapper

### A lightweight **Input Method Engine (IME)** for seamless English → Bengali typing in real time.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-orange?style=for-the-badge)

*A configurable keyboard remapping engine that captures global keyboard events and instantly converts English keystrokes into Bengali Unicode characters.*

</div>

---

## 📖 Overview

**Bengali Keyboard Mapper** is a Python-based Input Method Engine (IME) that enables users to type Bengali characters using a standard English keyboard.

Instead of changing your operating system's keyboard layout, the application intercepts keyboard events globally and translates keystrokes according to a customizable mapping file.

Designed to be lightweight, fast, and easily extensible, it provides a smooth typing experience while preserving common keyboard shortcuts.

---

## ✨ Features

- 🌐 **Global Keyboard Hooking**
  - Captures keyboard input system-wide.

- ⚡ **Real-Time Translation**
  - Converts English characters into Bengali instantly.

- 📝 **Custom Mapping**
  - Fully configurable using `map.txt`.

- 🔤 **Unicode Support**
  - Supports UTF-8 Bengali characters.

- 🎛️ **Modifier Key Handling**
  - Preserves `Ctrl` shortcuts like `Ctrl+C`, `Ctrl+V`, etc.

- 🚀 **Lightweight**
  - Minimal resource consumption.

- 🛑 **Graceful Exit**
  - Press **ESC** anytime to stop the application.

---

# 📂 Project Structure

```
Bengali-Keyboard-Mapper/
│
├── bengali_mapper.py      # Main application
├── map.txt                # English → Bengali mapping
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚙️ Requirements

- Python 3.8+
- keyboard library

Install dependencies

```bash
pip install keyboard
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/USERNAME/Bengali-Keyboard-Mapper.git
```

Navigate into the project

```bash
cd Bengali-Keyboard-Mapper
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the program

```bash
python bengali_mapper.py
```

---

# ⚙️ Configuration

The keyboard layout is defined inside

```
map.txt
```

Each line follows the format

```
EnglishKey:BengaliCharacter
```

Example

```text
a:অ
b:ব
c:চ
d:দ
e:এ
```

The mapping file must be saved using **UTF-8 encoding**.

---

# ▶️ Usage

1. Start the application.
2. Begin typing normally.
3. English keystrokes are automatically replaced with Bengali characters.
4. Standard **Ctrl** shortcuts continue working.
5. Press **ESC** to terminate the application.

---

# ⚡ Workflow

```text
Keyboard Input
      │
      ▼
Global Keyboard Hook
      │
      ▼
Read Mapping (map.txt)
      │
      ▼
Character Lookup
      │
      ├── Found
      │      │
      │      ▼
      │ Output Bengali Character
      │
      └── Not Found
             │
             ▼
      Output Original Character
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming Language |
| ⌨️ keyboard | Global Keyboard Event Hooking |
| 🔤 UTF-8 | Unicode Bengali Character Support |

</div>
