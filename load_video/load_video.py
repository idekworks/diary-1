'''
load a video file and convert it to a jpeg file.

default file structure
load_video.py
param.py
input


'''

import subprocess
import os
import sys

from param import parse_param

if __name__ == "__main__":
    param = parse_param()
    
    input_files = []
    with open(param.input, 'r') as f:
        for row in f:
            input_files.append(row[:-1])
    # save the image to tmp
    if os.path.exists('tmp'):
        subprocess.call('rm -rf tmp', shell=True)
    
    for input_file in input_files:
        video_path = os.path.join(param.video_path, input_file)
        if os.path.exists(video_path):
            print(video_path)
            subprocess.call('mkdir tmp', shell=True)
            subprocess.call('ffmpeg -i {} tmp/image_%05d.jpg'.format(video_path), shell=True)
            subprocess.call('rm -rf tmp', shell=True)
        else:
            print('{} does not exist'.format(input_file))
