from typing import List
from numpy import random, roll
import orchestration.config as config
from orchestration.constants import keys, roman_numerals


class MarkovGenerator:
    def __init__(self) -> None:
        self.markov_node = config.probability_matrices[random.randint(
            0, len(config.probability_matrices))]

    def predict_next_state(self, note: str) -> str:
        note_probability = self.markov_node.possible_options.index(note)
        return random.choice(self.markov_node.possible_options, p=self.markov_node.probabilities[note_probability])

    def generate_possible_options(self, start_note: str) -> None:
        self.generate_scale(start_note)
        notes = [roman_numerals[number] -
                 1 for number in self.markov_node.notes]

        if config.feel == 'major':
            self.add_chord_quality(notes, [1, 2, 5], 6)

        elif config.feel == 'minor':
            self.add_chord_quality(notes, [0, 3, 4], 2)

    def add_chord_quality(self, notes: list, minor_intervals: list, diminished_note_index: int):
        for index, note in enumerate(notes):
            self.markov_node.possible_options.append(
                self.markov_node.scale[note])
            if note in minor_intervals:
                self.markov_node.possible_options[index] += 'm'

            elif note == diminished_note_index:
                self.markov_node.possible_options[index] += 'dim'

    def generate_scale(self, start_note: str) -> None:
        scale_shift = roll(keys, -keys.index(start_note))
        scale_indexes = []

        if config.feel == 'major':
            scale_indexes = [0, 2, 4, 5, 7, 9, 11]
            self.markov_node.scale = [scale_shift[i] for i in scale_indexes]

        elif config.feel == 'minor':
            scale_indexes = [0, 2, 3, 5, 7, 9, 11]
            self.markov_node.scale = [scale_shift[i] for i in scale_indexes]

    def generate_sequence(self, note: str, length: int = 30) -> List[str]:
        self.generate_possible_options(note)

        chords = [self.markov_node.possible_options[0]]

        for _ in range(length - 2):
            chords.append(self.predict_next_state(chords[-1]))

        chords.append(self.markov_node.possible_options[0])

        print(self.markov_node)
        print(chords)

        return chords
