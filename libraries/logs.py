import sys
import os
import time
import traceback
import inspect

from libraries.colors import *
from libraries.resource_path import resource_path

class Logs:

    def __init__(self, collecting_errors=True, filename="info.log"):
        self.FILE = resource_path(filename)
        self.info_text = ""
        self.warning_text = ""
        self.error_text = ""
        self.MAX_SPACES = 30
        self.MAX_LINE_LENGTH = 70
        self.info("The app is starting...")

        self.project_root = os.path.dirname(os.path.abspath(__file__))

        if collecting_errors:
            sys.excepthook = self.error_collector


    def get_time(self):
        current_time = time.localtime()
        return time.strftime("%H:%M:%S", current_time)


    def add_log(self, text):
        with open(self.FILE, "a", encoding="utf8") as f:
            f.write(text + "\n")


    def format_filename(self, filename):
        rel_path = os.path.relpath(filename, os.path.abspath(os.path.dirname(__file__)))
        return rel_path


    def warn(self, text):
        self.warning(text)


    def format_line(self, text):
        if len(text) > self.MAX_LINE_LENGTH:
            return text[:self.MAX_LINE_LENGTH] + '...'
        return text


    def debug(self, text="Debug text wasn't added!"):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = self.format_filename(caller_frame.f_code.co_filename)

        spaces_count = self.MAX_SPACES - len(filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        self.debug_text = f"[DEBUG] [{self.get_time()}] [{filename}]{spaces} {self.format_line(text)}"

        print(COL_CYAN + self.debug_text + COL_RESET)
        self.add_log(self.debug_text)


    def info(self, text="Info text wasn't added!"):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = self.format_filename(caller_frame.f_code.co_filename)

        spaces_count = self.MAX_SPACES - len(filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        self.info_text = f"[INFO]  [{self.get_time()}] [{filename}]{spaces} {self.format_line(text)}"

        print(COL_GREEN + self.info_text + COL_RESET)
        self.add_log(self.info_text)


    def warning(self, text="Warning text wasn't added!"):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = caller_frame.f_code.co_filename
        short_filename = filename.replace("\\", "/").split("/")[-1]

        spaces_count = self.MAX_SPACES - len(short_filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        self.warning_text = f"[WARN]  [{self.get_time()}] [{short_filename}]{spaces} {text}"

        print(COL_YELLOW + self.warning_text + COL_RESET)
        self.add_log(self.warning_text)


    def error(self, text="Error text wasn't added!", adding_text=True):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = caller_frame.f_code.co_filename
        short_filename = filename.replace("\\", "/").split("/")[-1]

        spaces_count = self.MAX_SPACES - len(short_filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        self.error_text = f"[ERROR] [{self.get_time()}] [{short_filename}]{spaces} {text}"

        if adding_text:
            print(COL_RED + self.error_text + COL_RESET)
            self.add_log(self.error_text)
        else:
            print(COL_RED + text + COL_RESET)
            self.add_log(text)


    def error_collector(self, exc_type, exc_value, exc_traceback):

        error_messages = []
        current_time = self.get_time()

        for tb in traceback.extract_tb(exc_traceback):
            filename = os.path.relpath(tb.filename, start=os.getcwd())
            line_number = tb.lineno
            short_filename = filename.replace("\\", "/").split("/")[-1]

            spaces_count = self.MAX_SPACES - len(filename)
            spaces = ""
            for i in range(spaces_count):
                spaces = spaces + " "

            error_message = f"[ERROR] [{current_time}] [{short_filename}] in line {line_number}"
            error_messages.append(error_message)

        final_message = f"{exc_type.__name__}: {exc_value}"
        error_messages.append(final_message)

        full_message = "\n".join(error_messages)
        self.error(full_message, False)

log = Logs(collecting_errors=True)
