# Gesture Based Volume Control

A Python application that allows you to control your system's volume using hand gestures, leveraging OpenCV and mediapipe for hand tracking, and pycaw for audio control.

## Technologies Used 
- **MediaPipe** - Hand tracking and landmark detection  
- **pycaw** - Windows audio volume control interface  
- **comtypes** - Windows COM object interoperability  
- **OpenCV** - Real-time video processing and rendering  
- **NumPy** - Mathematical operations for gesture analysis

## Installation 

### Prerequisites
- Windows OS (for pycaw audio control)
- Webcam
- Python 3.6+

### Setup
```
pip install opencv-python mediapipe numpy comtypes pycaw
```

## Project Structure 
```
Gesture Based Volume Control
├── HandTrackingModule.py    # Custom hand detection module
├── volume_control.py        # Main application script
└── README.md                # This file
```



# Hand Tracking Module

## Features
- Real-time hand landmark detection
- Finger position tracking (21 landmarks per hand)
- Gesture recognition (fingers up/down)
- Configurable detection parameters

## Methods
- **findHands()**: Processes image and draws hand landmarks
- **findPosition()**: Returns list of landmark coordinates
- **fingersUp()**: Detects which fingers are raised




# Volume Control

## Features 
- Real-time hand tracking using webcam
- Adjust system volume by pinching thumb and index finger
- Visual feedback with volume bar and percentage
- FPS counter to monitor performance
- Simple and intuitive interface

## Usage 
1. Run the application:
   ```bash
   python volume_control.py
   ```

2. Show your hand to the webcam.
3. Control volume by adjusting the distance between your thumb and index finger:
   - Bring fingers closer to decrease volume
   - Spread fingers apart to increase volume

4. Press `q` to quit the application.






