from random import randint, shuffle
import pandas as pd
import numpy as np
import os

from sources.libraries.resource_path import resource_path
from sources.libraries.logger import log

from sources.logic.text_manager import txt
from sources.logic.options_manager import options_manager
class QuestionsManager:
    def __init__(self):
        self.csv_name = 'resources/databases/english.csv'
        self.df = pd.read_csv(resource_path(self.csv_name))
        self.number_of_possibilities = len(self.df)
        self.question = ""
        self.true_answer = ""
        self.wrong_answers = []
        self.image = ""
        self.status = False
        self.current_language = "english"
        self.df_images = pd.read_csv(
            resource_path("resources/databases/images.csv")
        )

        self.question_numbers = []

        for i in range(self.number_of_possibilities):
            self.question_numbers.append(i)

        self.question_numbers_randomized = \
            self.question_numbers.copy()

        shuffle(self.question_numbers_randomized)

        self.question_numbers = [-1] + self.question_numbers

    def replace_ukrainian(self, text_input):
        text = text_input
        text = text.replace("ї","ï").replace("і","i")
        text = text.replace("Ї","Ï").replace("І","I")
        text = text.replace("Є","Е").replace("є","е")
        text = text.replace("Ґ","г").replace("ґ","г")
        return text

    def change_the_language(self):
        self.csv_name = resource_path(
            f'resources/databases/{self.current_language}.csv'
        )
        self.df = pd.read_csv(self.csv_name)
        self.number_of_possibilities = len(self.df)

    def format_text(self, text_input, max_length):
        text = text_input

        text = self.replace_ukrainian(text)
        # Because fonts don't support ukrainian

        try:
            words = text.split(' ')
        except:
            log.info(
                f"In {text} there no spaces. "
                "Can not split this text."
            )
            return text

        wrapped_lines = []
        current_line = []
        current_length = 0

        for word in words:

            if current_length > 0:
                the_space_count = 1

            else:
                the_space_count = 0

            line_length = current_length + \
                len(word) + the_space_count

            if line_length > max_length:
                wrapped_lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)

            else:
                if current_length > 0:
                    current_line.append(word)
                    the_space_count = 1
                else:
                    current_line = [word]
                    the_space_count = 0

                current_length += len(word) + the_space_count

        if current_line:
            wrapped_lines.append(' '.join(current_line))

        return '\n'.join(wrapped_lines)

    def randomize_question(self):

        if txt.current_language != self.current_language:
            self.current_language = txt.current_language
            self.change_the_language()

        if options_manager.randomizing_style == "normal":
            if len(self.question_numbers_randomized) == 0:
                for i in range(self.number_of_possibilities):
                    self.question_numbers_randomized.append(i)

                shuffle(self.question_numbers_randomized)

            self.number_of_the_question = \
                self.question_numbers_randomized[0]

            self.question_numbers_randomized.pop(0)

        elif options_manager.randomizing_style == "alternative":
            self.number_of_the_question = randint(
                0, self.number_of_possibilities - 1
                )

        elif options_manager.randomizing_style == "in_order":
            if len(self.question_numbers) == 0:
                for i in range(self.number_of_possibilities):
                    self.question_numbers.append(i)

            self.number_of_the_question = self.question_numbers[0]

            self.question_numbers.pop(0)

        self.number_of_the_question -= 1
        #! Don't touch this part
        # When we have 100 questions,
        # the 100th index is "out of range"...
        # And I cant fix it.

        self.question = self.df.iloc[
            self.number_of_the_question, 0
            ]

        self.true_answer = self.df.iloc[
            self.number_of_the_question, 1
            ]

        self.wrong_answer1 = self.df.iloc[
            self.number_of_the_question, 2
            ]

        self.wrong_answer2 = self.df.iloc[
            self.number_of_the_question, 3
            ]

        self.wrong_answer3 = self.df.iloc[
            self.number_of_the_question, 4
            ]

        self.image = self.df_images.iloc[
                self.number_of_the_question, 0
            ]

        self.image = resource_path(f'resources/images/{self.image}')

        if not os.path.exists(self.image):
            log.error(
                f"The image path '{self.image}' does not exist!"
            )

            self.image = ""


        self.question = \
            self.format_text(self.question, 35)

        self.true_answer = \
            self.format_text(self.true_answer, 20)

        self.wrong_answer1 = \
            self.format_text(self.wrong_answer1, 20)

        self.wrong_answer2 = self.format_text(
            self.wrong_answer2, 20
        )

        self.wrong_answer3 = self.format_text(
            self.wrong_answer3, 20
        )

        log.info(
            "Randomizing the next question. The arguments are: "
            f"{[self.question, self.true_answer,
            self.wrong_answer1, self.wrong_answer2,
            self.wrong_answer3, self.image]}"
        )

        return (
            self.question, self.true_answer,
            self.wrong_answer1, self.wrong_answer2,
            self.wrong_answer3, self.image
        )

questions_manager = QuestionsManager()
