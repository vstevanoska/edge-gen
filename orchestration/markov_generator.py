import numpy as np
from typing import List
from orchestration.constants import keys
import orchestration.config as config

class MarkovGenerator:
    def __init__(self) -> None:
        self.possible_options = []


    def _generate_possible_options(self, key_index: int) -> List[str]:
        options = []
        progression_indexes = [0, 5, 7, 10, 3]

        for i in range(len(progression_indexes)):
            current_index = (key_index + progression_indexes[i]) % 12
            options.append(keys[current_index])

        return options


    def _predict_next_state(self, note: str) -> str:
        return np.random.choice(self.possible_options, p=config.probability_matrix[self.possible_options.index(note)])


    def generate_sequence(self, chord: str, length: int = 30) -> List[str]:
        self.possible_options = self._generate_possible_options(keys.index(chord))

        chords = []
        chords.append(chord)

        for _ in range(length - 2):
            chords.append(self._predict_next_state(chords[-1]))

        chords.append(chord)

        for chord in chords:
            if self.possible_options.index(chord) <= 1:
                chords[chords.index(chord)] += "m"

            elif self.possible_options.index(chord) == 2:
                chords[chords.index(chord)] += "7"

        return chords
