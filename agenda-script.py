import sys
import time
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt6.QtCore import QTimer, Qt


class TopicTimer(QWidget):
    def __init__(self, agenda):
        super().__init__()
        self.agenda = agenda
        self.current_index = 0
        self.time_remaining = 0
        self.timer_running = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.init_ui()
        self.load_topic(0)

    def init_ui(self):
        self.setWindowTitle("Meeting Timer")
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.resize(400, 240)

        self.layout = QVBoxLayout()

        # Labels first: current topic, timer, next topic
        self.current_topic_label = QLabel("", self)
        self.current_topic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_topic_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.current_topic_label)

        self.timer_label = QLabel("", self)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 48px;")
        self.layout.addWidget(self.timer_label)

        self.next_topic_label = QLabel("", self)
        self.next_topic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.next_topic_label.setStyleSheet("font-size: 16px; color: gray;")
        self.layout.addWidget(self.next_topic_label)

        # Buttons: initially hidden as needed
        self.skip_button = QPushButton("Skip", self)
        self.skip_button.clicked.connect(self.skip_topic)
        self.skip_button.setVisible(False)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setVisible(False)

        self.restart_button = QPushButton("Restart", self)
        self.restart_button.clicked.connect(self.restart_timer)
        self.restart_button.setVisible(False)

        # Buttons added after labels (bottom of layout)
        self.layout.addWidget(self.skip_button)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.restart_button)

        self.setLayout(self.layout)

    def load_topic(self, index):
        if index < len(self.agenda):
            topic, duration = self.agenda[index]
            self.time_remaining = duration
            self.current_topic_label.setText(f"Current: {topic}")
            self.timer_label.setText(self.format_time(self.time_remaining))
            if index + 1 < len(self.agenda):
                next_topic = self.agenda[index + 1][0]
                self.next_topic_label.setText(f"Next: {next_topic}")
            else:
                self.next_topic_label.setText("Next: End")
        else:
            self.current_topic_label.setText("Current: End")
            self.timer_label.setText("")
            self.next_topic_label.setText("")
            self.timer.stop()
            self.timer_running = False
            self.stop_button.setVisible(False)
            self.skip_button.setVisible(False)
            self.restart_button.setVisible(True)

    def start_timer(self):
        if self.current_index < len(self.agenda):
            self.timer.start(1000)
            self.timer_running = True
            self.start_button.setVisible(False)
            self.stop_button.setVisible(True)
            self.skip_button.setVisible(True)
            self.restart_button.setVisible(True)

    def stop_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.stop_button.setVisible(False)
        self.start_button.setVisible(True)

    def restart_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.current_index = 0
        self.load_topic(0)
        self.skip_button.setVisible(False)
        self.start_button.setVisible(True)
        self.stop_button.setVisible(False)
        self.restart_button.setVisible(False)

    def skip_topic(self):
        self.current_index += 1
        if self.current_index < len(self.agenda):
            self.load_topic(self.current_index)
            if self.timer_running:
                self.timer.start(1000)
        else:
            self.load_topic(self.current_index)

    def update_timer(self):
        self.time_remaining -= 1
        if self.time_remaining >= 0:
            self.timer_label.setText(self.format_time(self.time_remaining))
        else:
            self.current_index += 1
            if self.current_index < len(self.agenda):
                self.load_topic(self.current_index)
            else:
                self.load_topic(self.current_index)

    @staticmethod
    def format_time(seconds):
        return time.strftime('%M:%S', time.gmtime(seconds))


def load_agenda_from_file(file_path):
    agenda = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) == 2:
                    topic = parts[0].strip()
                    try:
                        duration = int(parts[1].strip())
                        agenda.append((topic, duration))
                    except ValueError:
                        pass
    return agenda


def main():
    if len(sys.argv) < 2:
        print("Usage: python agenda-script.py agenda.txt")
        sys.exit(1)

    agenda_file = sys.argv[1]
    agenda = load_agenda_from_file(agenda_file)

    app = QApplication(sys.argv)
    timer = TopicTimer(agenda)
    timer.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()