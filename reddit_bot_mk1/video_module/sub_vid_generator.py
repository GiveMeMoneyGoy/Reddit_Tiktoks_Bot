#!/usr/bin/python3

# ARGUMENTS:
#
#   "--sub_dir_fp"     "'[sub dir filepath]'"   FILEPATH TO  SUBREDDIT DIRECTORY TO GENERATE FROM
#   "--pv_gen"      "'[voice gender option]'"   GENDER OF VOICE OF POST
#   "--rv_gen"      "'[voice gender option]'"   GENDER OF VOICE OF REPLY
#   "--subs_mult"   "[float num]"               MULTIPLIER FOR SUBTITLES DISPLAY SPEED



from tiktokvoice import tts

import os, sys, time, math
import pathlib, subprocess, random, asyncio
import argparse, pyautogui
from datetime import datetime

from mutagen.mp3 import MP3
from video_generator import generate_tr_video



#args
parser = argparse.ArgumentParser()
voice_choices = ["male", "male_goofy", "male_all", "male_and_female", "female"]

#argument to pass name of subreddit/subreddit dir
parser.add_argument(
    "--sub_dir_fp",
    nargs = 1,
    required = True
)

#argument to pass gender of tts voice that reads post
parser.add_argument(
    "--pv_gen",
    nargs = 1,
    required = True,
    choices = voice_choices
)

#argument to pass gender of tts voice that reads reply
parser.add_argument(
    "--rv_gen",
    nargs = 1,
    required = True,
    choices = voice_choices
)

#argument to pass /nav/ .txt filepath to write result videos' directory filepath to
parser.add_argument(
    "--nav_txt_fp",
    nargs = 1,
    required = True,
)

#argument to pass multiplier of subtitle display speed for debugging purposes
parser.add_argument(
    "--subs_mult",
    nargs = 1,
    required = False,
    choices = voice_choices,
    default = 1.05
)

#parse arguments
args = parser.parse_args()

scraped_sub_dir_fp = args.sub_dir_fp[0]
post_voice_gender = args.pv_gen[0]
tr_voice_gender = args.rv_gen[0]
nav_txt_fp = args.nav_txt_fp[0]
subs_speed_mult = args.subs_mult

#vars
max_n_words_sub, max_n_chars_sub = 4, 15
txt_to_srt_tool_fp = "/home/aryan/Documents/reddit_bot_mk1/video_module/txt_to_srt_tool"
final_products_dir = "/home/aryan/Documents/reddit_bot_mk1/final_products"
posts_cache_fp = scraped_sub_dir_fp + "/posts_cache"
post_folders = os.listdir(posts_cache_fp)

background_video_dir_fp = "/home/aryan/Documents/reddit_bot_mk1/video_module/background-video"
background_music_dir_fp = "/home/aryan/Documents/reddit_bot_mk1/video_module/background-audio"
background_video_choices = ["/minecraft_parkour_loop.mp4", "/slime_loop.mp4"]
background_music_choices = ["/1.mp3", "/2.mp3", "/3.mp3", "/4.mp3", "/5.mp3"]

now_str = datetime.now().strftime("%y-%m-%d_%H:%M:%S")
results_dir_fp = final_products_dir + "/" + now_str
if (len(post_folders) != 0): os.system("mkdir " + results_dir_fp)

#voice vars
tts_male_voices_list = ["en_us_010", "en_uk_003", "en_au_002", "en_uk_001"]
tts_male_goofy_voices_list = ["en_us_ghostface", "en_male_narration", "en_us_rocket", "en_us_006"]
tts_male_all_voices_list = ["en_us_ghostface", "en_male_narration", "en_us_rocket", "en_us_006", "en_us_010", "en_uk_003", "en_au_002", "en_uk_001"]
tts_male_and_female_voices_list = ["en_us_010", "en_uk_003", "en_au_002", "en_uk_001", "en_us_001", "en_au_001", "en_us_002"]
tts_female_voices_list = ["en_us_001", "en_au_001", "en_us_002"]

#^LIST OF VOICES: https://github.com/oscie57/tiktok-voice/wiki/Voice-Codes
#  english voices:
#   -disney voices: en_us_ghostface, en_us_chewbacca, en_us_c3po, en_us_stitch, en_us_stormtrooper, en_us_rocket, en_female_madam_leota
#   -english voices (normal):
#     -male: en_au_002, en_uk_001, en_uk_003, en_us_006, en_us_007, en_us_009, en_us_010
#     -female: en_au_001, en_us_001, en_us_002,
#   -english voices (other): en_male_narration, en_male_funny, en_female_emotional



#functions

#function that creates mp3
def create_mp3(text_to_read, fp, gender):

    #randomzie voice
    if (gender == "male"):
        index = random.randrange(0, len(tts_male_voices_list))
        tts_voice = tts_male_voices_list[index]

    elif (gender == "male_goofy"):
        index = random.randrange(0, len(tts_male_goofy_voices_list))
        tts_voice = tts_male_goofy_voices_list[index]

    elif (gender == "male_all"):
        index = random.randrange(0, len(tts_male_all_voices_list))
        tts_voice = tts_male_all_voices_list[index]

    elif (gender == "male_and_female"):
        index = random.randrange(0, len(tts_male_and_female_voices_list))
        tts_voice = tts_male_and_female_voices_list[index]

    elif (gender == "female"):
        index = random.randrange(0, len(tts_female_voices_list))
        tts_voice = tts_female_voices_list[index]

    else:
        print("!!! invalid gender passed to randomize_voice in vid_gen_handler.py")

    #create .mp3
    tts(text_to_read, tts_voice, fp, play_sound = False)

    #wait 0.5 seconds to as to not get blocked from the API or something
    time.sleep(0.5)

#coroutine that jiggles mouse
async def jiggle_mouse():

    pyautogui.moveTo(random.randrange(100, 1820), random.randrange(100, 980), 1)


#main coroutine
async def main():
    n_videos_from_sub = 0

    #for every post folder in posts_cache folder
    for n_post_folder in range(0, len(post_folders)):
    
        #get vars

        #filepath of directory of post and name of post
        post_dir_name = post_folders[n_post_folder]
        post_dir_fp = posts_cache_fp + "/" + post_dir_name

        #filepath of screenshot, content.txt and post_audio.txt
        post_screenshot_fp = post_dir_fp + "/post_screenshot.png"
        post_content_fp = post_dir_fp + "/content.txt"
        post_audio_fp = post_dir_fp + "/audio.mp3"

        #filepath of top_replies_cache and list of top reply directories
        tr_cache_fp = post_dir_fp + "/top_replies_cache"
        try: tr_folders = os.listdir(tr_cache_fp)
        except: continue

        #if post has worthy top replies (top reply folders)
        if (len(tr_folders) != 0):

            #get contents of post's content.txt as a string
            with open (post_content_fp, "r") as content_file:
                post_content = content_file.read()

            #create .mp3 of post content string
            create_mp3(post_content, post_audio_fp, post_voice_gender)

            print("created .mp3 for post #" + str(n_post_folder) + " with name: " + post_dir_name)

            #length of post audio .mp3
            post_audio_len_s = 0.0
            for file in pathlib.Path(post_dir_fp).iterdir():
                if str(file) == post_audio_fp:
                    audio = MP3(str(file))
                    post_audio_len_s = audio.info.length

            #for every reply in top_replies_cache folder
            for n_tr_folder in range(0, len(tr_folders)):

                #count n video       
                n_videos_from_sub += 1
 
                #get vars

                #filepath to this top reply's folder and name of folder
                tr_dir_name = tr_folders[n_tr_folder]
                tr_dir_fp = tr_cache_fp + "/" + tr_dir_name

                #filepath to reply_audio.txt and content.txt and subtitles.srt
                tr_content_fp = tr_dir_fp + "/content.txt"
                tr_audio_fp = tr_dir_fp + "/audio.mp3"
                tr_subtitles_fp = tr_dir_fp + "/subtitles.srt"
   
                #get contents of reply's content.txt as a string
                with open (tr_content_fp, "r") as content_file:
                    reply_content = content_file.read() 

                #create .mp3 of reply content string
                create_mp3(reply_content, tr_audio_fp, tr_voice_gender)

                print("  created .mp3 for reply #" + str(n_tr_folder) + " with name: " + tr_dir_name)

                #length of reply audio .mp3
                tr_audio_len_s = 0.0
                for file in pathlib.Path(tr_dir_fp).iterdir():
                    if str(file) == tr_audio_fp:
                        audio = MP3(str(file))
                        tr_audio_len_s = audio.info.length
                tr_audio_len_s = math.ceil(tr_audio_len_s) * float(subs_speed_mult)

                #subtitles .srt
                second_to_begin_reading = math.ceil(post_audio_len_s + 0.5)
                str_command_string = txt_to_srt_tool_fp + " " + tr_content_fp + " " + str(max_n_words_sub) + " " + str(max_n_chars_sub) + " " + str(tr_audio_len_s) + " " + str(subs_speed_mult) + " " + str(second_to_begin_reading) + " " + tr_subtitles_fp
                os.system(str_command_string)
    
                #get random background video and music fp
                background_vid_fp = background_video_dir_fp + background_video_choices[random.randrange(0, len(background_video_choices))]
                background_music_fp = background_music_dir_fp + background_music_choices[random.randrange(0, len(background_music_choices))]

                #generate dedicated folder
                vid_specific_folder_fp  = results_dir_fp + "/" + str(n_videos_from_sub) + "_"
                for n in range(0, 10):
                    vid_specific_folder_fp += str(random.randrange(0, 10))
                os.system("mkdir " + vid_specific_folder_fp)
        
                #create description.txt in dedicated video folder
                vid_desc_fp = vid_specific_folder_fp + "/description.txt"
                os.system("touch " + vid_desc_fp)

                #write contents of post to description.txt
                with open (vid_desc_fp, "w") as desc_file:
                    desc_file.write(post_content)

                #generate post-top reply video
                result_fp = vid_specific_folder_fp + "/vid.mp4"
                try:
                    generate_tr_video(post_screenshot_fp, post_audio_fp, post_audio_len_s, tr_audio_fp, tr_audio_len_s, tr_subtitles_fp, background_vid_fp, background_music_fp, result_fp)
                    print("  !!! generated video #" + str(n_videos_from_sub))
                except Exception as err: 
                    pass
                    print("  !!! error in video generation for video #" + str(n_videos_from_sub))
                    print(err)

                #remove top reply folder
                os.system("rm -rf " + tr_dir_fp)

                await jiggle_mouse()

        #remove post folder if there are no more top reply folders
        tr_folders = os.listdir(tr_cache_fp)
        if (len(tr_folders) == 0): os.system("rm -rf " + post_dir_fp)

    #write result videos' dir's filepath to /nav/ .txt
    with open(nav_txt_fp, "w") as nav_txt_file:
        nav_txt_file.write(results_dir_fp)

# execute
asyncio.run(main())
