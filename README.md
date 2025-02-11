# anti-afk

**anti-afk** is a Python library that simulates user activity to prevent your system from being marked as AFK (Away From Keyboard). It works by periodically moving the mouse and optionally simulating a key press (default: Shift). This is especially useful for keeping your status active in applications like Microsoft Teams, Zoom, or any other environment that detects inactivity.

## Features

- **Simulated Mouse Movement:** Randomly moves the mouse within a specified pixel range.
- **Optional Key Press Simulation:** Simulates a Shift key press to generate extra activity.
- **Customizable Duration & Interval:** Specify how long and how frequently the simulation should run.
- **Interruptible Execution:** The simulation stops immediately if the ESC key is pressed.

## Installation

You can install **anti-afk** from PyPI using pip:

```bash
pip install anti-afk-lib
```

## Example

Below is the simple example to call the module for 10 minutes (run_duration: Run for 10 minutes).

```bash
from anti_afk.anti_afk import AntiAFK
AntiAFK(run_duration=10).run()
```

## Dependencies

This project depends on the following Python packages:

- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [keyboard](https://pypi.org/project/keyboard/)

You can install these dependencies using pip. If you have a virtual environment set up, activate it first, then run:
```bash
pip install -r requirements.txt
```
