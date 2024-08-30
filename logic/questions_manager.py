from random import randint, shuffle
import pandas as pd
import numpy as np

from libraries.resource_path import resource_path
from libraries.logger import log

class QuestionsManager:
    def __init__(self):
        self.csv_name = 'databases/english.csv'
        self.df = pd.read_csv(resource_path(self.csv_name))
        self.number_of_possibilities = len(self.df)
        self.randomizing_status = "normal"
        self.question = ""
        self.true_answer = ""
        self.wrong_answers = []
        self.image = ""
        self.status = False
        self.df_images = pd.read_csv(
            resource_path("databases/images.csv")
        )

        self.question_numbers = []

        for i in range(self.number_of_possibilities):
            self.question_numbers.append(i)

        self.question_numbers_randomized = \
            self.question_numbers.copy()

        shuffle(self.question_numbers_randomized)

        self.question_numbers = [-1] + self.question_numbers

    def change_the_language(self, new_language):
        self.csv_name = f'databases/{new_language}.csv'
        self.df = pd.read_csv(resource_path(self.csv_name))
        self.number_of_possibilities = len(self.df)

    def format_text(self, text_input, max_length):
        text = text_input

        text = text.replace("ї","ï").replace("і","i")
        text = text.replace("Ї","Ï").replace("І","I")
        text = text.replace("Є","Е").replace("є","е")
        #todo check the pusab font

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

        if self.randomizing_status == "normal":
            log.debug(self.question_numbers_randomized)
            if len(self.question_numbers_randomized) == 0:
                for i in range(self.number_of_possibilities):
                    self.question_numbers_randomized.append(i)

                shuffle(self.question_numbers_randomized)

            self.number_of_the_question = \
                self.question_numbers_randomized[0]

            self.question_numbers_randomized.pop(0)

        elif self.randomizing_status == "alternative":
            self.number_of_the_question = randint(
                0, self.number_of_possibilities - 1
                )

        elif self.randomizing_status == "in_range":
            if len(self.question_numbers) == 0:
                for i in range(self.number_of_possibilities):
                    self.question_numbers.append(i)

            self.number_of_the_question = self.question_numbers[0]

            self.question_numbers.pop(0)

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

        self.question = \
            self.format_text(self.question, 50)

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

        if isinstance(self.image,
            (float, np.float64)) and np.isnan(self.image):
            self.image = ""
        else:
            self.image = resource_path(f'images/{self.image}')

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
