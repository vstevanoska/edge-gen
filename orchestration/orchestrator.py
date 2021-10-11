import sox
from os import remove
from glob import glob
from typing import List
import orchestration.config as config
import orchestration.constants as constants
from orchestration.instrument import Instrument
from orchestration.markov_generator import MarkovGenerator

class Orchestrator:
    def __init__(self) -> None:
        self.instruments: List[Instrument] = []

        config.song_bpm = int(input("Enter the BPM of the song: "))
        config.song_key = input("Enter song key: ").upper()

        markov_generator = MarkovGenerator()
        config.progression = markov_generator.generate_sequence(config.song_key, config.song_bars)

    def add_instrument(self, instrument) -> None:
        self.instruments.append(instrument)

    def orchestrate(self) -> None:
        for instrument in self.instruments:
            instrument.generate()

    def mix_orchestration(self) -> None:
        wav_files = glob(constants.output_dir + '/[!master]*.wav')

        combiner = sox.Combiner()
        combiner.build(wav_files, constants.output_dir + "master_track.wav", "merge")

        [remove(x) for x in wav_files]
