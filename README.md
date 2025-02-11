# anti-afk

Introducing a Python library **anti-afk**, designed to simulate user activity, ensuring that your system remains active and does not enter an idle state (AFK). The library periodically moves the mouse pointer and can optionally simulate a key press (defaulting to the Shift key). This functionality delivers several professional benefits:

**Enhanced Session Stability:**
Prevents unwanted session terminations in environments such as VPN connections, remote desktop sessions, and remote debugging, thereby reducing the risk of losing unsaved work.

**Operational Continuity:**
Maintains active sessions across various remote and cloud-based platforms, ensuring that time-sensitive workflows are not disrupted by automatic timeouts or logouts.

**Improved Multi-Tasking Efficiency:**
Supports scenarios where multiple customer sessions or tasks are managed concurrently, enabling uninterrupted work streams and more efficient resource allocation.

By keeping your system’s status active, this library helps safeguard against connectivity disruptions and session timeouts, contributing to a more resilient and productive operational environment.

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
