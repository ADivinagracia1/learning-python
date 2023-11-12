import random

feet_in_mile = 5280
kmph_to_mph = 1000/3600

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)