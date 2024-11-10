#!/usr/bin/python3


# ARGUMENT 1 : PERMALINK OF POST
# ARGUMENT 2 : FILEPATH OF WOULD-BE SCREENSHOT PNG
# ARGUMENT 3 : INDEX OF SCREENSHOT TARGET (AS STRING)
#    1 -> SUBREDDIT PAGE POST
#    2 -> POST PAGE REPLY


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from PIL import Image
from io import BytesIO
import sys, time

#options
options = Options()
options.add_argument("--headless")

#vars
plink = sys.argv[1]
png_fp = sys.argv[2]
screenshot_target_index = sys.argv[3]
url = "https://www.reddit.com" + plink

#argument 3 string
match screenshot_target_index:
    case "1":
        elem_xpath = "//shreddit-post[@permalink='" + plink + "']"
    case "2":
        elem_xpath = "//shreddit-comment[@permalink='" + plink + "']"
    case _:
        print("!!! INVALID THIRD ARGUMENT PASSED TO screenshotter.py")

#open url
driver = webdriver.Firefox(options=options)
driver.get(url)
driver.maximize_window()

#zoom out to avoid google log-in popup
driver.execute_script("document.body.style.zoom='90%'")

#take screenshot
elem = driver.find_element(By.XPATH, elem_xpath)
scr_bytes = elem.screenshot_as_png
image = Image.open(BytesIO(scr_bytes))
image.save(png_fp)

#close browser
driver.quit()
