import time
import random
import pyautogui
import keyboard
import sys
import threading
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class AntiAFK:
    """
    Simulates anti-AFK activity by moving the mouse and optionally simulating
    a key press to prevent the system from going idle.
    
    Attributes:
        run_duration (int): Total time in seconds to run the simulation.
        interval (int): Seconds between each activity cycle.
        move_range (int): Maximum distance (in pixels) to randomly move the mouse.
        key_press (bool): Whether to simulate a Shift key press each cycle.
    """
    
    def __init__(self, run_duration=60, interval=15, log_actions=False, move_range=20, key_press=True):
        """
        Initializes the AntiAFK instance.
        
        :param run_duration: Total time in minutes to keep active (converted to seconds).
        :param interval: Seconds between each activity cycle.
        :param move_range: Maximum pixel offset for random mouse movement.
        :param key_press: Whether to simulate a Shift key press.
        """
        self.run_duration = run_duration * 60  # Convert minutes to seconds
        self.interval = interval
        self.log_actions = log_actions
        self.move_range = move_range
        self.key_press = key_press
        self._stop_event = threading.Event()

    def _move_mouse(self):
        """
        Moves the mouse to a new position by applying a random offset.
        """
        try:
            x, y = pyautogui.position()
            offset_x = random.randint(-self.move_range, self.move_range)
            offset_y = random.randint(-self.move_range, self.move_range)
            pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.25)
            if self.log_actions:
                logger.info(f"Moved mouse to: ({x + offset_x}, {y + offset_y})")
        except Exception as e:
            logger.exception("Error moving mouse: %s", e)

    def _simulate_key_press(self):
        """
        Simulates a Shift key press if enabled.
        """
        if self.key_press:
            try:
                pyautogui.press("shift")
                if self.log_actions:
                    logger.info("Simulated Shift key press.")
            except Exception as e:
                logger.exception("Error simulating key press: %s", e)

    def _monitor_escape(self):
        """
        Runs in a background thread and waits for the ESC key.
        When ESC is pressed, it sets the stop event.
        """
        logger.info("ESC key monitor thread started. Waiting for ESC key...")
        keyboard.wait('esc')
        logger.info("ESC key detected. Stopping simulation.")
        self._stop_event.set()

    def _run_cycle(self):
        """
        Executes one activity cycle: moves the mouse, simulates key press, and
        then waits for the interval period while checking for the stop event.
        """
        if self._stop_event.is_set():
            return False

        self._move_mouse()
        self._simulate_key_press()

        # Instead of a single long sleep, wait with timeout to check for exit
        if self._stop_event.wait(timeout=self.interval):
            return False
        return True

    def run(self):
        """
        Runs the anti-AFK simulation until the specified run duration elapses
        or until the ESC key is pressed.
        """
        logger.info("Starting AntiAFK simulation for %d seconds. Press ESC to exit.", self.run_duration)
        
        # Start a background thread to monitor the ESC key.
        monitor_thread = threading.Thread(target=self._monitor_escape, daemon=True)
        monitor_thread.start()
        
        start_time = time.time()
        end_time = start_time + self.run_duration

        try:
            while time.time() < end_time:
                if not self._run_cycle():
                    break
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received. Exiting simulation.")
        finally:
            logger.info("AntiAFK simulation finished or stopped.")
