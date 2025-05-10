#  AI-Powered Smart Glasses for the Blind

An assistive wearable device that helps visually impaired individuals detect objects and read printed text through voice feedback using a slide switch and button.
## Brief Discription Of What We Will Be Doing

###  Features

- **Dual-Mode Functionality via Slide Switch**:
  -  *Object Detection Mode*: Announces objects seen by the camera.
  -  *Text-to-Speech Mode*: Reads printed text aloud.
- **Push Button Trigger**: Image is captured **only** when the button is pressed.
- **Audio Feedback**:
  - “*Ready to take commands*” on boot.
  - Mode announcement based on switch position.
- **Offline Operation**: No internet required.
- **Lightweight and portable** for eyewear integration.

###  Hardware Components

| Component                     | Function                        |
|------------------------------|----------------------------------|
| Raspberry Pi Zero 2 W        | Main processing unit            |
| Pi Camera Module V2 (CSI)    | Vision input                    |
| USB Sound Card               | Audio output interface          |
| Wired Earbuds (3.5mm)        | Speaker for the user            |
| Push Button                  | Capture trigger                 |
| Slide Switch (2-way/DPDT)    | Toggle between modes            |
| 3.7V LiPo Battery (1200mAh)  | Power source                    |
| TP4056 Module                | Battery charging                |
| MT3608 Boost Converter       | Boost 3.7V → 5V for Pi          |

###  Hardware Wiring

| Pin / Component     | GPIO Pin       | Notes                                  |
|---------------------|----------------|----------------------------------------|
| Push Button         | GPIO 17        | Pull-down recommended (via resistor)   |
| Slide Switch        | GPIO 27        | Reads mode selection                   |
| Pi Camera           | CSI Port       | Enable in `raspi-config`               |
| USB Sound Card      | USB Port       | Used for audio output                  |
| Battery → TP4056    | Direct         | Charging module                        |
| TP4056 → MT3608     | Power In       | Boost voltage to 5V                    |
| MT3608 → Pi         | 5V & GND       | Pi power input                         |

###  Software Structure

```
ai-glasses/
├── glasses.py               # Main Python script
├── requirements.txt         # Python dependencies
├── startup.sh               # Auto-run setup script
├── images/                  # Captured image storage
├── README.md                # Project documentation
```

###  Main Software Libraries

- `OpenCV` – Camera interfacing and image processing
- `pyttsx3` – Offline text-to-speech
- `pytesseract` – OCR (Optical Character Recognition)
- `torch` + YOLOv5 – Object detection model
- `RPi.GPIO` – Handling GPIO input from switch and button

###  Setup Instructions (Short)

1. **Flash Raspberry Pi OS (Lite recommended)** on SD card.
2. Enable:
   - Camera: `sudo raspi-config` → *Interfaces* → Enable Camera
   - I2C (optional for expansion)
3. `sudo apt update && sudo apt install` the required packages.
4. Install Python libraries from `requirements.txt`.
5. Configure `glasses.py` to **auto-start** using `rc.local` or systemd.
6. Connect hardware as per the wiring guide.

# Hardware 
After the brief discription you will be able to identify, which components we are going to use.

- Raspberry Pi Zero 2 W
- Pi Camera Module V2 (CSI)
- USB Sound Card
- Wired Earbuds (3.5mm)
- Push Button
- Slide Switch (2-way/DPDT)
- 3.7V LiPo Battery (1200mAh)
- TP4056 Module
- MT3608 Boost Converter

## Wiring of the hardware components
**Power supply wiring**
1. Battery → TP4056:
   - B+ to battery red wire (positive)
   - B- to battery black wire (negative)
   
2. TP4056 → MT3608:
   - OUT+ to MT3608 IN+
   - OUT- to MT3608 IN-

3. MT3608 Output → Pi:
   - Adjust MT3608 output to 5V using a multimeter and potentiometer screw.
   - Connect OUT+ and OUT- of MT3608 to Pi's 5V and GND pins.
![Screenshot 2025-05-10 194757](https://github.com/user-attachments/assets/27bf2a02-a73c-4ad2-b77d-0cd5d63927a9)



   


