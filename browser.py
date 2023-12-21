import psutil
import time
from keyboard import Keyboard

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