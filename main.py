from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from sources.ui.main_menu import MainMenu
from sources.ui.question_menu import QuestionMenu
from sources.ui.answered_menu import AnsweredMenu
from sources.ui.options_menu import OptionsMenu

from sources.libraries.colors import *
from sources.libraries.logger import log

from sources.logic.points_manager import points_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.options_manager import options_manager

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
        options_manager.save()
        if questions_manager.status:
            log.info(
                "The app stopped when a question "
                "was asked. Points were lost."
            )
            points_manager.lose()

if __name__ == '__main__':
    QuizApp().run()
