from random import randint

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from logic.music_manager import music_manager
from logic.questions_manager import questions_manager
from logic.points_manager import points_manager
from logic.text_manager import txt

from libraries.resource_path import resource_path
from libraries.colors import *
from libraries.logs import log

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

        button_height = 3
        self.true_button = Button(
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, None),
            size_hint_y=button_height,
        )

        self.wrongbutton1 = Button(
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, None),
            size_hint_y=button_height,
        )

        self.wrongbutton2 = Button(
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, None),
            size_hint_y=button_height,
        )

        self.wrongbutton3 = Button(
            background_color=BLUE,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, None),
            size_hint_y=button_height,
        )

        self.main_layout.add_widget(self.question_text)
        self.main_layout.add_widget(self.image_layout)
        self.main_layout.add_widget(self.top_answers_layout)
        self.main_layout.add_widget(self.bottom_answers_layout)

        self.add_widget(self.main_layout)

        self.true_button.bind(on_press=self.check_answer)
        self.wrongbutton1.bind(on_press=self.check_answer)
        self.wrongbutton2.bind(on_press=self.check_answer)
        self.wrongbutton3.bind(on_press=self.check_answer)

    def update_variables(self):
        (
        self.question, self.true_answer,
        self.wrong_answer1, self.wrong_answer2, self.wrong_answer3,
        self.image_path
        ) = questions_manager.randomize_question()

        if self.image_path and self.image_path.strip():
            self.image = Image(
                source=resource_path(self.image_path),
                size_hint_y=None,
                height=200
            )

            log.info(
                "The image was created. "
                f"The path do the image is '{self.image_path}'."
            )

        elif self.image_path == None or self.image_path == "":
            self.image = None
            log.warning(
                "There are no image for this question. "
                "The image wasn't created."
            )

        else: #not self.image_path.strip()
            self.image = None
            log.warning(
                "There are no image "
                f"with the '{self.image_path}' path. "
                "The image wasn't created."
            )

    def update_question(self):
        self.question_text.text = self.question
        self.true_button.text = self.true_answer
        self.wrongbutton1.text = self.wrong_answer1
        self.wrongbutton2.text = self.wrong_answer2
        self.wrongbutton3.text = self.wrong_answer3

        self.image_layout.clear_widgets()
        self.top_answers_layout.clear_widgets()
        self.bottom_answers_layout.clear_widgets()

        if self.image:
            if self.previous_image:
                self.image_layout.remove_widget(self.previous_image)
            self.image_layout.add_widget(self.image)
            self.previous_image = self.image
            log.info(
                "The image was added to the layout. "
                f"The path do the image is '{self.image_path}'."
                )
        else:
            if self.previous_image:
                self.image_layout.remove_widget(self.previous_image)
                self.previous_image = None
            log.warning(
                "There are no image for this question. "
                "The image wasn't added to the layout."
                )

        r = randint(1, 4)
        if r == 1:
            self.top_answers_layout.add_widget(self.true_button)
            self.top_answers_layout.add_widget(self.wrongbutton1)
            self.bottom_answers_layout.add_widget(self.wrongbutton2)
            self.bottom_answers_layout.add_widget(self.wrongbutton3)
        elif r == 2:
            self.top_answers_layout.add_widget(self.wrongbutton3)
            self.top_answers_layout.add_widget(self.true_button)
            self.bottom_answers_layout.add_widget(self.wrongbutton1)
            self.bottom_answers_layout.add_widget(self.wrongbutton2)
        elif r == 3:
            self.top_answers_layout.add_widget(self.wrongbutton2)
            self.top_answers_layout.add_widget(self.wrongbutton3)
            self.bottom_answers_layout.add_widget(self.true_button)
            self.bottom_answers_layout.add_widget(self.wrongbutton1)
        else:
            self.top_answers_layout.add_widget(self.wrongbutton1)
            self.top_answers_layout.add_widget(self.wrongbutton2)
            self.bottom_answers_layout.add_widget(self.wrongbutton3)
            self.bottom_answers_layout.add_widget(self.true_button)

    def update_menu(self):
        self.update_variables()
        self.update_question()

    def check_answer(self, instance):
        music_manager.button_clicked.play()
        if instance.text == questions_manager.true_answer:
            points_manager.win()
            win = True
        else:
            points_manager.lose()
            win = False

        self.manager.current = "AnsweredMenu"
        self.manager.get_screen("AnsweredMenu").update_labels(win)
        questions_manager.status = False
        music_manager.transition.play()

        log.info(f"The answer was {str(win).lower()}.")
        log.info("Going to the next screen - AnsweredMenu.")