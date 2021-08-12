import webbrowser
import random
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def random_video_link(random_video_ids):
    random_video_id = random.choice(random_video_ids)
    random_video_link = f"https://www.youtube.com/watch?v={random_video_id}"
    return random_video_link


def play_video(link):
    webbrowser.open(link)
    # boost volume
    for i in range(60):
        keyboard.press(Key.brightness_up)


def main():
    motivational_videos_ids = ["g-jwWYX7Jlo", "V3WrCx3mwNo",
                               "ERClHCOF14c", "QTB1YiWxxKU", "QTB1YiWxxKU", "wnHW6o8WMas"]
    video_link = random_video_link(motivational_videos_ids)
    print(video_link)
    play_video(video_link)


if __name__ == '__main__':
    main()
    exit()
