from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

from sources.logic.music_manager import music_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.points_manager import points_manager
from sources.logic.options_manager import options_manager
from sources.logic.text_manager import txt

from sources.libraries.colors import *
from sources.libraries.logger import log

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update_music, 0)

        self.main_layout = BoxLayout(
            orientation = "vertical",
            spacing = 32,
            padding = 32
        )

        self.top_layout = BoxLayout(
            spacing = 0,
            padding = 0
        )

        self.dedications_label = Label(
            text = txt.dedications,
            size_hint = (0.3, 0.3),
            font_size = 25,
            font_name = txt.small_font,
            pos_hint = {"center_x": 0.5, "center_y": 0.8}
        )

        self.name_label = Label(
            text = txt.name,
            size_hint = (1, 0.3),
            font_size = 70,
            font_name = txt.big_font,
            pos_hint = {"center_x": 0.5, "center_y": 0.8}
        )

        self.stats_label = Label(
            size_hint = (0.3, 0.3),
            font_size = 25,
            font_name = txt.small_font,
            pos_hint = {"center_x": 0.5, "center_y": 0.8},
            halign = "right"
        )

        self.options_button = Button(
            pos_hint = {"center_x": 0.5, "center_y": 0.7},
            size_hint = (0.7, 0.5),
            color = WHITE,
            font_size = 50,
            font_name = txt.big_font,
            halign = "center"
        )

        self.play_button = Button(
            pos_hint = {"center_x": 0.5, "center_y": 0.2},
            size_hint = (0.7, 0.5),
            color = WHITE,
            font_size = 64,
            font_name = txt.big_font
        )

        self.update_labels()

        self.options_button.bind(on_press = self.open_options)

        self.play_button.bind(on_press = self.start_game)

        self.top_layout.add_widget(self.dedications_label)
        self.top_layout.add_widget(self.name_label)
        self.top_layout.add_widget(self.stats_label)
        self.main_layout.add_widget(self.top_layout)
        self.main_layout.add_widget(self.options_button)
        self.main_layout.add_widget(self.play_button)

        self.add_widget(self.main_layout)

    def update_music(self, dt):
        music_manager.check_music()

        music_manager.transition.volume = options_manager.sounds_volume
        music_manager.button_clicked.volume = options_manager.sounds_volume
        music_manager.win.volume = options_manager.sounds_volume
        music_manager.lose.volume = options_manager.sounds_volume

        if music_manager.current_music:
            music_manager.current_music.volume = options_manager.music_volume

    def update_labels(self):
        self.stats_label.text = (
        f"{txt.points}: {points_manager.points}\n"
        f" {txt.win_streak}: {points_manager.win_streak}\n"
        f" {txt.best_win_streak}: {points_manager.best_win_streak}"
        )

        self.play_button.text = txt.play
        self.options_button.text = txt.options
        self.name_label.text = txt.name
        self.dedications_label.text = txt.dedications

        self.play_button.background_color = \
            options_manager.main_color

        self.options_button.background_color = \
            options_manager.main_color

    def start_game(self, instance):
        questions_manager.status = True
        music_manager.button_clicked.play()
        self.manager.current = "QuestionMenu"
        self.manager.get_screen('QuestionMenu').update_menu()
        music_manager.transition.play()
        log.info("Going to the next screen -> QuestionMenu.")

    def open_options(self, instance):
        self.manager.current = "OptionsMenu"
        music_manager.transition.play()
        music_manager.button_clicked.play()
        log.info("Going to the next screen -> OptionsMenu.")
        self.manager.get_screen('OptionsMenu').update_labels()
        self.manager.get_screen('OptionsMenu').update_menu()
