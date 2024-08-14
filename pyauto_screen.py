import pyautogui
import time

# Instructions for the user
print("Move the mouse to the desired location on the screen and click to capture the position.")

# Wait for a few seconds to allow the user to move the mouse
time.sleep(2)

# Function to capture the mouse position on click
def get_position_on_click():
    print("Ready to capture the position. Click anywhere to capture.")
    while True:
        if pyautogui.mouseInfo().split(', ')[1] == 'down':  # Check if the left mouse button is clicked
            x, y = pyautogui.position()
            print(f"Mouse position captured: ({x}, {y})")
            break

# Call the function to capture the mouse position
get_position_on_click()
