import os, json

from libraries.resource_path import resource_path
from libraries.logger import log

class OptionsManager():
    def __init__(self):
        self.JSON_PATH = resource_path('json\options.json')
        self.music_volume = 0.5
        self.sounds_volume = 0.25
        if not os.path.exists(self.JSON_PATH):
            log.info("the json/options.json file does not exist. The new one was created.")
            with open(self.JSON_PATH, 'w') as f:
                json.dump({
                    'music_volume': 0,
                    'sounds_volume': 0,
                }, f)

        try:
            self._import_data()
        except:
            log.info("The json/options.json format isn't the required one. The json/options.json file was reset.")

    def _save(self):
        with open(self.JSON_PATH, 'w') as f:
            json.dump({
                'music_volume': self.music_volume,
                'sounds_volume': self.sounds_volume,
            }, f)
        log.info("Data has been saved in the options.json file.")

    def _import_data(self):
        with open(self.JSON_PATH, 'r') as f:
            data = json.load(f)
            self.music_volume = data.get('music_volume', 0)
            self.sounds_volume = data.get('sounds_volume', 0)
        log.info("Data has been imported from the options.json file.")

options_manager = OptionsManager()
