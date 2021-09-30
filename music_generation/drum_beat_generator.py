from midiutil import MIDIFile
import music_generation.configuration as config

current_beat = 0
track = 0
channel = 0
duration = 0.25
velocity = 127


drum_notes = {
    "cymbal": 61,
    "hats":   57,
    "snare":  52,
    "kick":   48,
}

drum_pattern = {
#             |1                   |2                  |3                  |4
    "hats":   ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O', ' '],
    "snare":  [' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' '],
    "kick":   ['O', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', 'O', ' ', ' ', ' ', ' ', ' ']
}

midi_file = MIDIFile(1)


def generate_drum_beat(num_of_beats: int):
    global midi_file

    midi_file.addTempo(track, current_beat, int(config.song_bpm))
    midi_file.addNote(track, channel, drum_notes['cymbal'], current_beat, duration, velocity)

    for _ in range(int(num_of_beats / 2)):
        _generate_single_beat()
    
    midi_file.addNote(track, channel, drum_notes['kick'], current_beat, 2, velocity)
    midi_file.addNote(track, channel, drum_notes['cymbal'], current_beat, 2, velocity)

    return midi_file


def _generate_single_beat():
    global current_beat

    for i in range(len(drum_pattern['hats'])):
        if drum_pattern['hats'][i] == "O":
            midi_file.addNote(track, channel, drum_notes['hats'], current_beat, duration, velocity)

        if drum_pattern['snare'][i] == "O":
            midi_file.addNote(track, channel, drum_notes['snare'], current_beat, duration, velocity)

        if drum_pattern['kick'][i] == "O":
            midi_file.addNote(track, channel, drum_notes['kick'], current_beat, duration, velocity)

        current_beat += duration
