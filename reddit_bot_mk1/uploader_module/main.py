#!/usr/bin/python3

# ARGUMENTS:
#
#   "--platform"        "tiktok", "youtube"                 PLATFORM TO POST ON
#   "--vids_p_dir_fp"   "'[dir]'"                           VIDEO DIRS' PARENT DIR


import os, sys, time, random

import pyautogui, argparse

sys.path.insert(1, "/home/aryan/Documents/reddit_bot_mk1/uploader_module/scripts")

import py_auto

from general_upload_vid_funcs import *
from tiktok_upload_vid_funcs import *
from youtube_upload_vid_funcs import *




#args
parser = argparse.ArgumentParser()

#argument to pass whether to post on tiktok or youtube
parser.add_argument(
    "--platform",
    nargs = 1,
    required = True,
    choices = ["tiktok", "youtube"]
)

#argument to pass name of video directories' parent directory
parser.add_argument(
    "--vids_p_dir_fp",
    nargs = 1,
    required = True
)

args = parser.parse_args()


# vars
images_fp = "/home/aryan/Documents/reddit_bot_mk1/uploader_module/images"
final_products_fp = "/home/aryan/Documents/reddit_bot_mk1/final_products"

platform = args.platform[0]

videos_parent_dir_fp = args.vids_p_dir_fp[0]
video_dir_names = os.listdir(videos_parent_dir_fp)

tiktok_fullscreen_profile_icon_pos = (1875, 183)



# functions

# function that returns the name of the last dir/file in a filepath
def get_name_last_file_in_fp(fp_str):

    result = ""
    for char in fp_str:
        result += char
        if (char == "/"): result = ""
    return result



# execute

# 1. tiktok
if (platform == "tiktok"):

    # 1.1. open tiktok and wait to load initially
##### MAKE IT OPEN TIKTOK STUDIO INSTEAD #####################################################
#    open_tab("https://www.tiktok.com")

    # sanity check if logged in initially by checking if able to find "Login" button
    login_btn = py_auto.find_img(images_fp + "/tiktok_login/tiktok_login_button.png", 10)
    if (login_btn[0] == True): pass
    else: tiktok_tab.tiktok_logout()

    # 1.2. log into account
#    tiktok_google_login(goog_email, goog_password)

    # 1.3. go to tiktok studio
    tiktok_home_page_nav_to_studio()

    # 1.4. upload vid from every directory specified
    for n_vid_dir_name in range(0, len(video_dir_names)):

        # 1.4.1. get vid description from description.txt
#        with open(final_products_fp + "/" + videos_parent_dir_name + "/" + video_dir_names[n_vid_dir_name] + "/description.txt", "r") as desc_file:
        with open(videos_parent_dir_fp + "/" + video_dir_names[n_vid_dir_name] + "/description.txt", "r") as desc_file:
            desc = desc_file.read()

        # 1.4.2 upload vid
        tiktok_upload_video(video_dir_names[n_vid_dir_name], videos_parent_dir_name, desc + " #fyp #foryou #storytime #reddit #reddit_tiktok #redditstorytime #redditstoriestts #redditreadings #redditguy")

    # 1.5. go back to home page
    tiktok_studio_nav_to_home_page()

    # 1.6. log out of account
    tiktok_logout()
    time.sleep(random.uniform(2, 2.5))

    # 1.7. close tab
    close_tab()

# 2. youtube
elif (platform == "youtube"):

    # youtube uploading status | 0 == no error, upload | 1 == error, do not upload
    yt_upload_status = 0

    # 2.2. upload vid from every directory specified
    for n_vid_dir_name in range(0, len(video_dir_names)):

        # 2.2.1. get vid description from description.txt and name of videos' dirs' parent dir
        with open(videos_parent_dir_fp + "/" + video_dir_names[n_vid_dir_name] + "/description.txt", "r") as desc_file:
            desc = desc_file.read()
        videos_parent_dir_name = get_name_last_file_in_fp(videos_parent_dir_fp)

        # 2.2.2 upload vid
        if (yt_upload_status == 0):
            yt_upload_status = youtube_upload_video(video_dir_names[n_vid_dir_name], videos_parent_dir_name, desc, desc + "#storytime #reddit #redditshorts #redditstorytime #redditstories #redditposts #redditguy #redditmemes")
