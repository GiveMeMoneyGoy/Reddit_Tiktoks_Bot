#!/usr/bin/python3



# ARGUMENT 1 : FILEPATH TO SCREENSHOT OF POST
# ARGUMENT 2 : FILEPATH TO POST AUDIO
# ARGUMENT 3 : LENGTH OF POST AUDIO IN SECONDS
# ARGUMENT 2 : FILEPATH TO TR AUDIO
# ARGUMENT 4 : LENGTH OF TR AUDIO IN SECONDS
# ARGUMENT 5 : FILEPATH TO BACKGROUND CLIP
# ARGUMENT 6 : FILEPATH TO TR SUBTITLES
# ARGUMENT 7 : NAME OF WOULD-BE RESULT



from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, CompositeVideoClip, CompositeAudioClip, TextClip, concatenate_videoclips
from moviepy.video.fx.all import crop
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.audio.fx.all as afx
import sys, random



#vars
vid_width_px = 608
vid_left_border = (1920 - vid_width_px) / 2



#functions

#function that generates a video
def generate_tr_video(post_screenshot_fp, post_audio_fp, post_audio_len, tr_audio_fp, tr_audio_len, subtitles_srt_fp, bg_clip_fp, bg_music_fp, result_fp):

    #get length and beginning of video
    bg_clip_begg = random.randrange(0, 3600)
    vid_len = 2 + post_audio_len + tr_audio_len

    #get background clip and image of post
    post_image = ImageClip(post_screenshot_fp).set_start(0.25).set_duration(post_audio_len).resize(width=520).set_pos(("center", "center"))
    bg_clip = VideoFileClip(bg_clip_fp).subclip(bg_clip_begg, bg_clip_begg + vid_len).crop(x1 = vid_left_border, width = vid_width_px)

    #get audioclips
    post_audio_clip = AudioFileClip(post_audio_fp)
    tr_audio_clip = AudioFileClip(tr_audio_fp)
    bg_music_clip = AudioFileClip(bg_music_fp).set_duration(vid_len)

    #get subtitles
    generator = lambda txt: TextClip(txt, font = "Montserrat-Bold", fontsize = 38, color = "white", stroke_color = "black", stroke_width = 1.75)
    sub_clip = SubtitlesClip(subtitles_srt_fp, generator)


    #compose video and audio
    result_vid = CompositeVideoClip([bg_clip, post_image, sub_clip.set_pos(("center", "center"))])
    res_audio = CompositeAudioClip([post_audio_clip.set_start(0.25), tr_audio_clip.set_start(0.5 + post_audio_len), bg_music_clip.fx(afx.volumex, 0.5)])

    #build
    result_vid.audio = res_audio

    #save
    result_vid.write_videofile(result_fp, fps = result_vid.fps, codec = "libx264", temp_audiofile = "temp-audio.m4a", remove_temp = True, audio_codec = "aac")
