# SoberSense 

Simple alcohol intoxication detection system using computer vision to identify signs of impairment.

## Overview
SoberSense analyzes facial features in real-time to detect potential signs of alcohol intoxication, including red eyes and drowsiness.

## Features
- Real-time red eye detection
- Drowsiness monitoring
- Intoxication risk scoring (0-100%)
- Color-coded status alerts
- Simple and easy to use

## Tech Stack
- Python
- OpenCV
- NumPy
- Haar Cascade Classifiers

## How It Works

### Detection Methods
1. **Red Eye Detection**: Analyzes eye regions for redness
2. **Drowsiness Detection**: Monitors if both eyes are visible and open

### Scoring System
- Red eyes detected = 50 points
- Drowsiness detected = 50 points
- Total Score: 0-100%

### Risk Levels
- 0-39% (GREEN): Clear/Sober
- 40-69% (ORANGE): Moderate Risk
- 70-100% (RED): High Risk

## Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/SoberSense.git
cd SoberSense
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Ensure Haar Cascade files are present in the project folder

## Usage
```bash
python sober_sense.py
```

Press `q` to quit the application.

## Use Cases
- Vehicle Safety: Pre-drive sobriety check
- Workplace Safety: Monitor operators
- Research: Study alcohol effects
- Awareness: Educational demonstrations

## Author
ISHIKA SHUKLA
- GitHub:https://github.com/ishikashukla672

## Disclaimer
This is an educational project. It should NOT be used as the sole method for determining intoxication.
```
