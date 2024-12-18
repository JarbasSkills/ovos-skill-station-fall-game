from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import stationfall_intro_parser


class StationFallSkill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="stationfall",
                         game_lang="en-us",
                         game_data=f'{self.root_dir}/res/{self.game_id}.DAT',
                         intro_parser=stationfall_intro_parser,
                         **kwargs)
