import psutil
import time
import pyautogui
import pygetwindow as gw

from keyboard import Keyboard

class BrowserController:
    def __init__(self) -> None:
        self.keyboard = Keyboard()

    def navigateToURL(self, url):
        # Open a new incognito tab so we can get a fresh game
        self.keyboard.KeyDown('n', True, True, self.pid)
        # Wait for tab to open
        time.sleep(0.5)
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

    def detectWordsForGame(self):
        # get active window title
        window_title = gw.getActiveWindow()
        # get window dimensions
        dimensions = gw.getWindowGeometry(window_title)
        dimensions = tuple(int(x) for x in dimensions)

        # grab a screenshot
        img = pyautogui.screenshot(region=dimensions)
        img.show()

    def waitForButtonAndClick(self, button_image, max_attempts=-1):
        isLookingForButton = True

        button_x = None
        button_y = None

        num_attempts = 0

        while (isLookingForButton):
            try:
                num_attempts += 1
                
                button_x, button_y = pyautogui.locateCenterOnScreen(button_image)

                print("Found play button at %d, %d" % (button_x, button_y))
                isLookingForButton = False
            except pyautogui.ImageNotFoundException:
                if (max_attempts > 0) and (num_attempts >= max_attempts):
                    print("%d Couldn't find %s. Giving up!" % (num_attempts, button_image))
                else:
                    print("%d Couldn't find %s. Will try again..." % (num_attempts, button_image))

                    time.sleep(0.25)
        
        if not isLookingForButton:
            pyautogui.moveTo(button_x // 2, button_y // 2, duration=0.25, tween=pyautogui.easeInOutQuad)
            pyautogui.click()

    def startGame(self):
        # click play button to start
        self.waitForButtonAndClick('assets/play-button.png')
        # dismiss marketing popup
        self.waitForButtonAndClick('assets/news-you-want-x.png', 10)
        # dismiss how to play popup
        self.waitForButtonAndClick('assets/how-to-play-x.png')
        # move mouse of the way for CV to detect pieces
        pyautogui.moveTo(50, 50, duration=0.25)
