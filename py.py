import serial
import time
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Set up the serial connection
ser = serial.Serial('COM4', 9600)

# Define the paths to the audio files using raw strings (with the new .wav format)
audio_files = {
    '1': r'C:\Users\momin\Downloads\Trash\a.wav',
    '2': r'C:\Users\momin\Downloads\Trash\b.wav',
    '3': r'C:\Users\momin\Downloads\Trash\c.wav',
    '4': r'C:\Users\momin\Downloads\Trash\d.wav'
}

# Store the last played number
last_received = None

# Function to play audio based on the received number
def play_audio_once(number):
    global last_received

    # Check if the current number is the same as the last played one
    if number == last_received:
        print("Same number received, no song will be played.")
        return

    # Update the last_received with the current number
    last_received = number

    if number in audio_files:
        print(f"Playing {audio_files[number]}")
        pygame.mixer.music.load(audio_files[number])  # Load the wav file
        pygame.mixer.music.play()  # Play the file
        while pygame.mixer.music.get_busy():  # Wait for the song to finish
            time.sleep(1)
        print(f"Finished playing {audio_files[number]}.")

try:
    while True:
        # Once the song is done, check for new serial data
        if ser.in_waiting > 0:  # Check if there's data waiting in the serial buffer
            data = ser.readline().decode('utf-8').strip()  # Read the entire line and strip newline characters
            print(f"Received data: {data}")

            # Ensure that the received data is one of '1', '2', '3', or '4'
            if data in ['1', '2', '3', '4']:
                play_audio_once(data)
            else:
                print("Invalid data received.")

        time.sleep(0.1)  # Small delay before checking for new input

except KeyboardInterrupt:
    print("Stopping serial read.")
finally:
    ser.close()  # Close the serial connection
