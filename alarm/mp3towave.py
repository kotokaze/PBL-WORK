#! /usr/bin/env python3
import sys
import pydub
from pathlib import Path


if __name__ == "__main__":
	MP3_FILE_PATH = Path(sys.argv[1])
	if (MP3_FILE_PATH.suffix == 'mp3'):
		print(f"IN: {MP3_FILE_PATH}")

		OUTPUT_FILE_PATH = MP3_FILE_PATH.stem + '.wav'
		print(f"OUT: {OUTPUT_FILE_PATH}")

		audio = pydub.AudioSegment.from_mp3(MP3_FILE_PATH)
		audio.export(OUTPUT_FILE_PATH, format='wav')