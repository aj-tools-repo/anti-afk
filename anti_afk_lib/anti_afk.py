import time
import random
import pyautogui
import keyboard

class AntiAFK:
    """
    A class that simulates anti-AFK activity by moving the mouse and optionally
    pressing a key to prevent the system from going idle.

    Attributes:
        run_duration (int): Total time in minutes to run the simulation.
        interval (int): Seconds to wait between each activity cycle.
        move_range (int): Maximum distance (in pixels) to randomly move the mouse.
        key_press (bool): Whether to simulate a Shift key press each cycle.
    """
    
    def __init__(self, run_duration=60, interval=15, log_actions=False, move_range=20, key_press=True):
        """
        Initializes the AntiAFK instance.
        
        :param run_duration: Total time in minutes to keep active.
        :param interval: Seconds between each activity cycle.
        :param move_range: Maximum pixel offset for random mouse movement.
        :param key_press: Whether to simulate a Shift key press.
        """
        self.run_duration = run_duration
        self.interval = interval
        self.log_actions = log_actions
        self.move_range = move_range
        self.key_press = key_press

    def _move_mouse(self):
        """
        Moves the mouse to a new position by applying a random offset to the current location.
        """
        x, y = pyautogui.position()
        offset_x = random.randint(-self.move_range, self.move_range)
        offset_y = random.randint(-self.move_range, self.move_range)
        pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.25)
        if self.log_actions: 
            print(f"[AntiAFK] Moved mouse to: ({x + offset_x}, {y + offset_y})")

    def _simulate_key_press(self):
        """
        Simulates a Shift key press if key_press is enabled.
        """
        if self.key_press:
            pyautogui.press("shift")
            if self.log_actions: 
                print("[AntiAFK] Simulated Shift key press.")

    def _check_exit(self):
        """
        Checks if the ESC key is pressed.
        
        :return: True if ESC is pressed, else False.
        """
        if keyboard.is_pressed("esc"):
            if self.log_actions: 
                print("[AntiAFK] ESC pressed. Exiting simulation.")
            return True
        return False

    def _run_cycle(self):
        """
        Executes one activity cycle: check for exit, move mouse, and simulate key press.
        
        :return: False if the cycle should be terminated (e.g., ESC pressed), True otherwise.
        """
        if self._check_exit():
            return False
        self._move_mouse()
        self._simulate_key_press()
        time.sleep(self.interval)
        return True

    def run(self):
        """
        Runs the anti-AFK simulation. The simulation will continue until the specified 
        run duration elapses or until the ESC key is pressed.
        """
        print(f"[AntiAFK] Running for {self.run_duration} minutes. Press ESC to exit.")
        total_seconds = self.run_duration * 60
        end_time = time.time() + total_seconds

        while time.time() < end_time:
            if not self._run_cycle():
                break

        print("[AntiAFK] Simulation finished or time is up.")
