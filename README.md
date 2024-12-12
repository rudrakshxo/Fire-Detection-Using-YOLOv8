# Fire and Smoke Detection using YOLO and OpenCV

This project demonstrates real-time object detection for fire and smoke using the YOLO (You Only Look Once) model and OpenCV. The system is capable of processing video files or live camera feeds to identify fire and smoke in the environment.

## Features
- Detects fire and smoke with bounding boxes and confidence scores.
- Real-time processing of video or live camera feeds.
- Displays annotated frames with labels and bounding boxes.

## Requirements

### Software
- Python 3.8+
- OpenCV
- Ultralytics YOLO library

### Hardware
- A computer with a GPU (for faster inference, optional).
- A webcam or a video file for testing.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fire-smoke-detection.git
   cd fire-smoke-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the trained YOLO model (`BestModel.pt`) and place it in the project directory.

4. Ensure your webcam is functional or have a video file ready for testing.

## Usage

### Running with a Video File
1. Update the `video_path` variable in the code to point to your video file.
2. Run the script:
   ```bash
   python detect.py
   ```

### Running with Live Camera Feed
1. Modify the `cap` initialization in the code:
   ```python
   cap = cv2.VideoCapture(0)  # For the default webcam
   ```
2. Execute the script:
   ```bash
   python detect.py
   ```

### Exiting
- Press the `q` key to terminate the live feed or video processing.

## Code Overview

### Main Components
- **YOLO Model Loading:**
  ```python
  model = YOLO('BestModel.pt')
  ```
  Loads the pretrained YOLO model.

- **Class Definitions and Colors:**
  ```python
  classnames = ['Fire', 'Smoke']
  colors = {'Fire': (0, 0, 255), 'Smoke': (255, 0, 0)}
  ```
  Defines the object classes and their respective bounding box colors.

- **Video Processing:**
  - Reads frames from a video file or camera feed using OpenCV.
  - Resizes frames to maintain aspect ratio and prepares them for YOLO inference.

- **Object Detection and Annotation:**
  - Performs object detection on each frame.
  - Draws bounding boxes, labels, and confidence scores.

- **Display and Termination:**
  - Displays the annotated frames in real time.
  - Terminates on pressing the `q` key.

## Example Output
- Bounding boxes drawn around detected fire or smoke.
- Confidence percentages displayed as labels.

## Future Enhancements
- Add support for logging detection events (e.g., save timestamps and classes).
- Integrate alarm or notification systems for detected hazards.
- Optimize inference speed for edge devices like Raspberry Pi.

## Acknowledgments
- **Ultralytics YOLO:** For the YOLO implementation.
- **OpenCV:** For video processing and display.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For questions or contributions, feel free to open an issue or submit a pull request!


