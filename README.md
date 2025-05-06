# 🕒 Meeting Agenda Timer

<img src="meeting_timer_screenshot.png?raw=true" width="500px"/>

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
- Dark mode UI with prominent text and controls
- **Optional chime** sound when each new topic begins

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

Basic usage:

```bash
python agenda-script.py agenda.txt
```

To enable the **chime sound** on each new topic:

```bash
python agenda-script.py agenda.txt --chime
```

---

## 🔔 Using a Chime Sound

You can use any short `.wav` sound file to play when the timer switches to a new topic.

### Recommended chime

Download this soft chime sound from Pixabay:  
[https://pixabay.com/sound-effects/chime-sound-7143/](https://pixabay.com/sound-effects/chime-sound-7143/)

Save the file as `chime.mp3`, then convert it to a `.wav` file.

### Convert to WAV using ffmpeg (macOS/Linux/Windows):

```bash
ffmpeg -i chime.mp3 -acodec pcm_s16le -ar 44100 chime.wav
```

Place the resulting `chime.wav` file in the same folder as `agenda-script.py`.

> Only `.wav` files are supported. MP3 is **not** compatible with PyQt6's audio system.

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

## 🛠 Optional Enhancements (Ideas)

- Accept `MM:SS` formatted durations
- Sound alert between agenda items (custom files per topic)
- Keyboard shortcuts for controls
- Export session log of start/end times per topic

---

## 📄 License

MIT License

This project is open source and free to use or adapt for your needs.
