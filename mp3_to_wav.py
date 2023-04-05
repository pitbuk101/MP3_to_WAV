import os
import argparse
from pydub import AudioSegment

# create argument parser
parser = argparse.ArgumentParser(description='Convert MP3 files to WAV format')
parser.add_argument('input_folder', type=str, help='Input folder path containing MP3 files')
parser.add_argument('output_folder', type=str, help='Output folder path to save WAV files')

# parse arguments

args = parser.parse_args(['./Argument_1', './Argument_2'])


# create output folder if it doesn't exist
if not os.path.exists(args.output_folder):
    os.makedirs(args.output_folder)

# loop through all files in the input folder
for filename in os.listdir(args.input_folder):
    if filename.endswith('.mp3'):
        # load the MP3 file and convert it to WAV format
        sound = AudioSegment.from_mp3(os.path.join(args.input_folder, filename))
        sound.export(os.path.join(args.output_folder, filename[:-4] + '.wav'), format='wav')
