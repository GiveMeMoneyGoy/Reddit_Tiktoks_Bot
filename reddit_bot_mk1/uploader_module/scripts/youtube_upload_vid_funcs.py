import os, sys, time, random, pyautogui
import pyautogui, py_auto



#vars
images_fp = "/home/aryan/Documents/reddit_bot_mk1/uploader_module/images"
tiktok_fullscreen_profile_icon_pos = (1875, 183)



#functions

#function that uploads video to youtube; starting from youtube studio
def youtube_upload_video(video_to_upload_dir_name, vid_dir_parent_dir_name, vid_title_str, vid_description_str):
    
    time.sleep(random.uniform(1.20, 1.45))
 
    #sanity check if we are in youtube studio
    youtube_studio_logo = py_auto.find_img(images_fp + "/youtube_upload/yt_studio_logo.png", 20)
    if (youtube_studio_logo[0] == True): pass
    else: sys.exit("!!! unable to confirm that we are in youtube studio page @ youtube_upload_video @ youtube_upload_vid.py @ /uploader_module/")

    #click on camera icon
    uvci_btn = py_auto.find_img(images_fp + "/youtube_upload/upload_videos_camera_icon.png", 30)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    py_auto.nav_pos(uvci_btn[1], uvci_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 5)
    pyautogui.click()

    #click on "Upload videos"
    upload_btn = py_auto.find_img(images_fp + "/youtube_upload/upload_videos_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 2)
    if (upload_btn[0] != False): py_auto.nav_pos(upload_btn[1], upload_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 6)
    pyautogui.click()

    #click on "Select files"
    select_files_btn = py_auto.find_img(images_fp + "/youtube_upload/select_files_btn.png", 6)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 2)
    if (select_files_btn[0] != False): py_auto.nav_pos(select_files_btn[1], select_files_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 8)
    pyautogui.click()

    #sanity check if file manager has opened by checking if able to find "Documents" button
    f_docs_btn = py_auto.find_img(images_fp + "/file_nav/documents_btn.png", 10)
    if (f_docs_btn[0] == True): pass
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

    pyautogui.write("vid.mp4")
    time.sleep(random.uniform(0.40, 0.45))

    pyautogui.press("enter")
    time.sleep(random.uniform(0.40, 0.45))

    #check if the daily upload limit has been reached. If so, return error status.
    daily_upload_limit_text = py_auto.find_img(images_fp + "/youtube_upload/daily_upload_limit_text.png", 5)
    if (daily_upload_limit_text[0] == False): pass
    else:
        print("!!! daily limit for uploading to youtube reached!")
        return 1

    #sanity check if video has uploaded to youtube servers by checking if able to find "Title (required)" on upload prompt
    title_text = py_auto.find_img(images_fp + "/youtube_upload/selected_video_title_text.png", 60)
    if (title_text[0] == True): pass
    else: sys.exit("!!! Unable to confirm that video has fully uploaded to youtube servers @ youtube_upload_video() @ youtube_upload_vid.py  @ /uploader_module/")

    #click on "Reuse details"
    reuse_details_btn = py_auto.find_img(images_fp + "/youtube_upload/reuse_details_btn.png", 6)
    n_secs, n_jits = random.uniform(0.99, 1.29), random.randrange(0, 3)
    py_auto.nav_pos(reuse_details_btn[1] + random.randrange(-20, 20), reuse_details_btn[2] + random.randrange(-5, 5), n_secs, n_jitters = n_jits, tpos_rand = 5)
    pyautogui.click()

    #click on "Search your videos" field
    search_ur_vids = py_auto.find_img(images_fp + "/youtube_upload/search_your_videos_field.png", 6)
    n_secs, n_jits = random.uniform(0.99, 1.29), random.randrange(0, 3)
    py_auto.nav_pos(search_ur_vids[1] + random.randrange(-40, 40), search_ur_vids[2] + random.randrange(-5, 5), n_secs, n_jitters = n_jits, tpos_rand = 5)
    time.sleep(random.uniform(0.80, 0.85))
    pyautogui.click()
    pyautogui.click()
    time.sleep(random.uniform(0.80, 0.85))

    #type in "What is something that is unattractive", to use that video as a template
    pyautogui.write("What is something that is unattractive", interval = 0.20)
    time.sleep(random.uniform(2.00, 2.45))
    
    #click on where the first result would be
    n_secs, n_jits = random.uniform(1.50, 2.00), random.randrange(0, 2)
    py_auto.nav_pos(595 + random.randrange(-20, 20), 485 + random.randrange(-20, 20), n_secs, n_jitters = n_jits, tpos_rand = 5)
    pyautogui.click()

    #click on "Reuse" button
    reuse_btn = py_auto.find_img(images_fp + "/youtube_upload/reuse_btn.png", 20)
    n_secs, n_jits = random.uniform(0.99, 1.29), random.randrange(0, 3)
    py_auto.nav_pos(reuse_btn[1] + random.randrange(-5, 5), reuse_btn[2] + random.randrange(-2, 2), n_secs, n_jitters = n_jits, tpos_rand = 3)
    pyautogui.click()
    time.sleep(random.uniform(0.40, 0.45))

    #click on title text field
    n_secs, n_jits = random.uniform(0.59, 0.89), random.randrange(0, 2)
    py_auto.nav_pos(title_text[1] + random.randrange(0, 201), title_text[2] + random.randrange(10, 20), n_secs, n_jitters = n_jits, tpos_rand = 5)
    pyautogui.click()

    #delete previous text and input title
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyDown("a")
    pyautogui.press("backspace")
    pyautogui.keyUp("a")
    pyautogui.keyUp("ctrlleft")
    py_auto.human_type(vid_title_str, 0.01, 0.01)
    time.sleep(random.uniform(0.30, 0.35))

    #click on description text field
    desc_text = py_auto.find_img(images_fp + "/youtube_upload/selected_video_description_text.png", 3)
    n_secs, n_jits = random.uniform(0.59, 0.89), random.randrange(0, 3)
    py_auto.nav_pos(desc_text[1] + random.randrange(0, 201), desc_text[2] + random.randrange(15, 25), n_secs, n_jitters = n_jits, tpos_rand = 5)
    pyautogui.click()

    #delete previous text and input description
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyDown("a")
    pyautogui.press("backspace")
    pyautogui.keyUp("a")
    pyautogui.keyUp("ctrlleft")
    py_auto.human_type(vid_description_str, 0.01, 0.01)
    time.sleep(random.uniform(0.30, 0.35))

    #move mouse above title text so as to not interfere with scrolling
    n_secs, n_jits = random.uniform(1.09, 1.49), random.randrange(0, 4)
    py_auto.nav_pos(title_text[1] + random.randrange(-30, 30), title_text[2] + random.randrange(20, 30), n_secs, n_jitters = n_jits, tpos_rand = 3)
    time.sleep(random.uniform(0.60, 0.65))

    #scroll down
    pyautogui.scroll(-10)
    time.sleep(random.uniform(0.60, 0.65))
    
    #click on "Yes, it's made for kids" button
    yes_mfk_btn = py_auto.find_img(images_fp + "/youtube_upload/made_for_kids_btn.png", 3)
    n_secs, n_jits = random.uniform(0.9, 1.42), random.randrange(0, 2)
    if (yes_mfk_btn[0] != False): py_auto.nav_pos(yes_mfk_btn[1], yes_mfk_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #click on "Next" button
    next_btn = py_auto.find_img(images_fp + "/youtube_upload/next_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    if (next_btn[0] != False): py_auto.nav_pos(next_btn[1], next_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #click on "Next" button again
    next_btn = py_auto.find_img(images_fp + "/youtube_upload/next_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    if (next_btn[0] != False): py_auto.nav_pos(next_btn[1], next_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #click on "Next" button again
    next_btn = py_auto.find_img(images_fp + "/youtube_upload/next_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    if (next_btn[0] != False): py_auto.nav_pos(next_btn[1], next_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #click on "Public" button
    public_btn = py_auto.find_img(images_fp + "/youtube_upload/public_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    if (public_btn[0] != False): py_auto.nav_pos(public_btn[1], public_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #click on "Publish" button
    publish_btn = py_auto.find_img(images_fp + "/youtube_upload/publish_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    if (publish_btn[0] != False): py_auto.nav_pos(publish_btn[1], publish_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #click on "Close" button
    close_us_btn = py_auto.find_img(images_fp + "/youtube_upload/close_upload_summary_btn.png", 3)
    n_secs, n_jits = random.uniform(1.00, 1.50), random.randrange(0, 3)
    if (close_us_btn[0] != False): py_auto.nav_pos(close_us_btn[1], close_us_btn[2], n_secs, n_jitters = n_jits, tpos_rand = 12)
    pyautogui.click()

    #log and return successful status
    print(f"successfully uploaded vid from /{vid_dir_parent_dir_name}/{video_to_upload_dir_name}/ to youtube")
    return 0
