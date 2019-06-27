'''
code for entering runtime parameters

--input: video file name
--video_path: video file path
 

'''

import argparse

def parse_param():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input', type=str, help='input video file name')
    parser.add_argument('--video_path', default='./', type=str, help='input video file path')

    args = parser.parse_args()
    
    return args
