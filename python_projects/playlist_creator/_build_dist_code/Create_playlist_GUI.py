import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class PlaylistCreator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playlist Creator")
        self.setGeometry(100, 100, 400, 200)

        # Create UI elements
        self.video_folder_label = QLabel("Video Folder:")
        self.video_folder_line = QLineEdit()
        self.video_folder_button = QPushButton("Browse")
        self.video_folder_button.clicked.connect(self.browse_video_folder)

        self.save_location_label = QLabel("Save Location:")
        self.save_location_line = QLineEdit()
        self.save_location_button = QPushButton("Browse")
        self.save_location_button.clicked.connect(self.browse_save_location)

        self.playlist_name_label = QLabel("Playlist Name:")
        self.playlist_name_line = QLineEdit()

        self.create_button = QPushButton("Create Playlist")
        self.create_button.clicked.connect(self.create_playlist)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_folder_label)
        layout.addWidget(self.video_folder_line)
        layout.addWidget(self.video_folder_button)
        layout.addWidget(self.save_location_label)
        layout.addWidget(self.save_location_line)
        layout.addWidget(self.save_location_button)
        layout.addWidget(self.playlist_name_label)
        layout.addWidget(self.playlist_name_line)
        layout.addWidget(self.create_button)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def browse_video_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Video Folder")
        if folder_path:
            self.video_folder_line.setText(folder_path)

    def browse_save_location(self):
        save_location = QFileDialog.getExistingDirectory(self, "Select Save Location")
        if save_location:
            self.save_location_line.setText(save_location)

    def create_playlist(self):
        folder_path = self.video_folder_line.text()
        save_location = self.save_location_line.text() or os.path.dirname(folder_path)
        playlist_name = self.playlist_name_line.text()

        if not os.path.exists(folder_path):
            self.show_error("The specified folder path does not exist.")
            return

        if not os.path.exists(save_location):
            self.show_error("Save location does not exist.")
            return

        video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

        if not video_files:
            self.show_error("No video files found in the specified folder.")
            return

        if not playlist_name:
            self.show_error("Please provide a name for the playlist.")
            return

        if not playlist_name.endswith('.m3u'):
            playlist_name += '.m3u'

        save_path = Path(save_location)
        existing_files = [file.name for file in save_path.iterdir()]
        if playlist_name in existing_files:
            base_name, ext = os.path.splitext(playlist_name)
            counter = 0
            while True:
                new_name = f"{base_name}_0{counter}{ext}"
                if new_name not in existing_files:
                    playlist_name = new_name
                    break
                counter += 1

        final_save_location = Path(save_location) / playlist_name

        try:
            with final_save_location.open('w', encoding='utf-8') as playlist:
                for file in video_files:
                    file_path = Path(folder_path) / file
                    playlist.write(str(file_path) + '\n')
        except PermissionError:
            self.show_error("Write permission is denied by the system administrator. Please choose another folder to save the file.")
            return

        self.show_success(f"Playlist '{playlist_name}' created successfully at {final_save_location}.")

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.exec_()

    def show_success(self, message):
        success_dialog = QMessageBox()
        success_dialog.setIcon(QMessageBox.Information)
        success_dialog.setText(message)
        success_dialog.exec_()

    def show_success(self, message):
        success_dialog = QMessageBox()
        success_dialog.setIcon(QMessageBox.Information)
        success_dialog.setText(message)
        success_dialog.finished.connect(self.close_application)  # Connect finished signal to close_application
        success_dialog.exec_()

    def close_application(self):
        QTimer.singleShot(100, QApplication.instance().quit)  # Close the application after a small delay

if __name__ == "__main__":
    app = QApplication(sys.argv)
    playlist_creator = PlaylistCreator()
    playlist_creator.show()
    sys.exit(app.exec_())
