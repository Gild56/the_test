import os, json, pygame

from kivy.clock import Clock

from libraries.resource_path import resource_path
from libraries.logger import log

from logic.text_manager import txt
from logic.music_manager import music_manager

class OptionsManager():
    def __init__(self):
        self.music_volume = 0.5
        self.sounds_volume = 0.25

        self.JSON_PATH = resource_path('json/options.json')

        if not os.path.exists(resource_path("json/")):
            os.makedirs(resource_path("json/"))
            log.info(
                "The json/ folder does not exist. "
                "A new json/ folder was created"
            )

        if not os.path.exists(self.JSON_PATH):
            self.clear()
            log.info(
                "the json/options.json file does not exist. "
                "The new one was created."
            )

        try:
            self._import_data()
        except:
            self.clear()
            log.info(
                "The json/options.json format isn't the required "
                "one. The json/options.json file was reset."
            )


    def _save(self):

        with open(self.JSON_PATH, 'w') as f:
            json.dump({
                'music_volume': self.music_volume,
                'sounds_volume': self.sounds_volume,
                'language': txt.current_language
            }, f)
        log.info("Data has been saved in the options.json file.")

    def _import_data(self):

        with open(self.JSON_PATH, 'r') as f:
            data = json.load(f)
            self.music_volume = data.get('music_volume', 0.5)
            self.sounds_volume = data.get('sounds_volume', 0.25)
            self.current_language = data.get('language', None)

        if not self.current_language in txt.ALL_LANGUAGES:
            txt.set_system_language()
        else:
            txt.current_language = self.current_language
            txt.set_language()

        log.info(
            "Data has been imported from the options.json file."
        )

        self._save()

    def clear(self):
        with open(self.JSON_PATH, 'w') as f:
            json.dump({
                'music_volume': 0.5,
                'sounds_volume': 0.25,
                'language': txt.current_language
            }, f)

        self._import_data()

options_manager = OptionsManager()
