Simple Python Screen Recorder

A simple Python application that captures your computer screen and saves the recording as a video file.

Requirements

Make sure you have Python 3 installed along with the following libraries:

OpenCV

pip install opencv-python


NumPy

pip install numpy


PyAutoGUI

pip install pyautogui

How to Use

Run the record.py script.

Enter the desired filename without the file extension.

The screen will be recorded for 5 seconds by default.

To change the recording duration, modify the recording_duration value in the script.

The recorded video will be saved in MP4 format using the following filename format:

filename_YYYY-MM-DD_HH-MM-SS.mp4

Example

If you enter:

test


the recorded video will be saved as:

test_2023-12-15_12-46-51.mp4


The resulting video can then be played using any standard video player.
