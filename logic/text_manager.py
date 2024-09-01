import locale

from libraries.resource_path import resource_path
from libraries.logger import log

import languages.en_texts
import languages.fr_texts
import languages.ru_texts
import languages.ua_texts

class TextManager():

    def __init__(self):

        self.ALL_LANGUAGES = [
            'english','french','russian','ukrainian'
        ]

        self.current_language = None

        self.big_font = resource_path("fonts/big_font.ttf")
        self.small_font = resource_path("fonts/small_font.ttf")

        self.labels = None

    def set_system_language(self):
        self.system_language, _ = locale.getlocale()
        log.info(f"The system language is {self.system_language}.")
        self.system_language = self.system_language.lower()

        if 'ru' in self.system_language:
            self.set_language('russian')

        elif 'fr' in self.system_language:
            self.set_language('french')

        elif 'ukr' in self.system_language or \
            'ua' in self.system_language:
            self.set_language('ukrainian')

        else:
            self.set_language('english')

    def set_language(self, next_language_input=None):

        if next_language_input == None:
            next_language = self.current_language
        else:
            next_language = next_language_input

        if next_language == 'english':
            self.current_language = next_language
            self.labels = languages.en_texts.labels
            log.info(
                "The language was changed into english."
            )

        elif next_language == 'russian':
            self.current_language = next_language
            self.labels = languages.ru_texts.labels
            log.info(
                "The language was changed into russian."
            )

        elif next_language == 'french':
            self.current_language = next_language
            self.labels = languages.fr_texts.labels
            log.info(
                "The language was changed into french."
            )

        elif next_language == 'ukrainian':
            self.current_language = next_language
            self.labels = languages.ua_texts.labels
            log.info(
                "The language was changed into ukrainian."
            )

        (
            self.good_answers,
            self.wrong_answers,
            self.keep_it_messages,
            self.dedications,
            self.name,
            self.points,
            self.win_streak,
            self.best_win_streak,
            self.clear_stats,
            self.play,
            self.next,
            self.main_menu,
            self.correct_answer,
            self.options,
            self.warning_message,
            self.reset_settings
        ) = self.labels

txt = TextManager()
