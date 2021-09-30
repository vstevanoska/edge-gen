from pychord import Chord
from random import randrange
from midiutil import MIDIFile
import orchestration.config as config
import orchestration.constants as constants

track = 0
channel = 0
duration = 2
velocity = 127


midi_file = MIDIFile(1)


def generate_bassline(progression: str, amount_of_notes_per_bar: int = 1):
    global duration
    duration /= amount_of_notes_per_bar

    current_beat = 0

    midi_file.addTempo(track, current_beat, int(config.song_bpm))

    for chord in progression.split(' '):
        for _ in range(amount_of_notes_per_bar):
            note_value = _choose_note_value_from_chord(Chord(chord))
            midi_file.addNote(track, channel, note_value, current_beat, duration, velocity)

            current_beat += duration

    return midi_file


def _choose_note_value_from_chord(chord: Chord):
    chord_notes = chord.components()
    note_from_chord = chord_notes[randrange(0, len(chord_notes))]

    out_note = 0

    if note_from_chord in constants.midi_notes.keys():
        out_note = constants.midi_notes[note_from_chord] - 12

    else:
        out_note = constants.note_alias[note_from_chord] - 12
        
    return out_note