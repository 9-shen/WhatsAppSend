import pywhatkit as kit
import pandas as pd
import pyautogui
import time
''' PS: Must The Contacts Are Already in WhatsApp Contact List '''
# Read the CSV file containing names and phone numbers, making sure numbers are strings
contacts = pd.read_csv('Contacts/contacts.csv', dtype={'number': str})

# Read the message from a text file
with open('Messages/message.txt', 'r', encoding='utf-8') as file:
    message_template = file.read()

# Time to wait between sending messages (in seconds)
delay_between_messages = 10  # Adjust this delay as needed

# Send the first message to initialize the WhatsApp Web session
for index, contact in contacts.iterrows():
    name = contact['name']
    number = contact['number']
    message = message_template.format(name=name)

    # Check if the number starts with a '+' sign, if not, add it
    if not number.startswith('+'):
        number = f'+{number}'

    message = message_template.format(name=name)

    try:
        if index == 0:
            # Open WhatsApp Web and send the first message
            kit.sendwhatmsg_instantly(number, message, wait_time=20, tab_close=False, close_time=2)
            time.sleep(10)  # Wait for the page to load and message to send
        else:
            # Click on the chat search bar (assuming the browser window is active and in focus)
            pyautogui.click(380, 310)  # Adjust this to the location of the search bar
            pyautogui.write(number)  # Type the number
            time.sleep(2) # Wait For 2s after typing the number
            pyautogui.press('enter')  # Press enter to open the chat
            time.sleep(5)  # Wait for the chat to open

            # Write the message
            pyautogui.write(message)
            time.sleep(2) # Wait 2s before send
            pyautogui.press('enter')  # Press enter to send the message
            time.sleep(1) # Wait 1s before Clear the search bar

            # Clear the search bar
            pyautogui.click(380, 310)  # Click on the search bar again
            time.sleep(2)  # Wait briefly to ensure the click registers
            pyautogui.hotkey('ctrl', 'a')  # Select all text in the search bar
            time.sleep(1) # Wait 1s before hit delete button
            pyautogui.press('backspace')  # Delete the selected text

        # Wait before sending the next message
        time.sleep(delay_between_messages)
    except Exception as e:
        print(f"Failed to send message to {name} ({number}). Error: {e}")

print("Messages sent successfully!")
