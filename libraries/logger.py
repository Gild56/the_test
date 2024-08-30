import sys, os, time, traceback, inspect, logging
from kivy.logger import Logger

from libraries.colors import *
from libraries.resource_path import resource_path

class Logs:

    def __init__(self, collecting_errors=True):
        self.LOGS_FILE = resource_path("info.log")
        self.info_text = ""
        self.warning_text = ""
        self.error_text = ""
        self.MAX_SPACES = 25
        self.MAX_SPACES2 = 5
        self.MAX_LINE_LENGTH = 80
        self.info("The app is starting...")

        self.project_root = os.path.dirname(
            os.path.abspath(__file__)
        )

        if not os.path.exists(resource_path("crashes/")):
            os.makedirs(resource_path("crashes/"))

        if collecting_errors:
            sys.excepthook = self.error_collector
            Logger.setLevel(logging.CRITICAL)


    def get_time(self):
        current_time = time.localtime()
        return time.strftime("%H:%M:%S", current_time)


    def get_date(self, style="text"):
        today = time.localtime()
        if style == "text":
            date = time.strftime("%d %B", today).lower()
        else:
            date = time.strftime("%d-%m-%Y", today)

        return date


    def add_log(self, text):
        with open(self.LOGS_FILE, "a", encoding="utf8") as f:
            f.write(text + "\n")


    def format_filename(self, filename):
        rel_path = os.path.relpath(
            filename, os.path.abspath(os.path.dirname(__file__))
        )

        return rel_path


    def warn(self, text):
        self.warning(text)


    def format_line(self, text):
        if len(text) > self.MAX_LINE_LENGTH:
            return str(text[:self.MAX_LINE_LENGTH]) + '...'
        return text


    def get_crashlog_filename(self):
        current_time = time.localtime()
        current_time = time.strftime("%H-%M-%S", current_time)
        crashlog_name = (
            f"crashes/crashlog_{self.get_date("numbers")}"
            f"_{current_time}.log"
        )
        while True:
            if not os.path.exists(crashlog_name):
                return crashlog_name
            crashlog_name += " (copy)"


    def debug(self, text="Debug text wasn't added!"):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = caller_frame.f_code.co_filename
        short_filename = filename.replace("\\", "/").split("/")[-1]

        spaces_count = self.MAX_SPACES - len(short_filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        self.debug_text = (
            f"[DEBUG] [{self.get_time()}] "
            f"[{short_filename}]{spaces} {self.format_line(text)}"
        )

        print(COL_BLUE + self.debug_text + COL_RESET)
        self.add_log(self.debug_text)


    def info(self, text="Info text wasn't added!"):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = caller_frame.f_code.co_filename
        short_filename = filename.replace("\\", "/").split("/")[-1]

        spaces_count = self.MAX_SPACES - len(short_filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        self.info_text = (
            f"[INFO]  [{self.get_time()}] "
            f"[{short_filename}]{spaces} {self.format_line(text)}"
        )

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

        self.warning_text = (
            f"[WARN]  [{self.get_time()}] "
            f"[{short_filename}]{spaces} {text}"
        )

        print(COL_YELLOW + self.warning_text + COL_RESET)
        self.add_log(self.warning_text)


    def error(self, text="Error text wasn't added!", critical=False):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        filename = caller_frame.f_code.co_filename
        short_filename = filename.replace("\\", "/").split("/")[-1]

        spaces_count = self.MAX_SPACES - len(short_filename)
        spaces = ""
        for i in range(spaces_count):
            spaces = spaces + " "

        if critical:
            self.error_text = (
                f"[ERROR] [{self.get_time()}] "
                f"[CRITICAL]{spaces} {text}"
            )
        else:
            self.error_text = (
                f"[ERROR] [{self.get_time()}] "
                f"[{short_filename}]{spaces} {text}"
            )

        print(COL_RED + self.error_text + COL_RESET)
        self.add_log(self.error_text)


    def crash(self, text):
        print("\n" + COL_RED + text + COL_RESET)

        self.crashlog_filename = self.get_crashlog_filename()

        with open(self.crashlog_filename, "a", encoding="utf8") as f:
            f.write(text)


    def error_collector(self, exc_type, exc_value, exc_traceback):
        error_messages = []
        current_time = self.get_time()

        error_messages.append(
            f"A crash happened on [{self.get_date()}] "
            f"at [{current_time}]."
        )

        crash_message_lines = \
            len(traceback.extract_tb(exc_traceback))

        for times, tb in enumerate(
            traceback.extract_tb(exc_traceback)
        ):
            filename = os.path.relpath(
                tb.filename, start=os.getcwd()
            )

            short_filename = filename.replace(
                "\\", "/"
                ).split("/")[-1]

            line_number = tb.lineno

            with open(tb.filename, 'r') as f:
                lines = f.readlines()
                the_line = lines[line_number - 1].strip()

            spaces_count = (
                self.MAX_SPACES - len(short_filename)
            )

            spaces = ' ' * spaces_count

            line_number = str(line_number)

            if len(line_number) < 5:
                spaces_count = (
                    self.MAX_SPACES2 - len(line_number)
                )
            else:
                spaces_count = 4

            spaces2 = ' ' * spaces_count

            if times == 0:
                i = "I"
            else:
                i = "i"

            if times == crash_message_lines - 1:
                punctuation = "."
            else:
                punctuation = ","

            error_message = (
                f"{i}n [{short_filename}]{spaces} in line "
                f"{line_number}:{spaces2} "
                f"[ {the_line} ]{punctuation}"
            )
            error_messages.append(error_message)

        final_message = (
            'The error is called '
            f'"{exc_type.__name__}": {exc_value}.'
        )
        error_messages.append(final_message)

        full_message = "\n".join(error_messages)

        self.error(
            f'"{exc_type.__name__}": '
            f'"{exc_value}.',
            critical=True
        )

        self.crash(full_message)

log = Logs(collecting_errors=True)
