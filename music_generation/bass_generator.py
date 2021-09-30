from pychord import Chord
from midiutil import MIDIFile
import music_generation.configuration as config

current_beat = 0
track = 0
channel = 0
duration = 2
velocity = 127


midi_file = MIDIFile(1)


def generate_bassline(progression: str):
    global current_beat
    global midi_file

    midi_file.addTempo(track, current_beat, int(config.song_bpm))

    chords = progression.split(' ')

    for _, chord in enumerate(chords):
        midi_file.addNote(track, channel, config.midi_notes[Chord(chord).root] - 12, current_beat, duration, velocity)
        current_beat += duration

    return midi_file
