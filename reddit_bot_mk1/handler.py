#!/usr/bin/python3

import os, time, sys

import pathlib, subprocess, datetime, random

import pyautogui



#FOR EVERY SUBREDDIT IN subreddits THERE SHOULD BE A VALUE IN google_linked_accs DICTIONARY WITH THE SAME NAME AS FIRST VALUE AND LIST WITH 2 ELEMENTS: EMAIL AND PASSWORD



#vars


#general
log_fp =                "/home/aryan/Documents/reddit_bot_mk1/handler_log.txt"

subreddits_cache_fp =   "/home/aryan/Documents/reddit_bot_mk1/subreddits_cache"
final_products_fp =     "/home/aryan/Documents/reddit_bot_mk1/final_products"

nav_dir_fp =            "/home/aryan/Documents/reddit_bot_mk1/nav"
nav_scraped_sub_dir_txt_fp = nav_dir_fp +   "/scraped_dir_fp.txt"
nav_result_videos_dir_txt_fp = nav_dir_fp + "/new_videos_dir_fp.txt"

scraper_exec_fp =       "rust_scraper/target/debug/rust_scraper"
vid_gen_fp =            "video_module/sub_vid_generator.py"
vid_uploader_fp =       "uploader_module/main.py"


#vid generation
post_tts_voice =        "male_and_female"
reply_tts_voice =       "male_all"


#reddit auth
user_agent_str =        "Mozilla/post-comment-reply/0.1"

username_str =          ""
password_str =          ""
client_id_str =         ""
client_secret_str =     ""

reddit_access_token_request_url = "https://www.reddit.com/api/v1/access_token"


#subreddits

# FOR EVERY SUBREDDIT IN subreddits THERE SHOULD BE A VALUE IN google_linked_accs DICTIONARY WITH THE SAME NAME AS FIRST VALUE AND LIST WITH 2 ELEMENTS: EMAIL AND PASSWORD
# PASSWORDS MUST NOT CONTAIN ANY OF THESE SYMBOLS: '()', '`',

subreddits =        ["AskReddit"]

google_linked_accs = {

    "AskReddit":    ["", ""],

}



#functions


#subreddit scraping

#function that calls the scraper and saves filepath of scraped subreddit's directory to specified .txt in /nav/
def call_scraper_for_sub(sub_name, sub_dir_nav_txt_fp):

    #call executable
    os.system("./" + scraper_exec_fp + " " + sub_name + " " + sub_dir_nav_txt_fp)

#function that instantiates subreddit directory after scrape
def get_sub_dir_fp_after_scrape(scraped_sub_dir_txt_fp):

    with open(scraped_sub_dir_txt_fp, "r") as nav_txt_file:
        fp = nav_txt_file.read()
    return fp


#video generation

#function that calls video generator and saves filepath of newly generated videos' directory to specified .txt in /nav/
def call_generator_for_sub(sub_dir_fp, result_vids_fp_txt_fp):
    
    #build command and execute
    os.system("python3 " + vid_gen_fp + " --sub_dir_fp " + sub_dir_fp + " --pv_gen " + post_tts_voice + " --rv_gen " + reply_tts_voice + " --nav_txt_fp " + result_vids_fp_txt_fp)

#function that instantiates video directory after generation
def get_vids_dir_fp_after_gen(new_videos_dir_fp_txt_fp):

    with open(new_videos_dir_fp_txt_fp, "r") as nav_txt_file:
        fp = nav_txt_file.read()
    return fp

#function that returns the name of a filesystem path's last objec
def get_name_of_fp_obj(fp):

    name = ""
    for char in fp:
        name += char
        if (char == "/"): name = ""
    return name


#video uploading

#function that calls the video uploader
def call_uploader(platform, g_email, g_pass, vids_parent_dir_name, vid_dirs):

    #build command and execute
    cmd = "python3 " + vid_uploader_fp + " --platform " + platform + " --email " + g_email + " --passw '" + g_pass + "' --vids_p_dir " + vids_parent_dir_name + " --vid_dirs " + vid_dirs

    print(cmd)

    process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    process.wait()


#time and debugging

#function that returns current hour:min:sec.msec
def get_time():

    now = datetime.datetime.now()
    return now.time()

#function that writes to handler_log.txt
def write_to_log(text):

    with open(log_fp, "a") as log_file:
        log_file.write(text + "\n")

#function that jiggles the mouse
def jiggle_mouse():

    pyautogui.moveTo(random.randrange(100, 1820), random.randrange(100, 980), 1)    


#execute

# log beginning of execution
curr_time = str(get_time())
print(curr_time + " -- begginning execution...")
write_to_log(curr_time + " -- begginning execution...")

# for every subreddit,
for sub_name in subreddits:

    try:

        # 1. scrape subreddit

        # 1.1. log beginning of scrape
        curr_time = str(get_time())
        print(curr_time + " -- scraping " + sub_name)
        write_to_log(curr_time + " -- scraping " + sub_name)

        # 1.2. scrape and save scraped sub dir filepath to .txt in /nav/
        call_scraper_for_sub(sub_name, nav_scraped_sub_dir_txt_fp)

        # 1.3. get scraped sub's dir's filepath
        scraped_sub_dir_fp = get_sub_dir_fp_after_scrape(nav_scraped_sub_dir_txt_fp)

        # 1.4. log end of scrape
        curr_time = str(get_time())
        print(curr_time + " -- finished scraping " + sub_name)
        write_to_log(curr_time + " -- finished scraping " + sub_name)


        # 2. generate videos

        # 2.1. log beginning of video generation
        print(curr_time + " -- beginning video generation")
        write_to_log(curr_time + " -- beginning video generation")

        # 2.2. generate videos and get vids directory
        call_generator_for_sub(scraped_sub_dir_fp, nav_result_videos_dir_txt_fp)

        # 2.3. get generated videos' dir's filepath and name
        genned_vids_dir_fp = get_vids_dir_fp_after_gen(nav_result_videos_dir_txt_fp)
        genned_vids_dir_name = get_name_of_fp_obj(genned_vids_dir_fp)

        # 2.4. get generated videos' directories as string
        vid_dirs = os.listdir(genned_vids_dir_fp)
        vid_dirs_str = ""
        for n_vid_dir in range(0, len(vid_dirs)):
            vid_dirs_str += "'"
            vid_dirs_str += vid_dirs[n_vid_dir]
            if (n_vid_dir != len(vid_dirs) - 1): vid_dirs_str += "' "
            else: vid_dirs_str += "'"

        # 2.5. log end of video generation
        curr_time = str(get_time())
        print(curr_time + " -- finished video generation, generated " + str(len(vid_dirs)) + " videos")
        write_to_log(curr_time + " -- finished video generation, generated " + str(len(vid_dirs)) + " videos")

################# UPLOADING INDEFINITELY DISABLED, DO IT MANUALLY ###
        # 3. upload videos if there are any
#        if (len(vid_dirs) != 0):

            # 3.1. log beginning of video upload
#            print(curr_time + " -- beginning video upload")
#            write_to_log(curr_time + " -- beginning video upload")

            # 3.2. upload videos
#            call_uploader("youtube", google_linked_accs[sub_name][0], google_linked_accs[sub_name][1], genned_vids_dir_name, vid_dirs_str)

            # 3.3. log beginning of video upload
#            curr_time = str(get_time())
#            print(curr_time + " -- finished video upload")
#            write_to_log(curr_time + " -- finished video upload")

    except Exception as err:
        print(err)
        sys.exit()

        # log end of execution
        curr_time = str(get_time())
        print(curr_time + " -- finished execution...")
        write_to_log(curr_time + " -- finished execution...")
