import webbrowser
import random
from pynput.keyboard import Key, Controller
import time
import getpass

keyboard = Controller()
USER_NAME = getpass.getuser()


def random_video_link(random_video_ids):
    random_video_id = random.choice(random_video_ids)
    random_video_link = f"https://www.youtube.com/watch?v={random_video_id}"
    return random_video_link


def play_video(link):
    webbrowser.open_new_tab(link)
    # boost volume
    for i in range(100):
        keyboard.press(Key.media_volume_up)

    # fullscreen mode
    time.sleep(10)
    keyboard.press("f")


# def add_to_startup():
#     startup_folder = f'C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
#     dir_path = os.getcwd()
#     # file_path = f'{dir_path}\\Motivation.exe'
#     file_path = f'{dir_path}\\main.py'

#     print(startup_folder)
#     print(file_path)
#     if "motivation.bat" not in os.listdir(startup_folder):
#         with open(f"{startup_folder}\\motivation.bat", "w+") as bat_file:
#             bat_file.write(f'start "{file_path}"')


def main():
    motivational_videos_ids = ["g-jwWYX7Jlo", "V3WrCx3mwNo",
                               "ERClHCOF14c", "QTB1YiWxxKU", "QTB1YiWxxKU", "wnHW6o8WMas"]
    video_link = random_video_link(motivational_videos_ids)
    play_video(video_link)


if __name__ == '__main__':
    main()
    exit()
