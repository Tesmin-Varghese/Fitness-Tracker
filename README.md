Overview
This Python program utilizes pose detection techniques to track squats in a fitness video. It employs the Pose Module (poseModule.py) to detect key points in a person's body and calculates the angles of the knees to determine whether the person is standing or crouching.

Requirements
Python 3.x
OpenCV (cv2)
NumPy
Installation
Clone the repository to your local machine.
Ensure Python 3.x is installed.
Install the required Python packages:

pip install opencv-python numpy
Usage
Run the program by executing the Python script.

python squat_tracker.py
The program will read the input video file specified within the script (squat.mp4 in this case).
It will process each frame, detect poses, and track squat repetitions.
The count of squats performed will be displayed in the terminal.
Press Esc key to exit the program.
Code Structure
poseModule.py: Module containing pose detection functionality.
squat_tracker.py: Main program that reads the input video, processes frames, detects poses, and tracks squat repetitions.
Workflow
The program reads frames from the input video using OpenCV.
It resizes each frame for better processing.
Pose detection is performed on each frame using the Pose Module.
Key points are identified to calculate the angles of the knees.
Squat repetitions are counted based on changes in knee angles.
The count of squats is displayed in the terminal.
The video with pose overlays is displayed in a window.
Functionality
Pose Detection: The program utilizes a pre-trained pose detection model to identify key points in a person's body.
Angle Calculation: It calculates the angle between specific body joints to determine squat positions.
Repetition Tracking: Squat repetitions are tracked based on changes in knee angles from standing to crouching positions and vice versa.
Interpolation: NumPy's interp function is used to convert angle values to a percentage scale.

Contributions and Issues
Contributions to the project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

Author
This program was created by Tesmin Varghese (https://github.com/Tesmin-Varghese).
