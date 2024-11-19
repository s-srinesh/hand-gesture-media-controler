# import time
# import mediapipe as mp


# class GestureRecognition:
#     def __init__(self):
#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands()
#         self.mp_drawing = mp.solutions.drawing_utils
#         self.hold_start_time = None
#         self.hold_duration_threshold = 2.0 

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
#         threshold = 0.02
#         wrist = hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST]
#         wrist_diff = abs(wrist.x - wrist.y)

#         return wrist_diff < threshold

# # def recognize_gestures(landmarks):
# #     thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
# #     thumb_base = landmarks[mp_hands.HandLandmark.THUMB_BASE]
    
# #     if thumb_tip.y < thumb_base.y - 0.1:
# #         return "Thumb Up"
# #     # Add more gesture recognition logic here
# #     return "Unknown"


# import time
# import mediapipe as mp


# class GestureRecognition:
#     def __init__(self):
#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands()
#         self.mp_drawing = mp.solutions.drawing_utils
#         self.hold_start_time = None
#         self.hold_duration_threshold = 2.0 

#     def detect_gesture(self, hand_landmarks):
#         thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
#         index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]

#         # Gesture: Thumbs Up (thumb is above the index finger)
#         if thumb_tip.y < index_tip.y:
#             return 'volume_up'
        
#         # Gesture: Thumbs Down (thumb is below the index finger)
#         elif thumb_tip.y > index_tip.y:
#             return 'volume_down'

#         # Hold for Pause (if needed)
#         if self.is_hand_stationary(hand_landmarks):
#             if self.hold_start_time is None:
#                 self.hold_start_time = time.time()
#             elif time.time() - self.hold_start_time >= self.hold_duration_threshold:
#                 return 'hold_for_pause'
#         else:
#             self.hold_start_time = None

#         return 'unknown'

#     def is_hand_stationary(self, hand_landmarks):
#         threshold = 0.02
#         wrist = hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST]
#         wrist_diff = abs(wrist.x - wrist.y)

#         return wrist_diff < threshold

import time
import mediapipe as mp

class GestureRecognition:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils
        self.hold_start_time = None
        self.hold_duration_threshold = 2.0
        self.media_paused = False  # Track if media is paused

    def detect_gesture(self, hand_landmarks):
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]

        # Check for the "five" gesture
        if (index_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y and
            middle_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y and
            ring_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y and
            pinky_tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y):
            self.media_paused = True
            return 'hold_for_pause'  # Media should pause

        # Check for all fingers closed (to play media)
        elif (thumb_tip.y > hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y and
              index_tip.y > hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y and
              middle_tip.y > hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y and
              ring_tip.y > hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y and
              pinky_tip.y > hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y):
            if self.media_paused:
                self.media_paused = False
                return 'play_media'  # Media should play

        # Volume control gestures
        if thumb_tip.y < index_tip.y:
            return 'volume_up'
        elif thumb_tip.y > index_tip.y:
            return 'volume_down'

        return 'unknown'

    def is_hand_stationary(self, hand_landmarks):
        threshold = 0.02
        wrist = hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST]
        wrist_diff = abs(wrist.x - wrist.y)
        return wrist_diff < threshold
