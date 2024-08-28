from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ui.main_menu import MainMenu
from ui.question_menu import QuestionMenu
from ui.answered_menu import AnsweredMenu
from ui.options_menu import OptionsMenu

from libraries.colors import *
from libraries.logger import log

from logic.points_manager import points_manager
from logic.questions_manager import questions_manager

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
            log.info(
                "The app stopped when a question "
                "was asked. Points were lost."
                )
            points_manager.lose()

if __name__ == '__main__':
    QuizApp().run()
