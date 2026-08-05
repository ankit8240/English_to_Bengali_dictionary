<div align="center">

# 🔤 Bengali Keyboard Mapper

### A lightweight **Input Method Engine (IME)** for seamless English → Bengali typing in real time.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-orange?style=for-the-badge)

*A configurable keyboard remapping engine that captures global keyboard events and instantly converts English keystrokes into Bengali Unicode characters.*

</div>

---

# 📖 Overview

**Bengali Keyboard Mapper** is a Python-based Input Method Engine (IME) that enables users to type Bengali characters using a standard English keyboard.

Instead of changing your operating system's keyboard layout, the application intercepts global keyboard events and translates keystrokes according to a customizable mapping file.

Designed to be lightweight, fast, and easily extensible, it provides a smooth typing experience while preserving common keyboard shortcuts.

---

# ✨ Features

- 🌐 **Global Keyboard Hooking**
  - Captures keyboard input system-wide.

- ⚡ **Real-Time Translation**
  - Converts English characters into Bengali instantly.

- 📝 **Custom Character Mapping**
  - Configure the keyboard layout using `map.txt`.

- 🔤 **Unicode Support**
  - Supports UTF-8 encoded Bengali characters.

- 🎛️ **Modifier Key Handling**
  - Preserves common shortcuts such as `Ctrl+C`, `Ctrl+V`, and `Ctrl+X`.

- 🚀 **Lightweight & Fast**
  - Minimal resource usage with instant character translation.

- 🛑 **Graceful Exit**
  - Press **ESC** at any time to stop the application.

---

# 📂 Project Structure

```text
Bengali-Keyboard-Mapper/
│
├── bengali_mapper.py      # Main application
├── map.txt                # English → Bengali mapping
├── requirements.txt
└── README.md
```

---

# ⚙️ Requirements

- Python 3.8+
- keyboard library

Install the required dependency:

```bash
pip install keyboard
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/Bengali-Keyboard-Mapper.git
```

Navigate into the project:

```bash
cd Bengali-Keyboard-Mapper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python bengali_mapper.py
```

---

# ⚙️ Configuration

The keyboard layout is defined in the `map.txt` file.

Each line follows the format:

```text
EnglishKey:BengaliCharacter
```

Example:

```text
a:অ
b:ব
c:চ
d:দ
e:এ
```

> **Note:** Save the file using **UTF-8 encoding** to ensure proper Unicode support.

---

# ▶️ Usage

1. Run the application.
2. Type normally using your keyboard.
3. English characters are automatically translated into Bengali.
4. Standard **Ctrl** keyboard shortcuts continue to work.
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
Load map.txt
      │
      ▼
Character Lookup
      │
      ├── Match Found
      │      │
      │      ▼
      │ Output Bengali Character
      │
      └── No Match
             │
             ▼
      Output Original Character
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming Language |
| ⌨️ keyboard | Global Keyboard Event Handling |
| 🔤 UTF-8 | Unicode Bengali Character Encoding |
