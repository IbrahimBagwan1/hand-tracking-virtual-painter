# Hand Tracking Virtual Painter 🎨✋

> ⭐ If you find this project useful, please consider giving it a star!

A real-time **AI-based virtual painting app** using **hand tracking** and **gesture recognition**. Draw on your screen with just your **hand and a webcam**—no mouse or stylus required!

---

## 🖼️ Demo

![Demo Screenshot](demo-screenshot.png)

*Add a short video or GIF for a better showcase!*

---

## 🚀 Features

- ✋ Real-time hand tracking
- 🖌️ Draw using finger movement
- 🧠 AI-powered gesture recognition
- 🎨 Select colors with gestures
- 🧼 Eraser mode
- 📷 Works with any webcam

---

## 🧰 Technologies Used

- Python 🐍
- OpenCV
- MediaPipe
- NumPy

---

## 📦 Installation

```bash
git clone https://github.com/IbrahimBagwan1/hand-tracking-virtual-painter.git
cd hand-tracking-virtual-painter
pip install -r requirements.txt
```

---

## ▶️ Usage

Make sure your webcam is connected, then run:

```bash
python painter.py
```

---

## 🎯 How It Works

- Uses MediaPipe to track hand landmarks in real time.
- Detects finger gestures for:
  - **Drawing:** Index finger up
  - **Color selection:** Index + middle finger up
  - **Erasing:** Thumb + pinky gestures
- Tracks finger movement and paints on a virtual canvas.

---

## 🖼️ Screenshots

| Drawing | Color Selector | Erasing |
| ------- | ------------- | ------- |
| ![](screenshots/drawing.png) | ![](screenshots/color-selector.png) | ![](screenshots/erasing.png) |

*Add your own screenshots to the `screenshots/` folder!*

---

## 📚 Topics

`ai` • `opencv` • `mediapipe` • `hand-tracking` • `gesture-recognition` • `virtual-painter` • `python` • `drawing-app` • `real-time`

---

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---