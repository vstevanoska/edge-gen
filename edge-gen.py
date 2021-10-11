from os import mkdir, path
from orchestration.bass import Bass
from orchestration.pads import Pads
import orchestration.config as config
from orchestration.drums import Drums
from orchestration.constants import output_dir
from orchestration.orchestrator import Orchestrator

if __name__ == "__main__":
    if not path.exists(output_dir):
        mkdir(output_dir)

    orchestrator = Orchestrator()

    pads  = Pads(identifier="pads")
    bass  = Bass(identifier="bass", note_duration=2)
    drums = Drums(identifier="drums", note_duration=0.25)

    orchestrator.add_instrument(drums)
    orchestrator.add_instrument(bass)
    orchestrator.add_instrument(pads)

    orchestrator.orchestrate()
    orchestrator.mix_orchestration()