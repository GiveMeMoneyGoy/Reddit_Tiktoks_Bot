import os, sys, time, random, pyautogui
import pyautogui, py_auto



#vars
images_fp = "/home/aryan/Documents/reddit_bot_mk1/uploader_module/images"
final_products_fp = "/home/aryan/Documents/reddit_bot_mk1/final_products"
tiktok_fullscreen_profile_icon_pos = (1875, 183)



#functions

#function that logs into tiktok via google account; starting from tiktok homepage while logged out
def tiktok_google_login(email, password):
    
    #sanity check if logged out and on home page by checking if able to find "Log In" button
    login_btn = py_auto.find_img(images_fp + "/tiktok_login/tiktok_login_button.png", 10)
    if (login_btn[0] == True): pass
    else: sys.exit("!!! Unable to confirm that we are logged out @ tiktok_google_login() @ main.py @ /uploader_module/")

    #click "Log In" button on tiktok home page
    first_login = py_auto.find_img(images_fp + "/tiktok_login/tiktok_login_button.png", 3)
    n_secs, n_jits = random.uniform(1, 1.5), random.randrange(1, 3)
    if (first_login[0] != False): py_auto.nav_pos(first_login[1], first_login[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()

    #click "Continue with Google" button in tiktok login prompt
    cont_with_g = py_auto.find_img(images_fp + "/tiktok_login/tiktok_login_continue_with_google.png", 1)
    n_secs, n_jits = random.uniform(1, 1.5), random.randrange(0, 3)
    if (cont_with_g[0] != False): py_auto.nav_pos(cont_with_g[1], cont_with_g[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()

    #move mouse out of the way to not interfere with google login prompt
    n_secs, n_jits = random.uniform(0.35, 0.65), random.randrange(0, 3)
    py_auto.nav_pos(random.randrange(200, 500), random.randrange(200, 800), n_secs, n_jitters = n_jits, tpos_rand = 100)

    #click on "use other account" button in google login prompt and wait to load
    try: use_other_acc = py_auto.find_img(images_fp + "/tiktok_login/google_login_use_another_account_dark.png", 2.5)
    except Exception as err: 
        if (Exception == pyautogui.ImageNotFoundException):
            try:
                use_other_acc = py_auto.find_img(images_fp + "/tiktok_login/google_login_use_another_account_light.png", 2.5)
            except: raise Exception ("!!! could not locate \"use another account\" button in google login prompt")
        else: raise Exception ("!!! could not locate \"use another account\" button in google login prompt")
    n_secs, n_jits = random.uniform(0.73, 0.98), random.randrange(0, 3)
    if (use_other_acc[0] != False): py_auto.nav_pos(use_other_acc[1], use_other_acc[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()
    time.sleep(random.uniform(1.95, 2.15))

    #type in google account email and submit and wait to load
    py_auto.human_type(email, 0.05, variance = 0.05)
    pyautogui.press("enter")
    time.sleep(random.uniform(2.5, 2.95))

    #type in google account email and submit and wait to load
    py_auto.human_type(password, 0.05, variance = 0.05)
    pyautogui.press("enter")

    #click on "forward" button in google login prompt and wait to load
    goog_login_forward = py_auto.find_img(images_fp + "/tiktok_login/google_login_forward_button.png", 6)
    n_secs, n_jits = random.uniform(0.58, 0.71), random.randrange(0, 2)
    if (goog_login_forward[0] != False): py_auto.nav_pos(goog_login_forward[1], goog_login_forward[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()
    time.sleep(random.uniform(2.0, 2.95))



#function that logs out of tiktok account; starting from tiktok homepage while logged in
def tiktok_logout():

    #sanity check if logged in and on home page by checking if able to find "Upload" button
    upload_btn = py_auto.find_img(images_fp + "/tiktok_logout/tiktok_homepage_upload_button.png", 10)
    if (upload_btn[0] == True): pass
    else: sys.exit("!!! Unable to confirm that we are logged in @ tiktok_logout() @ main.py @ /uploader_module/")

    #wait a bit
    time.sleep(random.uniform(0.42, 1.26))

    #move to usual pixel coordinates of profile icon and wait to load drop-down menu
    n_secs, n_jits = random.uniform(0.6, 1.9), random.randrange(0, 3)
    py_auto.nav_pos(tiktok_fullscreen_profile_icon_pos[0], tiktok_fullscreen_profile_icon_pos[1], n_secs, n_jitters = n_jits, tpos_rand = 3)
    time.sleep(random.uniform(0.2, 0.4))

    #click on "Log out" button in drop down menu
    f_log_out_btn = py_auto.find_img(images_fp + "/tiktok_logout/first_log_out_button.png", 5)
    n_secs, n_jitts = random.uniform(0.45, 0.75), random.randrange(0, 3)
    if (f_log_out_btn[0] != False): py_auto.nav_pos(f_log_out_btn[1], f_log_out_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 2)
    pyautogui.click()

    #if a second "Log out" button needs to be clicked, do so
    s_log_out_btn = py_auto.find_img(images_fp + "/tiktok_logout/second_log_out_button.png", 2)
    n_secs, n_jitts = random.uniform(0.45, 0.75), random.randrange(0, 2)
    if (s_log_out_btn[0] != False): py_auto.nav_pos(s_log_out_btn[1], s_log_out_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 4)
    pyautogui.click()



#function that navigates to tiktok studio upload page; starting from tiktok homepage while logged in
def tiktok_home_page_nav_to_studio():

    #sanity check if logged in and on home page by checking if able to find "Upload" button
    upload_btn = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_homepage_upload_button.png", 10)
    if (upload_btn[0] == True): pass
    else: sys.exit("!!! Unable to confirm that we are logged in @ tiktok_upload_video() @ main.py @ /uploader_module/")

    #click on "Upload" button in tiktok homepage
    n_secs, n_jits = random.uniform(0.5, 0.9), random.randrange(0, 3)
    if (upload_btn[0] != False): py_auto.nav_pos(upload_btn[1], upload_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 7)
    pyautogui.click()



#function that navigates to tiktok home page; starting from tiktok studio page 
def tiktok_studio_nav_to_home_page():

    #sanity check if in tiktok studio page by checking if able to find "Back to Tiktok" button
    back_btn = py_auto.find_img(images_fp + "/tiktok_return_home_page/back_to_tiktok_button.png", 10)
    if (back_btn[0] == True): pass
    else: sys.exit("!!! Unable to confirm that we are logged in @ tiktok_upload_video() @ main.py @ /uploader_module/")
       
    #click on "Back to Tiktok" button in tiktok studio page
    n_secs, n_jits = random.uniform(0.5, 0.9), random.randrange(0, 2)
    if (back_btn[0] != False): py_auto.nav_pos(back_btn[1], back_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 2)
    pyautogui.click()

    #click on "Leave page" in confirmation popup
    conf_popup = py_auto.find_img(images_fp + "/tiktok_return_home_page/leave_page_button.png", 3)
    n_secs, n_jits = random.uniform(0.5, 0.9), random.randrange(0, 2)
    if (conf_popup[0] != False): py_auto.nav_pos(conf_popup[1], conf_popup[2], n_secs, n_jitters = n_jits, tpos_rand = 5)
    pyautogui.click()

        

#function that uploads video on tiktok; starting from tiktok studio upload page
def tiktok_upload_video(video_to_upload_dir_name, vid_dir_parent_dir_name, vid_description_str):

    #sanity check if we are in Tiktok Studio page by checking if able to find Tiktok Studio logo
    tiktok_studio_logo = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_studio_logo.png", 10)
    if (tiktok_studio_logo[0] == True): pass
    else: sys.exit("!!! Unable to confirm that we are in Tiktok Studio page @ tiktok_upload_video() @ main.py @ /uploader_module/")

    #click on "Select video" button in Tiktok Studio
    select_vid_btn = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_studio_select_video_button.png", 10)
    n_secs, n_jits = random.uniform(1.02, 1.57), random.randrange(0, 3)
    if (select_vid_btn[0] != False): py_auto.nav_pos(select_vid_btn[1], select_vid_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()

    #sanity check if file manager has opened by checking if able to find "Documents" button
    tiktok_studio_logo = py_auto.find_img(images_fp + "/file_nav/documents_btn.png", 10)
    if (tiktok_studio_logo[0] == True): pass
    else: sys.exit("!!! Unable to confirm that file manager has opened  @ tiktok_upload_video() @ main.py @ /uploader_module/")

    #click on "Documents" button in file manager and wait to load
    f_docs_btn = py_auto.find_img(images_fp + "/file_nav/documents_btn.png", 1)
    n_secs, n_jits = random.uniform(0.79, 1.12), random.randrange(0, 2)
    if (f_docs_btn[0] != False): py_auto.nav_pos(f_docs_btn[1], f_docs_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 8)
    pyautogui.click()

    #navigate to directory which contains video to upload via typing and select vid.mp4
    time.sleep(random.uniform(0.50, 0.55))

    py_auto.human_type("reddit_bot_mk1", 0.17, 0.04)
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.press("enter")
    time.sleep(random.uniform(0.80, 0.85))

    pyautogui.write("final_products", interval = 0.20)
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.press("enter")
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.write(vid_dir_parent_dir_name, interval = 0.25)
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.press("enter")
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.write(video_to_upload_dir_name, interval = 0.30)
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.press("enter")
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.press("enter")
    time.sleep(random.uniform(0.40, 0.45))
        
    #sanity check if video has uploaded to tiktok servers by checking if able to find "Video uploaded" text on studio page
    vid_uploaded_text = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_video_uploaded_text.png", 60)
    if (vid_uploaded_text[0] == True): pass
    else: sys.exit("!!! Unable to confirm that video has fully uploaded to tiktok servers @ tiktok_upload_video() @ main.py @ /uploader_module/")

    #click on text field under Description
    vid_desc_text = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_video_description_text.png", 1)
    n_secs, n_jits = random.uniform(0.68, 1.25), random.randrange(0, 2)
    if (vid_desc_text[0] != False): py_auto.nav_pos(vid_desc_text[1] + random.randrange(0, 201), vid_desc_text[2] + random.randrange(55, 75), n_secs, n_jitters = n_jits, tpos_rand = 8)
    pyautogui.click()
    time.sleep(random.uniform(0.30, 0.35))

    #delete previous text and input description
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyDown("a")
    pyautogui.press("backspace")
    pyautogui.keyUp("a")
    pyautogui.keyUp("ctrlleft")
    py_auto.human_type(vid_description_str, 0.01, 0.01)
    time.sleep(random.uniform(0.30, 0.35))

    #move mouse out of the way to not interfere with google login prompt
    n_secs, n_jits = random.uniform(0.35, 0.65), random.randrange(0, 3)
    py_auto.nav_pos(random.randrange(300, 400), random.randrange(200, 800), n_secs, n_jitters = n_jits, tpos_rand = 100)

    #scroll down
    pyautogui.scroll(-10)

    #click on "Post" button in tiktok upload page
    post_btn = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_post_button.png", 5)
    n_secs, n_jits = random.uniform(0.9, 1.4), random.randrange(0, 2)
    if (post_btn[0] != False): py_auto.nav_pos(post_btn[1], post_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()

    #check if scrolling and clicking "Post" was successful, retry if not, 10 attempts max before quitting
    n_attempts = 0
    while (n_attempts <= 10):

        try: 
            py_auto.find_img(images_fp + "/tiktok_upload/tiktok_manage_posts_button.png", 5, serious = True)
            break

        except:

            if (n_attempts <= 10):

                #update n attempts
                n_attempts += 1

                #scroll down
                pyautogui.scroll(-10)

                #click on "Post" button in tiktok upload page
                post_btn = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_post_button.png", 5)
                n_secs, n_jits = random.uniform(0.9, 1.4), random.randrange(0, 2)
                if (post_btn[0] != False): py_auto.nav_pos(post_btn[1], post_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
                pyautogui.click()

            else: raise Exception("!!! CANNOT POST TO TIKTOK EVEN AFTER 10 ATTEMPTS")

    #click on "Manage posts" button in tiktok "Your video has been uploaded" upload popup
    man_posts_btn = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_manage_posts_button.png", 5)
    n_secs, n_jits = random.uniform(0.65, 1.05), random.randrange(0, 2)
    if (man_posts_btn[0] != False): py_auto.nav_pos(man_posts_btn[1], man_posts_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()

    #click on "Upload" button in tiktok studio main page
    upload_btn = py_auto.find_img(images_fp + "/tiktok_upload/tiktok_studio_upload_button.png", 3)
    n_secs, n_jits = random.uniform(0.65, 1.05), random.randrange(0, 2)
    if (upload_btn[0] != False): py_auto.nav_pos(upload_btn[1], upload_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 10)
    pyautogui.click()
