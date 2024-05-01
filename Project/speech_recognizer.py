import tkinter as tk
import speech_recognition as sr
import subprocess
import screen_brightness_control as sbc  # Brightness control library

def listen():
    """
    Listens to user's voice and performs actions based on the recognized text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_box.insert(tk.END, text + "\n")
            handle_commands(text.lower())
        except sr.UnknownValueError:
            print("Sorry, could not recognize the text")
        except sr.RequestError:
            print("Sorry, could not request results from Google Speech Recognition")

def handle_commands(text):
    """
    Handles commands based on the recognized text.
    """
    commands = {
        "open notepad": "notepad.exe",
        "open explorer": "explorer.exe",
        "open task manager": "taskmgr.exe",
        "increase brightness": "increase_brightness",
        "decrease brightness": "decrease_brightness",
        "mute": "mute_audio",
        "unmute": "unmute_audio"
    }
    if text in commands:
        if commands[text] == "increase_brightness":
            increase_brightness()
        elif commands[text] == "decrease_brightness":
            decrease_brightness()
        elif commands[text] == "mute_audio":
            mute_audio()
        elif commands[text] == "unmute_audio":
            unmute_audio()
        else:
            subprocess.Popen(commands[text])

def increase_brightness():
    """
    Increases the screen brightness by a small amount.
    """
    current_brightness = sbc.get_brightness()
    new_brightness = min(current_brightness + 10, 100)  # Limit max brightness
    sbc.set_brightness(new_brightness)

def decrease_brightness():
    """
    Decreases the screen brightness by a small amount.
    """
    current_brightness = sbc.get_brightness()
    new_brightness = max(current_brightness - 10, 0)  # Limit min brightness
    sbc.set_brightness(new_brightness)

def mute_audio():
    """
    Mutes the system audio (might require additional libraries depending on OS).
    """
    # Implement mute functionality based on your OS (e.g., pycaw for Windows)
    print("Muting audio (implementation depends on OS)")

def unmute_audio():
    """
    Unmutes the system audio (might require additional libraries depending on OS).
    """
    # Implement unmute functionality based on your OS (e.g., pycaw for Windows)
    print("Unmuting audio (implementation depends on OS)")

root = tk.Tk()
root.title("Speech Recognizer")

text_box = tk.Text(root, height=10, width=50)
text_box.grid(column=0, row=0, padx=10, pady=10)

listen_button = tk.Button(root, text="Listen", command=listen)
listen_button.grid(column=1, row=0, padx=10, pady=10)

root.mainloop()