import os
from pathlib import Path

def create_playlist():
    while True:
        folder_path = input("Enter the path to the folder containing video files: ")
        if os.path.exists(folder_path):
            break
        else:
            print("The specified folder path does not exist.")
            choice = input("Do you wish to continue? (yes/no): ").lower()
            if choice == "no":
                print("Program terminated.")
                return

    while True:
        save_location = input("Enter the save location for the playlist (press Enter for current directory): ") or os.path.dirname(folder_path)
        if os.path.exists(save_location):
            break
        else:
            print("Save location does not exist.")
            choice = input("Do you wish to continue? (yes/no): ").lower()
            if choice == "no":
                print("Program terminated.")
                return

    video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    if not video_files:
        print("No video files found in the specified folder.")
        return

    while True:
        playlist_name = input("Enter the name for the playlist (e.g., my_playlist): ")
        if playlist_name:
            break
        else:
            print("Please provide a name for the playlist.")

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

    final_save_location = save_path / playlist_name

    try:
        with final_save_location.open('w') as playlist:
            for file in video_files:
                playlist.write(os.path.join(folder_path, file) + '\n')
    except PermissionError:
        print("Write permission is denied by the system administrator. Please choose another folder to save the file.")
        return

    print(f"\nPlaylist '{playlist_name}' created successfully at {final_save_location}.")

if __name__ == "__main__":
    create_playlist()
