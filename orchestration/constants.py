from os import getcwd

midi_notes: dict = {
    "C":    36,
    "C#":   37,
    "D":    38,
    "D#":   39,
    "E":    40,
    "F":    41,
    "F#":   42,
    "G":    43,
    "G#":   44,
    "A":    45,
    "A#":   46,
    "B":    47,
}

note_alias: dict = {
    "Db":   37,
    "Eb":   39,
    "Gb":   42,
    "Ab":   44,
    "Bb":   46,
    "Cb":   47,
}

keys: list = list(midi_notes.keys())

output_dir: str = getcwd() + "/build/"
soundfont_dir: str = getcwd() + "/orchestration/soundfonts/"