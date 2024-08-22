import locale

from logic.questions_manager import questions_manager
from logic.texts import *

from libraries.resource_path import resource_path
from libraries.logs import log

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

        if 'ru' in self.system_language:
            self.change_of_language('russian')

        elif 'fr' in self.system_language:
            self.change_of_language('french')

        elif 'uk' in self.system_language or 'ua' in self.system_language or "Uk" in self.system_language:
            self.change_of_language('ukrainien')

    def set_english(self):

        self.good_answers = GOOD_ANSWERS_ENGLISH
        self.wrong_answers = WRONG_ANSWERS_ENGLISH
        self.keep_it_messages = KEEP_IT_MESSAGES_ENGLISH

        self.dedications = "A game made by\nGild56 // @gild56gmd\nEnjoy!"
        self.name = "IQ Test"
        self.points = "points"
        self.win_streak = "your win streak now"
        self.best_win_streak = "best win streak"
        self.clear_stats = "Clear stats"
        self.play = "Play"
        self.next = "Continue"
        self.main_menu = "<-- Main menu"
        self.correct_answer = "The correct answer was"
        self.options = "Options"

        self.warning_message = (
            "WARNING!\nAfter doing this you won't be able to\n"
            "return to the previous stats."
        )

    def set_russian(self):

        self.good_answers = GOOD_ANSWERS_RUSSIAN
        self.wrong_answers = WRONG_ANSWERS_RUSSIAN
        self.keep_it_messages = KEEP_IT_MESSAGES_RUSSIAN

        self.dedications = "Игра от\nGild56 // @gild56gmd\nПриятной игры!"
        self.name = "IQ Тест"
        self.points = "очков"
        self.win_streak = "текущая серия правильных ответов"
        self.best_win_streak = "лучшая серия правильных ответов"
        self.clear_stats = "Очистить статистику"
        self.play = "Играть"
        self.next = "Дальше"
        self.main_menu = "<-- Главное меню"
        self.correct_answer = "Правильный ответ"
        self.options = "Настройки"

        self.warning_message = (
            "Осторожно!\nПосле этого нельзя\n"
            "вернуть предыдущие данные."
        )

    def set_french(self):

        self.good_answers = GOOD_ANSWERS_FRENCH
        self.wrong_answers = WRONG_ANSWERS_FRENCH
        self.keep_it_messages = KEEP_IT_MESSAGES_FRENCH

        self.dedications = "Jeu de\nGild56 // @gild56gmd\nAmusez-vous bien!"
        self.name = "Test de QI"
        self.points = "points"
        self.win_streak = "ta série actuelle"
        self.best_win_streak = "meilleure série"
        self.clear_stats = "Réinitialiser"
        self.play = "Jouer"
        self.next = "Continuer"
        self.main_menu = "<-- Menu principal"
        self.correct_answer = "La réponse correcte était"
        self.options = "Paramètres"

        self.warning_message = (
            "AVERTISSEMENT!\nAprès cela, tu ne pourras pas\n"
            "retourner aux statistiques précédentes."
        )

    def set_ukrainien(self):

        self.good_answers = GOOD_ANSWERS_UKRAINIEN
        self.wrong_answers = WRONG_ANSWERS_UKRAINIEN
        self.keep_it_messages = KEEP_IT_MESSAGES_UKRAINIEN

        self.dedications = "Гра вiд\nGild56 // @gild56gmd\nГарноï гри!"
        self.name = "IQ Тест"
        self.points = "очок"
        self.win_streak = "твоя поточна серiя"
        self.best_win_streak = "твоя найкраща серiя"
        self.clear_stats = "Очистити статистику"
        self.play = "Грати"
        self.next = "Далi"
        self.main_menu = "<-- Головне меню"
        self.correct_answer = "Правильна вiдповiдь була"
        self.options = ""

        self.warning_message = (
            "ОБЕРЕЖНО!\nПiсля цього неможливо\n"
            "повернутися до попереднiх даних."
        )

    def change_of_language(self, next_language=None):

        if next_language == 'english':
            self.current_language = next_language
            self.set_english()
            return

        elif next_language == 'russian':
            self.current_language = next_language
            self.set_russian()
            return

        elif next_language == 'french':
            self.current_language = next_language
            self.set_french()
            return

        elif next_language == 'ukrainien':
            self.current_language = next_language
            self.set_ukrainien()
            return


        if self.current_language == 'english':
            self.set_russian()
            self.current_language = 'russian'

        elif self.current_language == 'russian':
            self.set_french()
            self.current_language = 'french'

        elif self.current_language == 'french':
            self.set_ukrainien()
            self.current_language = 'ukrainien'

        else:
            self.set_english()
            self.current_language = 'english'

        questions_manager.change_the_language(self.current_language)

txt = TextManager()
