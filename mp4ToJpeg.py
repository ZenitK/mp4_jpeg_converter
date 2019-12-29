#!/usr/bin/python3
import subprocess
import sys
from os import listdir
from os.path import isfile, join

source_path = sys.argv[1]
output_path = sys.argv[2]

print("converting mp3 files from %s" % source_path)

all_files = listdir(source_path)

mp4_files = [f for f in all_files if (isfile(join(source_path, f)) and f.lower().endswith('mp4'))]

for mp4_file in mp4_files:
    print('Converting ' + mp4_file + ' to jpeg')
    jpeg_file_pattern = mp4_file.replace('.MP4', '_%03d.jpg')
    jpeg_full_path = join(output_path, jpeg_file_pattern)
    ffmpeg_args = ['ffmpeg', '-i', join(source_path, mp4_file), '-qscale:v', '2', jpeg_full_path]
    subprocess.call(args=ffmpeg_args)

    print('Converted ' + mp4_file + ' to jpeg')
