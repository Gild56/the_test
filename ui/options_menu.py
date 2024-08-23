from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

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
            spacing=8,
            padding=20
        )

        self.left_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8
        )

        self.right_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8
        )

        self.name_label = Label(
            text=txt.name,
            size_hint=(1, 0.3),
            font_size=60,
            font_name=txt.big_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )

        self.clear_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.3, 0.2),
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.big_font,
            halign="center"
        )

        self.return_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(0.5, 0.3),
            background_color=BLUE,
            color=WHITE,
            font_size=64,
            font_name=txt.small_font
        )

        self.update_labels()

        self.clear_button.bind(on_press=self.clear_stats)

        self.return_button.bind(on_press=self.return_in_main_menu)

        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.right_layout)

        self.add_widget(self.main_layout)

    def update_labels(self):
        self.clear_button.text=("")

    def return_in_main_menu(self, instance):
        questions_manager.status = True
        music_manager.button_clicked.play()
        self.manager.current = "MainMenu"
        self.manager.get_screen('MainMenu').update_menu()
        music_manager.transition.play()
        log.info("Going to the next screen - MainMenu.")

    def clear_stats(self, istance):
        music_manager.button_clicked.play()
        points_manager.clear()
        self.update_labels()
        log.info("The stats were succesfully cleared.")