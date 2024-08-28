import locale

from logic.questions_manager import questions_manager

from libraries.resource_path import resource_path
from libraries.logger import log

from languages.en_texts import *
from languages.fr_texts import *
from languages.ru_texts import *
from languages.ua_texts import *

class TextManager():

    def __init__(self):

        self.current_language = 'english'

        self.big_font = resource_path("fonts/big_font.ttf")
        self.small_font = resource_path("fonts/small_font.ttf")

        self.good_answers = []
        self.wrong_answers = []
        self.keep_it_messages = []
        self.dedications = ""
        self.name = ""
        self.points = ""
        self.win_streak = ""
        self.best_win_streak = ""
        self.clear_stats = ""
        self.warning_message = ""
        self.play = ""
        self.next = ""
        self.main_menu = ""
        self.correct_answer = ""
        self.options = ""

        self.system_language, _ = locale.getlocale()
        log.info(f"The system language is {self.system_language}.")
        self.system_language = self.system_language.lower()

        if 'ru' in self.system_language:
            self.change_of_language('russian')

        elif 'fr' in self.system_language:
            self.change_of_language('french')

        elif 'ukr' in self.system_language or \
            'ua' in self.system_language:
            self.change_of_language('ukrainian')

        else:
            self.change_of_language('english')

    def set_english(self):
        log.info("The language was changed into english.")

        self.good_answers = GOOD_ANSWERS_ENGLISH
        self.wrong_answers = WRONG_ANSWERS_ENGLISH
        self.keep_it_messages = KEEP_IT_MESSAGES_ENGLISH

        self.dedications = DEDICATIONS_ENGLISH
        self.name = NAME_ENGLISH
        self.points = POINTS_ENGLISH
        self.win_streak = WIN_STREAK_ENGLISH
        self.best_win_streak = BEST_WIN_STREAK_ENGLISH
        self.clear_stats = CLEAR_STATS_ENGLISH
        self.play = PLAY_ENGLISH
        self.next = NEXT_ENGLISH
        self.main_menu = MAIN_MENU_ENGLISH
        self.correct_answer = CORRECT_ANSWER_ENGLISH
        self.options = OPTIONS_ENGLISH
        self.change_language = CHANGE_LANGUAGE_ENGLISH
        self.warning_message = WARNING_MESSAGE_ENGLISH


    def set_russian(self):
        log.info("The language was changed into russian.")

        self.good_answers = GOOD_ANSWERS_RUSSIAN
        self.wrong_answers = WRONG_ANSWERS_RUSSIAN
        self.keep_it_messages = KEEP_IT_MESSAGES_RUSSIAN

        self.dedications = DEDICATIONS_RUSSIAN
        self.name = NAME_RUSSIAN
        self.points = POINTS_RUSSIAN
        self.win_streak = WIN_STREAK_RUSSIAN
        self.best_win_streak = BEST_WIN_STREAK_RUSSIAN
        self.clear_stats = CLEAR_STATS_RUSSIAN
        self.play = PLAY_RUSSIAN
        self.next = NEXT_RUSSIAN
        self.main_menu = MAIN_MENU_RUSSIAN
        self.correct_answer = CORRECT_ANSWER_RUSSIAN
        self.options = OPTIONS_RUSSIAN
        self.change_language = CHANGE_LANGUAGE_RUSSIAN
        self.warning_message = WARNING_MESSAGE_RUSSIAN


    def set_french(self):
        log.info("The language was changed into french.")

        self.good_answers = GOOD_ANSWERS_FRENCH
        self.wrong_answers = WRONG_ANSWERS_FRENCH
        self.keep_it_messages = KEEP_IT_MESSAGES_FRENCH

        self.dedications = DEDICATIONS_FRENCH
        self.name = NAME_FRENCH
        self.points = POINTS_FRENCH
        self.win_streak = WIN_STREAK_FRENCH
        self.best_win_streak = BEST_WIN_STREAK_FRENCH
        self.clear_stats = CLEAR_STATS_FRENCH
        self.play = PLAY_FRENCH
        self.next = NEXT_FRENCH
        self.main_menu = MAIN_MENU_FRENCH
        self.correct_answer = CORRECT_ANSWER_FRENCH
        self.options = OPTIONS_FRENCH
        self.change_language = CHANGE_LANGUAGE_FRENCH
        self.warning_message = WARNING_MESSAGE_FRENCH


    def set_ukrainian(self):
        log.info("The language was changed into ukrainian.")

        self.good_answers = GOOD_ANSWERS_UKRAINIAN
        self.wrong_answers = WRONG_ANSWERS_UKRAINIAN
        self.keep_it_messages = KEEP_IT_MESSAGES_UKRAINIAN

        self.dedications = DEDICATIONS_UKRAINIAN
        self.name = NAME_UKRAINIAN
        self.points = POINTS_UKRAINIAN
        self.win_streak = WIN_STREAK_UKRAINIAN
        self.best_win_streak = BEST_WIN_STREAK_UKRAINIAN
        self.clear_stats = CLEAR_STATS_UKRAINIAN
        self.play = PLAY_UKRAINIAN
        self.next = NEXT_UKRAINIAN
        self.main_menu = MAIN_MENU_UKRAINIAN
        self.correct_answer = CORRECT_ANSWER_UKRAINIAN
        self.options = OPTIONS_UKRAINIAN
        self.change_language = CHANGE_LANGUAGE_UKRAINIAN
        self.warning_message = WARNING_MESSAGE_UKRAINIAN


    def change_of_language(self, next_language=None):
        if next_language == 'english':
            self.current_language = next_language
            self.set_english()

        elif next_language == 'russian':
            self.current_language = next_language
            self.set_russian()

        elif next_language == 'french':
            self.current_language = next_language
            self.set_french()

        elif next_language == 'ukrainian':
            self.current_language = next_language
            self.set_ukrainian()

        questions_manager.change_the_language(self.current_language)


    def next_language(self):
        if self.current_language == 'english':
            self.set_russian()
            self.current_language = 'russian'

        elif self.current_language == 'russian':
            self.set_french()
            self.current_language = 'french'

        elif self.current_language == 'french':
            self.set_ukrainian()
            self.current_language = 'ukrainian'

        else:
            self.set_english()
            self.current_language = 'english'

        questions_manager.change_the_language(self.current_language)

txt = TextManager()
