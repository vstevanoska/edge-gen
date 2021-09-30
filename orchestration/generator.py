import sox
import subprocess
from os import remove
from glob import glob
from midi2audio import FluidSynth
import orchestration.config as config
import orchestration.constants as constants
from orchestration.bassline_generator import generate_bassline
from orchestration.drum_beat_generator import generate_drum_beat
from orchestration.markov_chord_generator import generate_sequence


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
    _generate_bass_track(progression, 1)
    _generate_chord_progression(progression)


def _generate_drum_track():
    drum_midi = generate_drum_beat(config.song_bars)

    with open(constants.output_dir + "drum_track.mid", "wb") as drum_file:
        drum_midi.writeFile(drum_file)


def _generate_bass_track(progression: str, amount_of_notes_per_bar: int = 1):
    bass_midi = generate_bassline(progression, amount_of_notes_per_bar)

    with open(constants.output_dir + "bass_track.mid", "wb") as bass_file:
        bass_midi.writeFile(bass_file)


def _generate_chord_progression(progression: str):
    c2m_command = "c2m {} --bpm {} --octave 5 --pattern basic --duration 2 --output {}" \
        .format(progression, config.song_bpm, constants.output_dir + "pad_track.mid")

    process = subprocess.Popen(c2m_command.split(), stdout=subprocess.PIPE)

    process.communicate()


def _generate_wav():
    _convert_midi_to_wav("drums.sf2", "drum_track")
    _convert_midi_to_wav("pads.sf2", "pad_track")
    _convert_midi_to_wav("bass.sf2", "bass_track")


def _convert_midi_to_wav(soundfont: str, track_name: str):
    fs = FluidSynth(constants.soundfont_dir + soundfont)
    
    fs.midi_to_audio(constants.output_dir + track_name + ".mid",
                     constants.output_dir + track_name + ".wav")
    
    remove(constants.output_dir + track_name + ".mid")


def _mix_music():
    wav_files = glob(constants.output_dir + '/[!master]*.wav')

    combiner = sox.Combiner()
    combiner.build(wav_files, constants.output_dir + "master_track.wav", "merge")

    [remove(x) for x in wav_files]
