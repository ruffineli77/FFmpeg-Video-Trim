
import subprocess
import tkinter as tk
from tkinter import filedialog


def select_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Mp4 Files", "*.mp4")])
    return file_path


def select_filepath():
    root = tk.Tk()
    root.withdraw()

    directory_path = filedialog.askdirectory()
    return directory_path


def format_time():
    print("This will use an hour:min:sec format.")

    good_nums = False
    while good_nums is False:
        num_good_nums = 0

        hour = input("Hour: ")
        minute = input("Minute: ")
        second = input("Second: ")
        time_values = [hour, minute, second]

        for digit in time_values:
            if len(digit) > 2 or digit == "" or digit.isalpha():
                pass
            else:
                num_good_nums += 1

        # print(f"{num_good_nums} out of 3 entries are correct.")

        if num_good_nums < 3:
            print("Dont enter an empty number, a letter, or a number larger than 99.")
        elif num_good_nums == 3:
            good_nums = True

    if len(hour) == 1:
        hour = f"0{hour}"
    if len(minute) == 1:
        minute = f"0{minute}"
    if len(second) == 1:
        second = f"0{second}"

    return f"{hour}:{minute}:{second}"


# Might want add more to help the user be aware of valid start time based on video length.
def trim_video():
    print("Select a file to trim: ")
    selected_file = select_file()
    print("Select a new file location: ")
    new_location = select_filepath()
    file_name = input("Enter a file name: ")
    print("Select the time to begin trimming your video: ")
    start_time = format_time()
    print("Select the length of your video: ")
    duration = format_time()

    tc_test = "ffmpeg -i input.mp4 -ss 00:01:10 -t 00:01:05 -c:v copy -c:a copy output.mp4"

    trim_command = f'ffmpeg -i "{selected_file}" -ss {start_time} -t {duration} -c:v copy -c:a copy "{new_location}/{file_name}".mp4'

    subprocess.run(trim_command, shell=True)


trim_video()
