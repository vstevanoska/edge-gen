import numpy as np
from music_generation.configuration import keys

possible_options = []

probability_matrix = [
    [0.00, 0.50, 0.35, 0.10, 0.05],
    [0.30, 0.00, 0.35, 0.20, 0.15],
    [0.35, 0.40, 0.00, 0.10, 0.15],
    [0.15, 0.15, 0.25, 0.00, 0.45],
    [0.20, 0.10, 0.45, 0.25, 0.00]
]


def _generate_possible_options(key_index: int):
    options = []
    progression_indexes = [0, 5, 7, 10, 3]

    for i in range(len(progression_indexes)):
        current_index = (key_index + progression_indexes[i]) % 12
        options.append(keys[current_index])

    return options


def _predict_next_state(note: str):
    global possible_options
    return np.random.choice(possible_options, p=probability_matrix[possible_options.index(note)])


def generate_sequence(chord: str, length: int = 30):
    original_chord = chord
    length -= 2

    global possible_options
    possible_options = _generate_possible_options(keys.index(original_chord))

    chords = []
    chords.append(chord)

    for n in range(length):
        chords.append(_predict_next_state(chords[-1]))

    chords.append(original_chord)

    for chord in chords:
        if possible_options.index(chord) <= 1:
            chords[chords.index(chord)] += "m"

        elif possible_options.index(chord) == 2:
            chords[chords.index(chord)] += "7"

    return chords
