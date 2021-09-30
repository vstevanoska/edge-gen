from os import getcwd

song_bpm: int = 80
song_key: str = "C"
song_bars: int = 16

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

keys: list = list(midi_notes.keys())

output_dir: str = getcwd() + "/build/"
soundfont_dir: str = getcwd() + "/music_generation/soundfonts/"