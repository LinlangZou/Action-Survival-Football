# ⚽ Action-Survival-Football | Cross-Dimensional Interactive Soccer Game

![Unreal Engine](https://img.shields.io/badge/Unreal_Engine-5.x-black?style=for-the-badge&logo=unrealengine)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![MediaPipe](https://img.shields.io/badge/AI_Vision-MediaPipe-orange?style=for-the-badge)
![OSC](https://img.shields.io/badge/Protocol-OSC_UDP-green?style=for-the-badge)

> **"Breaking the fourth wall, reshaping game interaction with real-world gestures."** > This is a 3D physics-based action game developed using Unreal Engine 5 and AI Computer Vision. Players not only face high-speed dribbling and shooting challenges in the virtual world but also seamlessly interact with the game in the real world via a **webcam gesture (High-Five)** at the moment of victory.

---

<img width="800" height="450" alt="gif-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/7efe7214-56f9-4f48-b359-fb9c83d8e75d" />




## 🎮 Core Gameplay & Features

- **🏃‍♂️ Physics-Driven Dribbling:** Zero pre-baked animations. Built entirely on Sphere Tracing and Physical Impulse (`Add Impulse`), delivering highly realistic ball-collision mechanics and drag feedback.
- **⏱️ Time-Attack Challenge:** A dynamic, frame-rate independent HUD tracking on-screen match time (utilizing `Delta Seconds`), urging players to complete the "Dribble & Shoot" objective under pressure.
- **✋ Cross-Dimensional Reset (Core Highlight):** Upon securing victory, **players can take their hands off the keyboard/mouse and give a "High-Five" (fully open hand) to their webcam**. The AI vision engine instantly captures the hand-skeleton state, sending a packet to UE5 to seamlessly reset the level and trigger time-reversal!

*(📝 Tip: Insert a cool GIF showcasing your gameplay or waving at the camera here!)*
`![Gameplay Demo](YOUR_GIF_URL_HERE)`

---

## 🛠️ Tech Stack & Architecture

This project operates on a **"Dual-Core"** pipeline, separated into the Game Engine Front-end and the AI Vision Back-end:

### 1. Game Engine Side (UE5 Blueprints)
- **Core Logic:** Developed purely using Blueprints, leveraging Singleton/Manager patterns to handle global UI and game states.
- **UI Management:** Variable-based `WBP_GameHUD` management for dynamic destruction and reconstruction upon winning or restarting.
- **Communication Interface:** Integrates the UE5 OSC plugin, listening to the local `0.0.0.0:8050` port to receive commands from the Python script with zero delay.

### 2. AI Vision Side (Python)
- **Framework:** `Python 3.11` + `OpenCV` + `MediaPipe` (v0.10.9 classic offline build).
- **Gesture Recognition:** Extracts 21 hand-skeleton landmarks, calculating the distance ratio between fingertips and the palm center to filter out mistriggers and accurately detect an open "High-Five" posture.
- **Ultra-low Latency Network:** Uses `python-osc` to stream `/gesture/highfive` signals targeted directly at UE5 via UDP protocol.

---

## 🚀 Getting Started

Follow these instructions to set up and play the game on your local machine:

### Prerequisites
1. Ensure **Unreal Engine 5** is installed.
2. A working **HD Webcam** connected to your PC.
3. Python environment set up with required vision dependencies:
   ```bash
   pip install -r requirements.txt
  Execution Steps
Fire up the Vision Engine: Run the Python script (or double-click the packaged AI .exe file). Your webcam indicator light should turn on.

Launch the Game: Open the UE5 project file (.uproject) and hit Play (PIE).

Enjoy: Kick the ball into the designated goal zone, then raise your hand and high-five your camera to replay!
