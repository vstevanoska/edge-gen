from genericpath import exists
from os import mkdir, path
from music_generation.configuration import output_dir
from music_generation.generator import generate_music

if __name__ == "__main__":
    if not path.exists(output_dir):
        mkdir(output_dir)
    generate_music()