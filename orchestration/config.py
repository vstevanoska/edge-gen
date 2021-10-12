from typing import List
from orchestration.markov_node import MarkovNode

bpm: int = 80
key: str = 'C'
bars: int = 16
feel: str = 'minor'

progression: List[str] = []

probability_matrices: List[MarkovNode] = [

    MarkovNode(notes=['I', 'IV'],
               probabilities=[
                   [0.40, 0.60],
                   [0.60, 0.40]]
               ),

    MarkovNode(notes=['I', 'V'],
               probabilities=[
                   [0.40, 0.60],
                   [0.60, 0.40]]
               ),

    MarkovNode(notes=['I', 'IV', 'V'],
               probabilities=[
                   [0.10, 0.60, 0.30],
                   [0.40, 0.10, 0.50],
                   [0.45, 0.40, 0.15]]
               ),
    MarkovNode(notes=['II', 'V', 'I'],
               probabilities=[
                   [0.05, 0.50, 0.45],
                   [0.15, 0.30, 0.55],
                   [0.20, 0.40, 0.40]]
               ),

    MarkovNode(notes=['I', 'VI', 'IV', 'V'],
               probabilities=[
                   [0.10, 0.35, 0.30, 0.25],
                   [0.15, 0.05, 0.50, 0.30],
                   [0.30, 0.20, 0.10, 0.40],
                   [0.40, 0.20, 0.35, 0.05]]
               ),

    MarkovNode(notes=['I', 'VI', 'II', 'V'],
               probabilities=[
                   [0.10, 0.45, 0.15, 0.30],
                   [0.15, 0.10, 0.40, 0.35],
                   [0.15, 0.30, 0.05, 0.50],
                   [0.40, 0.30, 0.20, 0.10]]
               )
]
