import os, json

from kivy.core.window import Window

from libraries.resource_path import resource_path
from libraries.logger import log

from logic.text_manager import txt

from libraries.colors import *

class OptionsManager():
    def __init__(self):
        self.music_volume = 0.5
        self.sounds_volume = 0.25
        self.menus_color = "blue"
        self.drawing_images = True
        self.randomizing_style = "normal"
        self.rainbow_buttons = False
        self.main_color = LIGHT_BLUE
        self.bg_color = DARK_BLUE

        self.RANDOMIZING_STYLES = [
            "normal", "alternative", "in_range"
        ]

        self.COLORS = [
            "blue", "orange",
            "violet", "pink",
            "yellow", "cyan",
            "grey", "black"
        ]

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
        self._import_data()


    def save(self):

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
            self.randomizing_style = data.get(
                'randomizing_style', "normal"
            )
            self.rainbow_buttons = data.get('rainbow_buttons', False)

        int(self.music_volume)
        int(self.sounds_volume)

        self.current_language.lower()
        self.randomizing_style.lower()

        if self.menus_color not in self.COLORS:
            self.menus_color = "blue"

        if self.music_volume > 1:
            self.music_volume = 1
        elif self.music_volume < 0:
            self.music_volume = 0

        if self.sounds_volume > 1:
            self.sounds_volume = 1
        elif self.sounds_volume < 0:
            self.sounds_volume = 0

        if self.randomizing_style not in self.RANDOMIZING_STYLES:
            self.randomizing_style = "normal"

        self.color_change()

        if self.drawing_images not in [True, False]:
            self.drawing_images = True

        if self.rainbow_buttons not in [True, False]:
            self.rainbow_buttons = False

        if not self.current_language in txt.ALL_LANGUAGES:
            txt.set_system_language()
        else:
            txt.current_language = self.current_language
            txt.set_language()

        log.info(
            "Data has been imported from the options.json file."
        )

        self.save()

    def color_change(self):

        if self.menus_color == "blue":
            self.main_color = LIGHT_BLUE
            self.bg_color = DARK_BLUE

        elif self.menus_color == "orange":
            self.main_color = LIGHT_ORANGE
            self.bg_color = DARK_ORANGE

        elif self.menus_color == "violet":
            self.main_color = LIGHT_VIOLET
            self.bg_color = DARK_VIOLET

        elif self.menus_color == "pink":
            self.main_color = PINK
            self.bg_color = DARK_PINK

        elif self.menus_color == "yellow":
            self.main_color = YELLOW
            self.bg_color = DARK_YELLOW

        elif self.menus_color == "cyan":
            self.main_color = LIGHT_CYAN
            self.bg_color = CYAN

        elif self.menus_color == "grey":
            self.main_color = LIGHT_GREY
            self.bg_color = DARK_GREY

        elif self.menus_color == "black":
            self.main_color = DARK_GREY
            self.bg_color = BLACK

        Window.clearcolor = self.bg_color

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

        log.info(
            "The options data has been cleared."
        )

        self._import_data()

options_manager = OptionsManager()
