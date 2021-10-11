from typing import List

song_bpm: int = 80
song_key: str = "C"
song_bars: int = 16

progression: List[str] = []

probability_matrix = [
    [0.00, 0.50, 0.35, 0.10, 0.05],
    [0.30, 0.00, 0.35, 0.20, 0.15],
    [0.35, 0.40, 0.00, 0.10, 0.15],
    [0.15, 0.15, 0.25, 0.00, 0.45],
    [0.20, 0.10, 0.45, 0.25, 0.00]
]
