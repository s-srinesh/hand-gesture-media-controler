# import pyautogui

# class MediaControl:
#     def perform_action(self, gesture):
#         if gesture == 'thumbs_up':
#             pyautogui.press('playpause')
#         # elif gesture == 'swipe_left':
#         #     pyautogui.hotkey('ctrl', 'left')
#         # elif gesture == 'swipe_right':
#         #     pyautogui.hotkey('ctrl', 'right')
#         elif gesture == 'five':
#             pyautogui.press('space')  # Pause/Play media with the spacebar
#         # elif gesture == 'hold_for_pause':
#         #     pyautogui.press('pause')  # Use the pause key for a longer pause


# import pyautogui

# def execute_gesture_command(gesture):
#     if gesture == "Thumb Up":
#         pyautogui.press('playpause')
#     # Add more media control commands here

# import pyautogui

# class MediaControl:
#     def perform_action(self, gesture):
#         if gesture == 'volume_up':
#             pyautogui.press('volumeup')  # Increase volume
#         elif gesture == 'volume_down':
#             pyautogui.press('volumedown')  # Decrease volume


import pyautogui

class MediaControl:
    def perform_action(self, gesture):
        if gesture == 'volume_up':
            pyautogui.press('volumeup')  # Increase volume
        elif gesture == 'volume_down':
            pyautogui.press('volumedown')  # Decrease volume
        elif gesture == 'hold_for_pause':
            pyautogui.press('pause')  # Pause media
        elif gesture == 'play_media':
            pyautogui.press('play')  # Play media
