from os import mkdir, path
from orchestration.constants import output_dir
from orchestration.generator import generate_music

if __name__ == "__main__":
    if not path.exists(output_dir):
        mkdir(output_dir)

    generate_music()