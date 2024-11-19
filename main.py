import cv2
from src.gesture_recognition import GestureRecognition
from src.media_control import MediaControl
from src.video_capture import VideoCapture

def main():
    video_capture = VideoCapture()
    gesture_recognition = GestureRecognition()
    media_control = MediaControl()

    while True:
        frame = video_capture.capture_frame()
        if frame is None:
            break

        # Convert frame to RGB for MediaPipe processing
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = gesture_recognition.hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                gesture = gesture_recognition.detect_gesture(hand_landmarks)
                media_control.perform_action(gesture)
                
                # Optional: Draw landmarks on the frame
                gesture_recognition.mp_drawing.draw_landmarks(frame, hand_landmarks, gesture_recognition.mp_hands.HAND_CONNECTIONS)

        # Display the frame with optional landmarks
        cv2.imshow('Hand Gesture Control', frame)
        
        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture resources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


# import time
# import cv2
# import pyautogui
# import mediapipe as mp

# class GestureRecognition:
#     def __init__(self):
#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands()
#         self.mp_drawing = mp.solutions.drawing_utils
#         self.hold_start_time = None
#         self.hold_duration_threshold = 2.0  # seconds to consider it a hold for pause

#     def detect_gesture(self, hand_landmarks):
#         thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
#         index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
#         middle_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
#         ring_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP]
#         pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]

#         # Gesture: Thumbs Up
#         if thumb_tip.y < index_tip.y and index_tip.y < middle_tip.y:
#             return 'thumbs_up'

#         # Gesture: Swipe Left
#         elif thumb_tip.x < index_tip.x:
#             return 'swipe_left'

#         # Gesture: Swipe Right
#         elif thumb_tip.x > index_tip.x:
#             return 'swipe_right'

#         # Gesture: Five (all fingers extended)
#         if (index_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y and
#             middle_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y and
#             ring_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y and
#             pinky_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y):
#             return 'five'

#         # Gesture: Hold for Pause
#         if self.is_hand_stationary(hand_landmarks):
#             if self.hold_start_time is None:
#                 self.hold_start_time = time.time()
#             elif time.time() - self.hold_start_time >= self.hold_duration_threshold:
#                 return 'hold_for_pause'
#         else:
#             self.hold_start_time = None

#         return 'unknown'

#     def is_hand_stationary(self, hand_landmarks):
#         # Placeholder for actual stationary hand detection logic
#         # For simplicity, let's assume we check if the landmarks aren't moving much
#         wrist = hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST]
#         wrist_x = wrist.x
#         wrist_y = wrist.y
#         # You should store previous wrist positions and check movement
#         return True  # Placeholder, adjust this according to your actual logic

# class MediaControl:
#     def perform_action(self, gesture):
#         if gesture == 'thumbs_up':
#             pyautogui.press('play')
#         elif gesture == 'swipe_left':
#             pyautogui.hotkey('ctrl', 'left')
#         elif gesture == 'swipe_right':
#             pyautogui.hotkey('ctrl', 'right')
#         elif gesture == 'five':
#             pyautogui.press('space')  # Pause/Play media with the spacebar
#         elif gesture == 'hold_for_pause':
#             pyautogui.press('pause')  # Use the pause key for a longer pause

# class VideoCapture:
#     def __init__(self):
#         self.cap = cv2.VideoCapture(0)

#     def capture_frame(self):
#         ret, frame = self.cap.read()
#         if not ret:
#             return None
#         return frame

#     def release(self):
#         self.cap.release()
#         cv2.destroyAllWindows()

# def main():
#     video_capture = VideoCapture()
#     gesture_recognition = GestureRecognition()
#     media_control = MediaControl()

#     while True:
#         frame = video_capture.capture_frame()
#         if frame is None:
#             break

#         # Convert frame to RGB for MediaPipe processing
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = gesture_recognition.hands.process(frame_rgb)

#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 gesture = gesture_recognition.detect_gesture(hand_landmarks)
#                 media_control.perform_action(gesture)

#                 # Optional: Draw landmarks on the frame
#                 gesture_recognition.mp_drawing.draw_landmarks(frame, hand_landmarks, gesture_recognition.mp_hands.HAND_CONNECTIONS)

#         # Display the frame with optional landmarks
#         cv2.imshow('Hand Gesture Control', frame)

#         # Exit loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release video capture resources
#     video_capture.release()

# if __name__ == "__main__":
#     main()


# import cv2
# import mediapipe as mp
# from src.gesture_recognition import recognize_gestures
# from src.media_control import execute_gesture_command

# def main():
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands()
#     mp_drawing = mp.solutions.drawing_utils

#     cap = cv2.VideoCapture(0)
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             break
        
#         frame = cv2.flip(frame, 1)
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(rgb_frame)
        
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#                 landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
#                 gesture = recognize_gestures(landmarks)
#                 execute_gesture_command(gesture)
#                 cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
#         cv2.imshow('Hand Gesture Control', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
