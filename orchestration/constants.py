from os import getcwd

roman_numerals: dict = {
    'I':    1,
    'II':   2,
    'III':  3,
    'IV':   4,
    'V':    5,
    'VI':   6,
    'VII':  7,
}

midi_notes: dict = {
    'C':    36,
    'C#':   37,
    'D':    38,
    'D#':   39,
    'E':    40,
    'F':    41,
    'F#':   42,
    'G':    43,
    'G#':   44,
    'A':    45,
    'A#':   46,
    'B':    47,
}

note_alias: dict = {
    'Db':   37,
    'Eb':   39,
    'Gb':   42,
    'Ab':   44,
    'Bb':   46,
    'Cb':   47,
}

keys: list = list(midi_notes.keys())

drum_notes = {
    'cymbal': 61,
    'hats':   57,
    'snare':  52,
    'kick':   48,
}

drum_patterns = [
    {
    #             |1                   |2                  |3                  |4
        'hats':   ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
        'snare':  [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' '],
        'kick':   ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ']
    },
    {
    #             |1                   |2                  |3                  |4
        'hats':   ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
        'snare':  [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        'kick':   ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ']
    }
]

output_dir: str = getcwd() + '/build/'
soundfont_dir: str = getcwd() + '/orchestration/soundfonts/'