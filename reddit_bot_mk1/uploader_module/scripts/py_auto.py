#!/usr/bin/python3

import pyautogui

import math, time, random, sys



#vars

prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]



#functions

#function that navigates like a human to an element
def nav_pos(target_x, target_y, secs, n_jitters = None, tpos_rand = None):

    start_x, start_y = pyautogui.position().x, pyautogui.position().y
    screen_x, screen_y, n_times_scr_x_larger_than_scr_y = pyautogui.size()[0], pyautogui.size()[1], pyautogui.size()[0] / pyautogui.size()[1]

    targets = []

    #jittery calculations 
    if (n_jitters != None and n_jitters > 0):

        #calculate destination between current pos and target pos and n jitters
        curr_dist = math.sqrt((target_x - start_x)**2 + (target_y - start_y)**2)
        start_dist = curr_dist

        jitter_dist = curr_dist / n_jitters

        #for every jitter add a new target pos    
        for n_jitter in range(1, math.floor(n_jitters) + 1):

            dist_x, dist_y = target_x - pyautogui.position().x, target_y - pyautogui.position().y
            jitter_dist_x = dist_x / n_jitters
            jitter_dist_y = dist_y / n_jitters

            #get jitter x
            if (pyautogui.position().x > target_x):
                dist_x = pyautogui.position().x - target_x
                jitter_dist_x = dist_x / n_jitters
                jitter_x = pyautogui.position().x - (jitter_dist_x * n_jitter)
            elif (pyautogui.position().x <= target_x):
                dist_x = target_x - pyautogui.position().x
                jitter_dist_x = dist_x / n_jitters
                jitter_x = pyautogui.position().x + (jitter_dist_x * n_jitter)

            #randomize jitter_x
            if (int(dist_x * 0.15) != 0): rand_num = random.randrange(int(-dist_x * 0.15), int(dist_x * 0.15))
            else: rand_num = 0
            if (jitter_x + rand_num >= 0 and jitter_x + rand_num <= pyautogui.size()[0]):
                jitter_x += rand_num

            #get jitter y
            if (pyautogui.position().y > target_y):
                dist_y = pyautogui.position().y - target_y
                jitter_dist_y = dist_y / n_jitters
                jitter_y = pyautogui.position().y - (jitter_dist_y * n_jitter)
            elif (pyautogui.position().y <= target_y):
                dist_y = target_y - pyautogui.position().y
                jitter_dist_y = dist_y / n_jitters
                jitter_y = pyautogui.position().y + (jitter_dist_y * n_jitter)

            #randomize jitter_y
            if (int(dist_y * 0.15) != 0): rand_num = random.randrange(int(-dist_y * 0.15), int(dist_y * 0.15))
            else: rand_num = 0
            if (jitter_y + rand_num >= 0 and jitter_y + rand_num <= pyautogui.size()[1]):
                jitter_y += rand_num

            curr_dist = math.sqrt((target_x - start_x)**2 + (target_y - start_y)**2)
            secs_for_move = (secs / n_jitters) * (start_dist / math.sqrt((jitter_x * n_times_scr_x_larger_than_scr_y)**2 + jitter_y**2))
            targets.append((jitter_x, jitter_y, secs_for_move))

    #append target to targets
    curr_dist = math.sqrt((target_x - start_x)**2 + (target_y - start_y)**2)
    if (n_jitters != None and n_jitters > 1):
        secs_for_move = (secs / n_jitters) * (start_dist / math.sqrt((jitter_x * n_times_scr_x_larger_than_scr_y)**2 + jitter_y**2))
    else: secs_for_move = secs

    if (tpos_rand != None and tpos_rand != 0):
        target_x += random.randrange(-tpos_rand, tpos_rand)
        target_y += random.randrange(-tpos_rand, tpos_rand)

    targets.append((target_x, target_y, secs_for_move))

    #move
    for target in targets:
        pyautogui.moveTo(target[0], target[1], target[2], pyautogui.easeInOutQuad)

#function that finds image on the screen
def find_img(img_fp, max_seconds, serious = None):

    n_attempts = 0
    while (n_attempts <= max_seconds * 4):
        try:
            target = pyautogui.locateCenterOnScreen(img_fp, confidence = 0.9)
            return (True, target[0], target[1])
            break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.25)
            n_attempts += 1
            continue
    if (n_attempts > max_seconds * 4 and serious != True):
        print("!!! Maximum seconds for find_img() of image: \"" + img_fp + "\" have been exceeded")
        return (False, 0, 0)
    elif (n_attempts > max_seconds * 4 and serious == True): raise Exception("!!! Maximum seconds for find_img() of image: \"" + img_fp + "\" have been exceeded")

#function that types like a human
def human_type(string, typing_speed, variance = None):
    
    for char in string:
        type_spd = typing_speed
        if (variance != None and variance != 0): 
            if (typing_speed - variance >= 0.01): type_spd += random.uniform(-variance, variance)
            else: type_spd += random.uniform(0.01, variance)
        pyautogui.write(char, interval = type_spd)
