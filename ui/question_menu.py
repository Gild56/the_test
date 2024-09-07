from random import randint

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from logic.music_manager import music_manager
from logic.questions_manager import questions_manager
from logic.points_manager import points_manager
from logic.options_manager import options_manager
from logic.text_manager import txt

from libraries.resource_path import resource_path
from libraries.colors import *
from libraries.logger import log

class QuestionMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.image = None
        self.previous_image = None

        self.update_variables()

        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.image_layout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            spacing=64,
            padding=64
        )

        self.question_text = Label(
            font_size=48,
            font_name=txt.big_font,
            halign="center"
        )

        self.top_answers_layout = BoxLayout(
            spacing=32,
            padding=32,
            size_hint_y=None
        )

        self.bottom_answers_layout = BoxLayout(
            spacing=32,
            padding=32,
            size_hint_y=None
        )

        self.true_button = Button(
            background_color=options_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.wrong_button1 = Button(
            background_color=options_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.wrong_button2 = Button(
            background_color=options_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.wrong_button3 = Button(
            background_color=options_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.main_layout.add_widget(self.question_text)
        self.main_layout.add_widget(self.image_layout)
        self.main_layout.add_widget(self.top_answers_layout)
        self.main_layout.add_widget(self.bottom_answers_layout)

        self.add_widget(self.main_layout)

        self.true_button.bind(on_press=self.check_answer)
        self.wrong_button1.bind(on_press=self.check_answer)
        self.wrong_button2.bind(on_press=self.check_answer)
        self.wrong_button3.bind(on_press=self.check_answer)

    def update_variables(self):
        (
        self.question, self.true_answer,
        self.wrong_answer1, self.wrong_answer2, self.wrong_answer3,
        self.image_path
        ) = questions_manager.randomize_question()

        if options_manager.drawing_images:

            if self.image_path == None or self.image_path == "":
                self.image = None
                log.warning(
                    "There are no image for this question. "
                    "The image wasn't created."
                )

            elif not self.image_path.strip(): #
                self.image = None
                log.warning(
                    "There are no image "
                    f"with the '{self.image_path}' path. "
                    "The image wasn't created."
                )

            else: #self.image_path and self.image_path.strip()
                self.image = Image(
                    source=resource_path(self.image_path),
                    size_hint_y=None,
                    height=200
                )
                log.info(
                    "The image was created. "
                    f"The path do the image is '{self.image_path}'."
                )

        else:
            self.image = None

    def update_question(self):
        self.question_text.text = self.question
        self.true_button.text = self.true_answer
        self.wrong_button1.text = self.wrong_answer1
        self.wrong_button2.text = self.wrong_answer2
        self.wrong_button3.text = self.wrong_answer3

        self.image_layout.clear_widgets()
        self.top_answers_layout.clear_widgets()
        self.bottom_answers_layout.clear_widgets()

        if options_manager.drawing_images:
            if self.image:
                if self.previous_image:
                    self.image_layout.remove_widget(
                        self.previous_image
                    )
                self.image_layout.add_widget(self.image)
                self.previous_image = self.image
                log.info(
                    "The image was added to the layout. "
                    f"The path do the image is '{self.image_path}'."
                    )
            else:
                if self.previous_image:
                    self.image_layout.remove_widget(
                        self.previous_image
                    )
                    self.previous_image = None
                log.warning(
                    "There are no image for this question. "
                    "The image wasn't added to the layout."
                )

        r = randint(1, 4)
        if r == 1:
            self.top_answers_layout.add_widget(self.true_button)
            self.top_answers_layout.add_widget(self.wrong_button1)
            self.bottom_answers_layout.add_widget(self.wrong_button2)
            self.bottom_answers_layout.add_widget(self.wrong_button3)

            if options_manager.rainbow_buttons:
                self.true_button.background_color = LIGHT_RED
                self.wrong_button1.background_color = LIGHT_YELLOW
                self.wrong_button2.background_color = LIGHT_GREEN
                self.wrong_button3.background_color = LIGHT_CYAN

        elif r == 2:
            self.top_answers_layout.add_widget(self.wrong_button3)
            self.top_answers_layout.add_widget(self.true_button)
            self.bottom_answers_layout.add_widget(self.wrong_button1)
            self.bottom_answers_layout.add_widget(self.wrong_button2)

            if options_manager.rainbow_buttons:
                self.wrong_button3.background_color = LIGHT_RED
                self.true_button.background_color = LIGHT_YELLOW
                self.wrong_button1.background_color = LIGHT_GREEN
                self.wrong_button2.background_color = LIGHT_CYAN

        elif r == 3:
            self.top_answers_layout.add_widget(self.wrong_button2)
            self.top_answers_layout.add_widget(self.wrong_button3)
            self.bottom_answers_layout.add_widget(self.true_button)
            self.bottom_answers_layout.add_widget(self.wrong_button1)

            if options_manager.rainbow_buttons:
                self.wrong_button2.background_color = LIGHT_RED
                self.wrong_button3.background_color = LIGHT_YELLOW
                self.true_button.background_color = LIGHT_GREEN
                self.wrong_button1.background_color = LIGHT_CYAN

        else:
            self.top_answers_layout.add_widget(self.wrong_button1)
            self.top_answers_layout.add_widget(self.wrong_button2)
            self.bottom_answers_layout.add_widget(self.wrong_button3)
            self.bottom_answers_layout.add_widget(self.true_button)

            if options_manager.rainbow_buttons:
                self.wrong_button1.background_color = LIGHT_RED
                self.wrong_button2.background_color = LIGHT_YELLOW
                self.wrong_button3.background_color = LIGHT_GREEN
                self.true_button.background_color = LIGHT_CYAN

        if not options_manager.rainbow_buttons:
            self.true_button.background_color = \
                options_manager.main_color

            self.wrong_button1.background_color = \
                options_manager.main_color

            self.wrong_button2.background_color = \
                options_manager.main_color

            self.wrong_button3.background_color = \
                options_manager.main_color


    def update_menu(self):
        self.update_variables()
        self.update_question()

    def check_answer(self, instance):
        music_manager.button_clicked.play()
        if instance.text == questions_manager.true_answer:
            points_manager.win()
            win = True
            music_manager.win.play()
        else:
            points_manager.lose()
            win = False
            music_manager.lose.play()

        self.manager.current = "AnsweredMenu"
        self.manager.get_screen("AnsweredMenu").update_labels(win)
        questions_manager.status = False
        music_manager.transition.play()

        log.info(f"The answer was {str(win).lower()}.")
        log.info("Going to the next screen -> AnsweredMenu.")