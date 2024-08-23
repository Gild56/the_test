from kivy.logger import Logger
from logging import CRITICAL

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from ui.main_menu import MainMenu
from ui.question_menu import QuestionMenu
from ui.answered_menu import AnsweredMenu
from ui.options_menu import OptionsMenu

from libraries.colors import *
from libraries.logger import log

from logic.music_manager import music_manager
from logic.points_manager import points_manager
from logic.questions_manager import questions_manager
from logic.text_manager import txt

Logger.setLevel(CRITICAL)

Window.clearcolor = DARK_BLUE

music_manager.play_music()

#txt.change_of_language("ukrainien")

class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='MainMenu'))
        sm.add_widget(QuestionMenu(name='QuestionMenu'))
        sm.add_widget(AnsweredMenu(name='AnsweredMenu'))
        sm.add_widget(OptionsMenu(name='OptionsMenu'))
        return sm

    def on_stop(self):
        log.info("Stopping the app...")
        if questions_manager.status:
            points_manager.lose()
            log.info(
                "The app stopped when a question "
                "was asked. Points were lost."
                )

if __name__ == '__main__':
    QuizApp().run()
