from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

from random import choice

from logic.music_manager import music_manager
from logic.points_manager import points_manager
from logic.text_manager import txt

from libraries.colors import *
from libraries.logger import log

class AnsweredMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=20
        )

        self.top_text = Label(
            size_hint=(1, 0.3),
            font_size=96,
            font_name=txt.big_font
        )

        self.bottom_text = Label(
            size_hint=(1, 0.3),
            font_size=64,
            font_name=txt.small_font
        )

        self.stats_label = Label(
            size_hint=(0.3, 0.3),
            font_size=32,
            font_name=txt.small_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            halign="center"
        )

        self.exit_button = Button(
            text=txt.main_menu,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint=(0.3, 0.15),
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            halign="center"
        )

        self.next_screen_button = Button(
            text=txt.next,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.4, 0.15),
            background_color=BLUE,
            color=WHITE,
            font_size=64,
            font_name=txt.big_font
        )

        self.next_screen_button.bind(on_press=self.next_screen)
        self.exit_button.bind(on_press=self.exit_to_main_menu)

        self.main_layout.add_widget(self.top_text)
        self.main_layout.add_widget(self.bottom_text)
        self.main_layout.add_widget(self.stats_label)
        self.main_layout.add_widget(self.exit_button)
        self.main_layout.add_widget(self.next_screen_button)

        self.add_widget(self.main_layout)

    def update_labels(self, is_correct):
        if is_correct:
            self.top_text.text = choice(txt.good_answers)
            self.bottom_text.text = choice(txt.keep_it_messages)
            Window.clearcolor = DARK_GREEN
            self.exit_button.background_color = GREEN
            self.next_screen_button.background_color = GREEN

        else:
            Window.clearcolor = DARK_RED
            self.exit_button.background_color = RED
            self.next_screen_button.background_color = RED
            self.top_text.text = choice(txt.wrong_answers)
            self.bottom_text.text = (
                f'{txt.correct_answer}: '
                f'"{self.manager.get_screen('QuestionMenu').true_answer}".'
            )

            self.stats_label.text=(
                f"{txt.points}: {points_manager.points}\n "
                f"{txt.win_streak}: {points_manager.win_streak}\n "
                f"{txt.best_win_streak}: {points_manager.best_win_streak}"
            )

    def next_screen(self, instance):
        music_manager.button_clicked.play()
        self.manager.current = "QuestionMenu"
        self.manager.get_screen('QuestionMenu').update_menu()
        music_manager.transition.play()
        Window.clearcolor = DARK_BLUE
        log.info("Going to the next screen - QuestionMenu.")

    def exit_to_main_menu(self, instance):
        music_manager.button_clicked.play()
        self.manager.current = "MainMenu"
        self.manager.get_screen('MainMenu').update_labels()
        Window.clearcolor = DARK_BLUE
        log.info("Going to the next screen - MainMenu.")
