"""
SoberSense - Simple Alcohol Intoxication Detector
Detects red eyes and drowsiness as signs of intoxication
Author: ishika
Date: December 2025
"""

import cv2
import numpy as np

# Load classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Thresholds
RED_THRESHOLD = 90  # How red the eyes should be
DROWSY_FRAME_COUNT = 0  # Counter for drowsy frames

print("[INFO] Starting SoberSense...")
print("[INFO] Press 'q' to quit")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    intoxication_score = 0
    
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        
        # Get face region
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]
        
        # Detect eyes in face
        eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 5)
        
        # Check for red eyes
        red_eyes = False
        for (ex, ey, ew, eh) in eyes:
            # Get eye region
            eye_region = face_color[ey:ey+eh, ex:ex+ew]
            
            # Calculate redness (Red channel - Blue channel)
            b, g, r = cv2.split(eye_region)
            redness = np.mean(r) - np.mean(b)
            
            if redness > RED_THRESHOLD:
                red_eyes = True
                cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
                cv2.putText(face_color, "RED EYE", (ex, ey-5), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            else:
                cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        # Check for drowsiness (few or no eyes detected)
        drowsy = len(eyes) < 2
        
        # Calculate simple score
        if red_eyes:
            intoxication_score += 50
        if drowsy:
            intoxication_score += 50
        
        # Display indicators
        if red_eyes:
            cv2.putText(frame, "RED EYES DETECTED", (x, y-30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
        if drowsy:
            cv2.putText(frame, "DROWSY", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    # Display intoxication score
    if intoxication_score >= 70:
        status = "HIGH RISK"
        color = (0, 0, 255)  # Red
    elif intoxication_score >= 40:
        status = "MODERATE"
        color = (0, 165, 255)  # Orange
    else:
        status = "CLEAR"
        color = (0, 255, 0)  # Green
    
    cv2.putText(frame, f"Score: {intoxication_score}%", (10, 30),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    cv2.putText(frame, f"Status: {status}", (10, 60),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    # Show frame
    cv2.imshow('SoberSense', frame)
    
 # Quit on 'q' or ESC or close window
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # 27 is ESC key
        break
    
    # Check if window was closed
    if cv2.getWindowProperty('SoberSense', cv2.WND_PROP_VISIBLE) < 1:
        break
print("[INFO] Shutting down...")
cap.release()
cv2.destroyAllWindows()
