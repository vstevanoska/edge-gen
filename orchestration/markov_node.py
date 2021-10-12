from typing import List


class MarkovNode:
    def __init__(self, notes: List[str], probabilities: List[float]) -> None:
        self.scale: List[str] = []
        self.notes: List[str] = notes
        self.possible_options: List[str] = []
        self.probabilities: List[float] = probabilities

    def __repr__(self) -> str:
        return 'Notes: {}\nProbabilities: {}\nScale: {}\nPossible options: {}'.format(
            '-'.join(self.notes), self.probabilities, self.scale, self.possible_options)
