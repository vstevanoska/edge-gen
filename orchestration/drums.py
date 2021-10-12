from random import randrange
import orchestration.config as config
from orchestration.instrument import Instrument
from orchestration.constants import drum_notes, drum_patterns


class Drums(Instrument):
    def __init__(self, identifier: str, note_duration: int = 0.25) -> None:
        super().__init__(identifier=identifier, note_duration=note_duration)

    def generate(self) -> None:
        self.midi_file.addTempo(self.track, self.current_beat, config.bpm)

        for bar in range(int(config.bars / 2)):
            if bar % 4 == 0:
                self.add_note(
                    note=drum_notes['cymbal'], duration=self.duration)

            self._generate_single_beat()

        self.add_note(note=drum_notes['kick'], duration=2)
        self.add_note(note=drum_notes['cymbal'], duration=2)

        self.save_midi()
        self.midi_to_audio()

    def _generate_single_beat(self) -> None:
        drum_pattern = drum_patterns[randrange(0, len(drum_patterns))]

        for i in range(16):
            if drum_pattern['hats'][i] == '#':
                self.add_note(note=drum_notes['hats'], duration=self.duration)

            if drum_pattern['snare'][i] == '#':
                self.add_note(note=drum_notes['snare'], duration=self.duration)

            if drum_pattern['kick'][i] == '#':
                self.add_note(note=drum_notes['kick'], duration=self.duration)

            self.current_beat += self.duration
