from pychord import Chord
from random import randrange
import orchestration.config as config
import orchestration.constants as constants
from orchestration.instrument import Instrument


class Bass(Instrument):
    def __init__(self, identifier: str, amount_of_notes_per_bar: int = 1, note_duration: int = 2) -> None:
        super().__init__(identifier=identifier, note_duration=note_duration)

        self.progression: list = config.progression
        self.amount_of_notes_per_bar: int = amount_of_notes_per_bar

    def generate(self) -> None:
        self.duration /= self.amount_of_notes_per_bar

        self.midi_file.addTempo(self.track, self.current_beat, config.song_bpm)

        for chord in self.progression:
            for _ in range(self.amount_of_notes_per_bar):
                note_value = self._choose_note_value_from_chord(Chord(chord))
                self.add_note(note=note_value, duration=self.duration)

                self.current_beat += self.duration

        self.save_midi()
        self.midi_to_audio()

    def _choose_note_value_from_chord(self, chord: Chord) -> int:
        chord_notes = chord.components()
        note_from_chord = chord_notes[randrange(0, len(chord_notes))]

        out_note: int = 0

        if note_from_chord in constants.midi_notes.keys():
            out_note = constants.midi_notes[note_from_chord] - 12

        else:
            out_note = constants.note_alias[note_from_chord] - 12

        return out_note
