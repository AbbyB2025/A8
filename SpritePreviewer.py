# GitHub Repository: https://github.com/AbbyB2025/A8.git

import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)
        self.total_duration = 2.0
        self.fps = int(self.num_frames / self.total_duration)
        #self.is_playing = False
        # Add any other instance variables needed to track information as the program
        # runs here
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.
        self.setCentralWidget(frame)
        main_layout = QVBoxLayout()
        frame.setLayout(main_layout)

        self.sprite_label = QLabel("Sprite Area")
        self.sprite_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite_label.setMinimumSize(200, 200)
        self.sprite_label.setStyleSheet("border: 1px solid gray;")
        main_layout.addWidget(self.sprite_label)

        fps_layout = QHBoxLayout()
        self.fps_text_label = QLabel("Frames per second ")
        self.fps_value_label = QLabel(str(self.fps))

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 100)
        self.slider.setValue(self.fps)
        self.slider.valueChanged.connect(self.handle_fps_click)

        fps_layout.addWidget(self.fps_text_label)
        fps_layout.addWidget(self.slider)
        fps_layout.addWidget(self.fps_value_label)
        main_layout.addLayout(fps_layout)

        self.btn_toggle = QPushButton("Start")
        self.btn_toggle.clicked.connect(self.handle_button_click)
        main_layout.addWidget(self.btn_toggle)

        menu_bar = self.menuBar()
        options_menu = menu_bar.addMenu("Options")
        pause_action = options_menu.addAction("Pause")
        pause_action.triggered.connect(self.pause_animation)
        exit_action = options_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

    def handle_fps_click(self, value):
        self.fps = value
        self.fps_value_label.setText(str(value))
        if self.timer.isActive():
            self.timer.start(1000 // self.fps)

    def handle_button_click(self):
        if self.timer.isActive():
            self.pause_animation()
        else:
            self.timer.start(1000 // self.fps)
            self.btn_toggle.setText("Stop")

    def pause_animation(self):
        self.timer.stop()
        self.btn_toggle.setText("Start")

    def update_animation(self):
        print("Animating...")

    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
