import psutil
import time
from keyboard import Keyboard
import pyautogui

class BrowserController:
    def __init__(self) -> None:
        self.keyboard = Keyboard()

    def navigateToURL(self, url):
        # Open a new incognito tab so we can get a fresh game
        self.keyboard.KeyDown('n', True, True, self.pid)
        # Wait for tab to open
        time.sleep(0.1)
        # Input URL
        self.keyboard.Type(url, self.pid)
        # Hit return        
        self.keyboard.Type('\n', self.pid)
        
    def findBrowserProcess(self, browserName):
        for proc in psutil.process_iter():
            proc_name = proc.name()
            if (proc_name == browserName):
                self.pid = proc.pid
                break

        print("Found browser process: %d" % self.pid)

    def waitForButtonAndClick(self, button_image):
        isLookingForButton = True

        button_x = None
        button_y = None

        while (isLookingForButton):
            try:
                button_x, button_y = pyautogui.locateCenterOnScreen(button_image)

                print("Found play button at %d, %d" % (button_x, button_y))
                isLookingForButton = False
            except pyautogui.ImageNotFoundException:
                print('%s. Will try again...' % button_image)
                time.sleep(0.25)
        
        pyautogui.moveTo(button_x // 2, button_y // 2, duration=0.25, tween=pyautogui.easeInOutQuad)
        pyautogui.click()

    def startGame(self):
        self.waitForButtonAndClick('assets/play-button.png')

        self.waitForButtonAndClick('assets/news-you-want-x.png')

        self.waitForButtonAndClick('assets/how-to-play-x.png')

        # move mouse of the way for CV to detect pieces
        pyautogui.moveTo(50, 50)
