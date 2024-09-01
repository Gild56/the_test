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
        self.menus_color = "blue"
        self.drawing_images = True
        self.randomizing_style = "normal"
        self.rainbow_buttons = False

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
                'language': txt.current_language,
                'menus_color': self.menus_color,
                'drawing_images': self.drawing_images,
                'randomizing_style': self.randomizing_style,
                'rainbow_buttons': self.rainbow_buttons
            }, f)
        log.info("Data has been saved in the options.json file.")

    def _import_data(self):

        with open(self.JSON_PATH, 'r') as f:
            data = json.load(f)
            self.music_volume = data.get('music_volume', 0.5)
            self.sounds_volume = data.get('sounds_volume', 0.25)
            self.current_language = data.get('language', None)
            self.menus_color = data.get('menus_color', "blue")
            self.drawing_images = data.get('drawing_images', True)
            self.randomizing_style = data.get('randomizing_style', "normal")
            self.rainbow_buttons = data.get('rainbow_buttons', False)

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
        txt.set_system_language()
        with open(self.JSON_PATH, 'w') as f:
            json.dump({
                'music_volume': 0.5,
                'sounds_volume': 0.25,
                'language': txt.current_language,
                'menus_color': "blue",
                'drawing_images': True,
                'randomizing_style': 'normal',
                'rainbow_buttons': False
            }, f)

        self._save()

        self._import_data()

options_manager = OptionsManager()
