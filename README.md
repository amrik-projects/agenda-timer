# 🕒 Meeting Agenda Timer

A lightweight, floating meeting timer app built with Python and PyQt6.

Perfect for structured meetings where each topic has a time limit. Display one topic at a time with a countdown, move automatically to the next, and stay on track with a clean, always-on-top interface.

---

## ✅ Features

- Displays the current topic with a large countdown timer
- Shows the next upcoming topic
- Automatically moves to the next agenda item
- Floating window stays on top (macOS and Windows)
- Manual **Start**, **Stop**, **Skip**, and **Restart** controls
- Displays "End" when the final topic is finished

---

## 📦 Requirements

- Python 3.9 or newer
- PyQt6

---

## 🔧 Set Up the Environment

### macOS or Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install PyQt6
```

### Windows (Command Prompt or PowerShell)

```cmd
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install PyQt6
```

---

## 📄 Creating Your Agenda File

Create a plain text file called `agenda.txt` with one agenda item per line.  
Each line should contain a topic and duration in **seconds**, separated by a comma.

Example:

```
Introductions,60
Team Update,180
Budget Review,300
Q&A,120
```

---

## ▶️ Running the App

Once your virtual environment is activated and `PyQt6` is installed, run:

```bash
python agenda-script.py agenda.txt
```

This will open a floating window that shows:

- **Current topic**
- **Countdown timer**
- **Next topic**
- **Control buttons**

---

## 🎛 Controls

| Button   | Action                             |
|----------|------------------------------------|
| Start    | Begin the timer                    |
| Stop     | Pause the timer                    |
| Skip     | Move to the next agenda item       |
| Restart  | Reset the agenda from the beginning |

The **Skip** and **Restart** buttons only appear after starting the timer.

---

## 🖥 Notes for Windows Users

- The script works out of the box on Windows.
- The always-on-top window flag is supported, but behavior may vary slightly depending on your window manager or system settings.

---

## 🛠 Optional Enhancements (Ideas)

- Accept `MM:SS` formatted durations
- Sound alert between agenda items
- Keyboard shortcuts for controls
- Export session log of start/end times per topic

---

## 📄 License

MIT License

This project is open source and free to use or adapt for your needs.
