import os, sys, time, random
import pyautogui, py_auto



#vars
images_fp = "/home/aryan/Documents/reddit_bot_mk1/uploader_module/images"
final_products_fp = "/home/aryan/Documents/reddit_bot_mk1/final_products"
tiktok_fullscreen_profile_icon_pos = (1875, 183)



#functions

#function that opens firefox via bash and navigates to url
def open_tab(url):

    #open firefox via terminal
    os.system("firefox")
    time.sleep(0.5)

    #type in url and press etner
    search_bar_icon = py_auto.find_img(images_fp + "/general/firefox_search_icon.png", 5)
    if (search_bar_icon[0] != False): py_auto.nav_pos(search_bar_icon[1], search_bar_icon[2], 0)
    pyautogui.click()
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(0.5)



#function that closes current firefox tab
def close_tab():

    #click on "x" icon to close
    close_icon = py_auto.find_img(images_fp + "/general/firefox_current_tab_close_icon.png", 0.5)
    if (close_icon[0] != False): py_auto.nav_pos(close_icon[1], close_icon[2], 1, n_jitters = 2)
    pyautogui.click()
