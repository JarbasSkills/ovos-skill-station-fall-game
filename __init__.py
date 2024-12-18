from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import stationfall_intro_parser


class StationFallSkill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # TODO - dedicated icon, use pyfrotz icon for now
        skill_icon = "https://raw.githubusercontent.com/TigreGotico/pyFrotz/refs/heads/dev/pyfrotz/gui/all/pyfrotz.png"
        bg = "http://infocom.elsewhere.org/gallery/stationfall/stationfall1.jpg"
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="stationfall",
                         game_lang="en-us",
                         game_data=f'{self.root_dir}/res/{self.game_id}.DAT',
                         intro_parser=stationfall_intro_parser,
                         skill_icon=skill_icon,
                         game_image=bg,
                         **kwargs)
