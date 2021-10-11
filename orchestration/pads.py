from subprocess import Popen, PIPE
import orchestration.config as config
import orchestration.constants as constants
from orchestration.instrument import Instrument


class Pads(Instrument):
    def __init__(self, identifier: str) -> None:
        super().__init__(identifier=identifier)
        
        self.progression: list = config.progression


    def generate(self) -> None:
        c2m_command = "c2m {} --bpm {} --octave 5 --pattern basic --duration 2 --output {}" \
            .format(' '.join(self.progression), config.song_bpm, constants.output_dir + self.identifier + ".mid")

        Popen(c2m_command.split(), stdout=PIPE).communicate()

        self.midi_to_audio()
