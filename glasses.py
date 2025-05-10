import cv2
import pytesseract
import torch
import pyttsx3
import RPi.GPIO as GPIO     
import time
from datetime import datetime

# === GPIO Setup ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Object mode
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Text mode
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Push button

# === Camera Setup ===
cap = cv2.VideoCapture(0)

# === TTS Engine Setup ===
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# === Model Load ===
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# === Startup Message ===
speak("Ready to take commands")

# === Mode Check ===
def get_mode():
    if GPIO.input(17) == GPIO.LOW:
        return "object"
    elif GPIO.input(27) == GPIO.LOW:
        return "text"
    else:
        return None

mode = get_mode()

if mode == "object":
    speak("Object detection is ready")
elif mode == "text":
    speak("Hold up, I will read this text for you")

# === Main Loop ===
try:
    while True:
        button_pressed = GPIO.input(22) == GPIO.LOW
        if button_pressed:
            ret, frame = cap.read()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"image_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"[INFO] Image saved: {filename}")

            if mode == "object":
                results = model(frame)
                labels = results.names
                detections = results.pred[0]
                spoken = set()
                for *box, conf, cls in detections:
                    label = labels[int(cls)]
                    if label not in spoken:
                        speak(f"{label} detected")
                        spoken.add(label)

            elif mode == "text":
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                text = pytesseract.image_to_string(gray)
                if text.strip():
                    speak("Here is the text")
                    speak(text)
                else:
                    speak("I couldn't find any text.")

            time.sleep(2)  # prevent re-triggering immediately

        # Update mode dynamically if needed
        new_mode = get_mode()
        if new_mode != mode:
            mode = new_mode
            if mode == "object":
                speak("Switched to object detection")
            elif mode == "text":
                speak("Switched to text reading")

except KeyboardInterrupt:
    print("Shutting down")

finally:
    cap.release()
    GPIO.cleanup()
