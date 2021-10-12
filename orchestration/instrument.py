from abc import ABC
from os import remove
from midi2audio import FluidSynth
from midiutil.MidiFile import MIDIFile
import orchestration.constants as constants


class Instrument(ABC):
    def __init__(self, identifier: str, note_duration: int = 2) -> None:
        super().__init__()

        self.identifier = identifier
        self.track = 0
        self.channel = 0
        self.duration = note_duration
        self.velocity = 127
        self.current_beat = 0

        self.midi_file = MIDIFile(1)

    def add_note(self, note: int, duration: float) -> None:
        self.midi_file.addNote(self.track, self.channel,
                               note, self.current_beat, duration, self.velocity)

    def generate(self) -> None:
        raise NotImplementedError()

    

    def save_midi(self) -> None:
        with open(constants.output_dir + self.identifier + '.mid', 'wb') as midi:
            self.midi_file.writeFile(midi)

    def midi_to_audio(self) -> None:
        fs = FluidSynth(constants.soundfont_dir + self.identifier + '.sf2')

        fs.midi_to_audio(constants.output_dir + self.identifier + '.mid',
                         constants.output_dir + self.identifier + '.wav')

        remove(constants.output_dir + self.identifier + '.mid')
