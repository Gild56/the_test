from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

from logic.music_manager import music_manager
from logic.options_manager import options_manager
from logic.points_manager import points_manager
from logic.questions_manager import questions_manager
from logic.text_manager import txt

from libraries.colors import *
from libraries.logger import log

class OptionsMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(
            spacing=32,
            padding=32
        )

        self.left_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.right_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.reset_settings_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(1, 0.1),
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            halign="center"
        )

        self.clear_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(1, 0.1),
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font
        )

        self.return_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(1, 0.1),
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font
        )

        self.update_labels()

        self.clear_button.bind(on_press=self.clear_stats)
        self.reset_settings_button.bind(on_press=self.reset_settings)
        self.return_button.bind(on_press=self.return_in_main_menu)

        self.left_layout.add_widget(self.reset_settings_button)
        self.left_layout.add_widget(self.clear_button)
        self.left_layout.add_widget(self.return_button)

        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.right_layout)

        self.add_widget(self.main_layout)


    def update_labels(self):
        self.reset_settings_button.text=(txt.reset_settings)
        self.clear_button.text=(txt.clear_stats)
        self.return_button.text=(txt.main_menu)


    def reset_settings(self, instance):
        options_manager.clear()
        txt.set_system_language()
        self.update_labels()
        music_manager.button_clicked.play()


    def return_in_main_menu(self, instance):
        questions_manager.status = True
        options_manager._save()

        music_manager.button_clicked.play()
        music_manager.transition.play()

        self.manager.current = "MainMenu"
        self.manager.get_screen('MainMenu').update_labels()
        log.info("Going to the next screen -> MainMenu.")


    def clear_stats(self, instance):
        music_manager.button_clicked.play()
        points_manager.clear()
