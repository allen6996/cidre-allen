import cv2
import numpy as np

# --- CONFIGURATION ---
# Path to the pre-trained Haar Cascade XML files
# NOTE: We keep the face cascade to define a rough ROI, but will NOT draw its box.
FACE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
EYE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_eye.xml'

T_ZONE_COLOR = (255, 255, 255)  # BGR: WHITE
LINE_THICKNESS = 5
CIRCLE_RADIUS = 5

# Initialize OpenCV's Cascade Classifiers
face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
eye_cascade = cv2.CascadeClassifier(EYE_CASCADE_PATH)

if face_cascade.empty() or eye_cascade.empty():
    raise IOError("Could not load Haar cascade files. Check paths.")

# Initialize webcam
cap = cv2.VideoCapture(0)

print("[INFO] Starting video stream for T-Zone features...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 1. Detect faces (Used ONLY to define the main area, box is NOT drawn)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Define the face ROI for feature detection
        roi_gray = gray[y:y + h, x:x + w]
        
        # --- T-ZONE FEATURE DETECTION ---
        
        # 2. Detect eyes within the top half of the face ROI (Horizontal Bar)
        # We limit the search area to the top 50% of the detected face box.
        eyes = eye_cascade.detectMultiScale(
            roi_gray[:h // 2, :], 
            scaleFactor=1.1, 
            minNeighbors=10
        )
        
        eye_centers = []
        for (ex, ey, ew, eh) in eyes:
            # Calculate global coordinates for the eye center
            eye_center_x = x + ex + ew // 2
            eye_center_y = y + ey + eh // 2
            eye_centers.append((eye_center_x, eye_center_y))
            
            # Draw circles on the detected eye centers (T-Zone recognition dots)
            cv2.circle(frame, (eye_center_x, eye_center_y), CIRCLE_RADIUS, T_ZONE_COLOR, -1)

        # 3. Draw T-Zone Contour Approximation
        
        # A. Horizontal Bar (Connect the two most likely eye centers)
        if len(eye_centers) >= 2:
            # Sort eyes by X-coordinate
            eye_centers.sort(key=lambda p: p[0])
            pt1 = eye_centers[0]
            pt2 = eye_centers[-1] # Use the leftmost and rightmost detected eyes
            
            # Draw the line connecting the eyes (Forehead/Eyebrow approximation)
            cv2.line(frame, pt1, pt2, T_ZONE_COLOR, LINE_THICKNESS)
            
            # B. Vertical Bar (Nose Bridge approximation)
            # Start: Midpoint of the horizontal line
            nose_start_x = (pt1[0] + pt2[0]) // 2
            nose_start_y = pt1[1] 
            
            # End: Center of the estimated nose area (approx 65% down the face)
            nose_end_x = x + w // 2
            nose_end_y = y + int(h * 0.65)
            
            cv2.line(frame, (nose_start_x, nose_start_y), (nose_end_x, nose_end_y), T_ZONE_COLOR, LINE_THICKNESS)
            

    # Display the resulting frame
    # NOTE: The only drawn elements are the T-Zone lines and dots.
    cv2.imshow("T-Zone Detection (OpenCV Only)", frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()