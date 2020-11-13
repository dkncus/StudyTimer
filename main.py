import threading
import win32api
import tkinter as tk
from playsound import playsound

class MediaController():
    def __init__(self):
        # Create empty list to hold timers
        self.current_timer = None

        # Check if it is currently running
        self.isRunning = False

    # Presses the built-in play/pause button
    def toggle_play_pause(self):
        # Press the play/pause button programmatically
        win32api.keybd_event(0xB3, win32api.MapVirtualKey(0xB3, 0))

    # On the press of the play/pause button, do something
    def on_button(self):
        # If the loop is not currently running and the button has been pressed
        if not self.isRunning:
            # Set the timer to be currently running
            print("Timer Running")
            self.isRunning = True

            # Start the Study Timer
            print("Starting Time Loop")
            self.study_time()

        # If the loop is currently running and the button has been pressed
        else:
            # Set the timer to be no longer running
            self.isRunning = False
            print("No Longer Running, killing timers")

            # Toggle play/pause
            self.toggle_play_pause()

            # Clear the list of timers
            self.clear_timers()

    # Stop all current timers, and clear the timer list
    def clear_timers(self):
        self.current_timer.cancel()
        self.current_timer = None

    # Start the study time
    def study_time(self):
        # Amount of study time in seconds
        study_time = 15
        print("Starting Study Time:", study_time, "seconds")

        # Toggle toggle play/pause
        self.toggle_play_pause()

        # Store timer, start the timer
        self.current_timer = threading.Timer(study_time, self.break_time)
        self.current_timer.start()

    # Start the break time
    def break_time(self):
        # Amount of break time in seconds
        break_time = 5
        print("Starting Break Time:", break_time, "seconds")

        # Toggle toggle play/pause
        self.toggle_play_pause()

        # Play an Alarm Sound
        playsound('end_study.mp3')

        # Store timer, start the timer
        self.current_timer = threading.Timer(break_time, self.study_time)
        self.current_timer.start()

if __name__ == '__main__':
    # Window Settings
    window = tk.Tk()
    window.title("StudyMan v1.0")
    window.resizable(False, False)
    window["bg"] = 'gray15'
    window.iconphoto(False, tk.PhotoImage(file = r'./play-pause.png',).zoom(5).subsample(20))
    media_controller = MediaController()

    # Entry Labels/Windows
    studyTimeLabel = tk.Label(window, text="Study Time", font=("Gotham", 12, 'bold'), fg='white')
    breakTimeLabel = tk.Label(window, text="Break Time", font=("Gotham", 12, 'bold'), fg='white')
    studyTime = tk.Label(window, text="50", font=("Gotham", 12, 'bold'), fg='white', width = 20)
    breakTime = tk.Label(window, text="10", font=("Gotham", 12, 'bold'), fg='white', width = 20)
    minuteLabel1 = tk.Label(window, text="min", font=("Gotham", 12, 'bold'), fg='white')
    minuteLabel2 = tk.Label(window, text="min", font=("Gotham", 12, 'bold'), fg='white')
    minuteLabel1['bg'] = 'gray15'
    minuteLabel2['bg'] = 'gray15'
    studyTime['bg'] = 'gray15'
    breakTime['bg'] = 'gray15'
    studyTimeLabel['bg'] = 'gray15'
    breakTimeLabel['bg'] = 'gray15'

    # Grid Packing Setup for Windows/Labels Windows
    studyTimeLabel.grid(row = 0, column = 0)
    breakTimeLabel.grid(row = 1, column = 0)
    studyTime.grid(row = 0, column = 1)
    breakTime.grid(row = 1, column = 1)
    minuteLabel1.grid(row = 0, column = 2)
    minuteLabel2.grid(row = 1, column = 2)

    # Play/pause button
    photo = tk.PhotoImage(file = r'./play-pause.png').zoom(5).subsample(20)
    button = tk.Button(
        image = photo,
        bg = "green2",
        fg = "black",
        command = media_controller.on_button,
    )
    button.grid(row = 2, column = 1)

    window.mainloop()