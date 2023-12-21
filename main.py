from browser import BrowserController

BROWSER_NAME = "Brave Browser" # TODO take as arg
KEYWORD_URL = "https://washingtonpost.com/games/keyword"

# Find PID for browser
browser = BrowserController()
browser.findBrowserProcess(BROWSER_NAME)

# Navigate to https://www.washingtonpost.com/games/keyword/
browser.navigateToURL(KEYWORD_URL)

# TODO Detect and dismiss popups
browser.startGame()

# TODO Detect letters and coordinates

# TODO solve keyword

# TODO Input letters and account for possibility of multiple solutions

# TODO save recorded footage