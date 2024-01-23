from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui  # Keep pyautogui for screenshots
import pydirectinput  # Use pydirectinput for mouse/keyboard input
import time

# Load the trained model
model = YOLO(r'c:\Users\Owner\runs\detect\yolov8_rainbowsix\weights\best.pt')

# Define the region to capture (top left 1280x800)
region = {'top': 0, 'left': 0, 'width': 1280, 'height': 800}

# To ensure we only click once per character detection
character_detected = False

# Define a threshold for how close a character needs to be to the center (in pixels)
center_proximity_threshold = 100

# Delay after mouse movement (in seconds)
post_move_delay = 0.05

while True:
    # Capture a specific region of the screen using pyautogui
    screen = pyautogui.screenshot(region=(region['left'], region['top'], region['width'], region['height']))
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # Perform object detection
    results = model(frame)
    current_frame_character_detected = False

    # To aim the character in center
    screen_center_x, screen_center_y = region['width'] // 2, region['height'] // 2
    
    

    for result in results:
        if result.boxes:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                centerX, centerY = (x1 + x2) // 2, (y1 + y2) // 2

                label_id = box.cls.item()
                label = result.names[label_id]
                conf = box.conf.item()

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                if label == 'Head':
                    # Calculate distance from screen center
                    distance_to_center = np.sqrt((centerX - screen_center_x)**2 + (centerY - screen_center_y)**2)

        
                    # Print the actual location of the detected character box
                    print(f"Character Box Coordinates: Top-Left ({x1}, {y1}), Bottom-Right ({x2}, {y2})")

                    
                    # Debug: Draw a circle at the target point
                    cv2.circle(frame, (centerX, centerY), 5, (255, 0, 0), -1)

                    # Debug: Draw a line from screen center to target
                    cv2.line(frame, (screen_center_x, screen_center_y), (centerX, centerY), (255, 255, 0), 2)

                    

                    time.sleep(post_move_delay)

                    # Check if the character is close enough to the center
                    if distance_to_center <= center_proximity_threshold:
                        if not character_detected:
                            pydirectinput.mouseDown()
                            character_detected = True

                        current_frame_character_detected = True
                        break

    # Release the mouse button if no character is detected
    if character_detected and not current_frame_character_detected:
        pydirectinput.mouseUp()
        character_detected = False

    # Display the frame with predictions
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("YOLOv8 Real-Time Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
