from ultralytics import YOLO
import cv2

# Loading a pretrained YOLO model
model = YOLO("yolov8n.pt")

# Input video path
video_input_path = 0 # Replace with a video path to track objects in a video. Example: video_input_path = "video.mp4"

# Opening video file
cap = cv2.VideoCapture(video_input_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Performing object detection
    resized_frame = cv2.resize(frame, (640, 640))
    results = model.predict(source=frame, conf=0.5, save=False, verbose=False)

    # Annotate the frame with detections
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO Object Detection", annotated_frame)

    # Press q to exit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
