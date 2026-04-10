# GitHub Repository: https://github.com/AbbyB2025/A8.git
# Abby Blundell u1114910
# A8SpritePreviewer

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
        self.fps = 1
        self.current_frame = 0
        self.is_playing = False
        # Add any other instance variables needed to track information as the program
        # runs here
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

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
        layout = QVBoxLayout()
        frame.setLayout(layout)

        top_layout = QHBoxLayout()
        self.sprite_label = QLabel()
        if self.frames:
            self.sprite_label.setPixmap(self.frames[0])
        top_layout.addWidget(self.sprite_label)
        layout.addLayout(top_layout)
        # Adding the image inside the horizontal layout which is inside the main vertical layout

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(1, 100)
        self.slider.setValue(self.fps)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.handle_slider_change)
        top_layout.addWidget(self.slider)
        layout.addLayout(top_layout)
        # Adding the slider inside the horizontal layout which is inside the main vertical layout
        # We did the image first because it's left side to right side oriented

        fps_layout = QHBoxLayout()
        fps_layout.addWidget(QLabel("Frames per second"))
        self.current_fps_label = QLabel(str(self.fps))
        fps_layout.addWidget(self.current_fps_label)
        layout.addLayout(fps_layout)
        # Adding a Frames Per Second inside a different horizontal layout
        # Will go below the other horizontal layout because of top to bottom orientation

        self.toggle_btn = QPushButton("Start")
        self.toggle_btn.clicked.connect(self.toggle_animation)
        layout.addWidget(self.toggle_btn)
        # Adding the Start Button at the very bottom because of top to bottom orientation

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        pause_action = file_menu.addAction("Pause")
        pause_action.triggered.connect(self.pause_animation)
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        # Adding a File menu on the top left that has Pause and Exit Actions

    def handle_slider_change(self, value):
        self.fps = value
        self.current_fps_label.setText(str(value))
        self.timer.setInterval(int(1000 // self.fps))

    def toggle_animation(self):
        if self.is_playing:
            self.pause_animation()
        else:
            self.timer.start(int(1000 / self.fps))
            self.toggle_btn.setText("Stop")
        self.is_playing = not self.is_playing

    def pause_animation(self):
        self.timer.stop()
        self.toggle_btn.setText("Start")

    def update_frame(self):
        if not self.frames: return
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.sprite_label.setPixmap(self.frames[self.current_frame])


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
