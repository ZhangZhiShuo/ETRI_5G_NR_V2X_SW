import os
import sys
import sender_window
import receiver_window
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class SelectWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Electronics and Telecommunications Research Institute')
        self.setWindowIcon(QIcon(resource_path('./resource/etri.png')))
        self.setFixedSize(700, 360)

        select_layout = QGridLayout()
        self.setLayout(select_layout)

        # Sender Button
        sender_select_button = QPushButton("Sender Window", self)
        sender_select_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sender_font = sender_select_button.font()
        sender_font.setPointSize(45)
        sender_select_button.setFont(sender_font)
        sender_select_button.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : rgb(169,169,169);"
            "border-color : rgb(0, 0, 0);"
            "border-style : solid;"
            "border-width : 2px;"
            "border-radius : 15px"
            "}"
            "QPushButton::hover"
            "{"
            "background-color : rgb(192,192,192);"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color : rgb(240, 240, 240);"
            "}"
        )
        sender_select_button.clicked.connect(lambda: self.show_sender_window(sender_select_button))
        select_layout.addWidget(sender_select_button)

        # Receiver Button
        receiver_select_button = QPushButton("Receiver Window", self)
        receiver_select_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        receiver_font = receiver_select_button.font()
        receiver_font.setPointSize(45)
        receiver_select_button.setFont(receiver_font)
        receiver_select_button.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : rgb(169,169,169);"
            "border-color : rgb(0, 0, 0);"
            "border-style : solid;"
            "border-width : 2px;"
            "border-radius : 15px"
            "}"
            "QPushButton::hover"
            "{"
            "background-color : rgb(192,192,192);"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color : rgb(240, 240, 240);"
            "}"
        )
        receiver_select_button.clicked.connect(lambda: self.show_receiver_window(receiver_select_button))
        select_layout.addWidget(receiver_select_button)

    def show_sender_window(self, button):
        try:
            self.sender_window = sender_window.SenderWindow()
            self.sender_window.show()
        except Exception as e:
            print(f"Failed to open sender window{e}")
            return
        self.close()

    def show_receiver_window(self, button):
        try:
            self.receiver_video_window = receiver_window.ReceiverVideoWindow()
            self.receiver_video_window.show()
        except Exception as e:
            print(f"Failed to open receiver window{e}")
            return
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sel_window = SelectWindow()
    sel_window.show()
    sys.exit(app.exec_())
