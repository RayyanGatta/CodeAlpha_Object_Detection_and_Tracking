Object Detection and Tracking System
====================================

This repository contains an **AI-powered object detection and tracking system** built using **YOLO (You Only Look Once)** for real-time detection and tracking of objects in video streams. The project is designed for high-performance and accurate detection, leveraging state-of-the-art deep learning models.

Features
--------

-   **Real-Time Object Detection:** Utilizes YOLOv5/YOLOv8 for efficient and accurate object detection.
-   **Object Tracking:** Incorporates Deep SORT for tracking objects across video frames.
-   **Video Support:** Processes live video streams or pre-recorded video files.
-   **Customizability:** Adjustable detection thresholds and easy integration of custom-trained models.
-   **GPU Acceleration:** Optimized for hardware acceleration using CUDA for faster inference.

Technology Stack
----------------

-   **Python 3.8+**
-   **YOLOv5/YOLOv8** for object detection (via the `ultralytics` library)
-   **Deep SORT** for object tracking
-   **OpenCV** for video processing
-   **Matplotlib** (optional) for visualization and saving annotated frames

Use Cases
---------

-   Real-time surveillance systems
-   Autonomous driving
-   Retail analytics
-   Crowd monitoring
-   Custom AI solutions for specific object detection needs

Setup Instructions
------------------

1. Clone this repository:

   ```bash
   git clone https://github.com/FurqanTheGreat/CodeAlpha_Object_Detection_and_Tracking.git
   cd CodeAlpha_Object_Detection_and_Tracking
   ```

2.  Install dependencies:

    ```bash
    pip install ultralytics opencv-python
    ```

3.  Create a virtual environment: (Alternate)

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    source venv/Scripts/activate # For Bash
    pip install -r requirements.txt
    ```

4.  Run the system:

    ```bash
    python object_tracker.py
    ```

    Press 'q' to exit.

Output
------

-   Real-time annotated video streams showing detected objects with bounding boxes, confidence scores, and unique tracking IDs.
-   Optionally save the annotated video or frames for further analysis.

* * * * *
