from random import randrange
from midiutil import MIDIFile
import orchestration.config as config


current_beat = 0
track = 0
channel = 0
duration = 0.25
velocity = 127


midi_file = MIDIFile(1)


drum_notes = {
    "cymbal": 61,
    "hats":   57,
    "snare":  52,
    "kick":   48,
}

drum_patterns = [
    {
    #             |1                   |2                  |3                  |4
        "hats":   ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
        "snare":  [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' '],
        "kick":   ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ']
    },
    {
    #             |1                   |2                  |3                  |4
        "hats":   ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
        "snare":  [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        "kick":   ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ']
    }
]


def generate_drum_beat(num_of_bars: int):
    midi_file.addTempo(track, current_beat, int(config.song_bpm))

    for bar in range(int(num_of_bars / 2)):
        if bar % 4 == 0:
            add_note(note = drum_notes['cymbal'], duration = duration)

        _generate_single_beat()

    add_note(note = drum_notes['kick'], duration = 2)
    add_note(note = drum_notes['cymbal'], duration = 2)

    return midi_file


def _generate_single_beat():
    global current_beat

    drum_pattern = drum_patterns[randrange(0, len(drum_patterns))]

    for i in range(16):
        if drum_pattern['hats'][i] == '#':
            add_note(note = drum_notes['hats'], duration = duration)

        if drum_pattern['snare'][i] == '#':
            add_note(note = drum_notes['snare'], duration = duration)

        if drum_pattern['kick'][i] == '#':
            add_note(note = drum_notes['kick'], duration = duration)

        current_beat += duration


def add_note(note: int, duration: float):
    midi_file.addNote(track, channel, note, current_beat, duration, velocity)