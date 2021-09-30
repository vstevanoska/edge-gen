import sox
import subprocess
import music_generation.configuration as config

from os import remove
from glob import glob
from midi2audio import FluidSynth
from music_generation.bass_generator import generate_bassline
from music_generation.drum_beat_generator import generate_drum_beat
from music_generation.markov_chord_generator import generate_sequence


def __init__():
    config.song_bpm = input("Enter the BPM of the song: ")
    config.song_key = input("Enter song key: ").upper()


def generate_music():
    __init__()

    _generate_music_midi()
    _generate_wav()
    _mix_music()


def _generate_music_midi():
    progression = ' '.join(generate_sequence(config.song_key, config.song_bars))

    _generate_drum_track()
    _generate_bass_track(progression)
    _generate_chord_progression(progression)


def _generate_drum_track():
    drum_midi = generate_drum_beat(config.song_bars)

    with open(config.output_dir + "drum_track.mid", "wb") as drum_file:
        drum_midi.writeFile(drum_file)


def _generate_bass_track(progression: str):
    bass_midi = generate_bassline(progression)

    with open(config.output_dir + "bass_track.mid", "wb") as bass_file:
        bass_midi.writeFile(bass_file)


def _generate_chord_progression(progression: str):
    c2m_command = "c2m {} --bpm {} --octave 5 --pattern basic --duration 2 --output {}" \
        .format(progression, config.song_bpm, config.output_dir + "pad_track.mid")

    process = subprocess.Popen(
        c2m_command.split(), stdout=subprocess.PIPE)

    process.communicate()


def _generate_wav():
    _convert_midi_to_wav(config.soundfont_dir + "drums.sf2", "drum_track")
    _convert_midi_to_wav(config.soundfont_dir + "pads.sf2", "pad_track")
    _convert_midi_to_wav(config.soundfont_dir + "bass.sf2", "bass_track")


def _convert_midi_to_wav(soundfont_path: str, track_name: str):
    fs = FluidSynth(soundfont_path)
    fs.midi_to_audio(config.output_dir + track_name + ".mid",
                     config.output_dir + track_name + ".wav")
    
    remove(config.output_dir + track_name + ".mid")


def _mix_music():
    wav_files = glob(config.output_dir + '/[!master]*.wav')

    combiner = sox.Combiner()
    combiner.build(wav_files, config.output_dir + "master_track.wav", "merge")

    [remove(x) for x in wav_files]
