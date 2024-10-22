import os, json

from sources.libraries.resource_path import resource_path
from sources.libraries.logger import log

class PointsManager:
    def __init__(self):
        self.WINNING_POINTS = 7
        self.MAX_WINNING_WIN_STREAK_POINTS = 5
        self.WINNING_WIN_STREAK_POINTS = 1
        self.LOSING_POINTS = 10

        self.points = 0
        self.win_streak = 0
        self.best_win_streak = 0

        if not os.path.exists(resource_path("sources/json/")):
            os.makedirs(resource_path("sources/json/"))
            log.info(
                "The sources/json/ folder does not exist. "
                "A new sources/json/ folder was created"
            )

        self.JSON_PATH = resource_path('sources/json/points.json')

        if not os.path.exists(self.JSON_PATH):
            log.info(
                "the sources/json/points.json file does not exist. "
                "The new one was created."
            )
            with open(self.JSON_PATH, 'w') as f:
                json.dump({
                    'points': 0,
                    'win_streak': 0,
                    'best_win_streak': 0
                }, f)

        try:
            self._import_data()
        except:
            log.info(
                "The sources/json/points.json format isn't the required "
                "one. The sources/json/options.json file was reset."
            )

    def save(self):
        with open(self.JSON_PATH, 'w') as f:
            json.dump({
                'points': self.points,
                'win_streak': self.win_streak,
                'best_win_streak': self.best_win_streak
            }, f)
        log.info("Data has been saved in the points.json file.")

    def _import_data(self):
        if os.path.getsize(self.JSON_PATH) == 0:
            with open(self.JSON_PATH, 'w') as f:
                json.dump({
                    'points': 0,
                    'win_streak': 0,
                    'best_win_streak': 0
                }, f)

        with open(self.JSON_PATH, 'r') as f:
            data = json.load(f)
            self.points = data.get('points', 0)
            self.win_streak = data.get('win_streak', 0)
            self.best_win_streak = data.get('best_win_streak', 0)
        log.info("Data has been imported from the points.json file.")

    def clear(self):
        self.points, self.win_streak, self.best_win_streak = 0, 0, 0
        log.info("The stats were succesfully cleared.")
        self.save()

    def win(self):
        self.points += self.WINNING_POINTS

        if self.win_streak < \
            self.MAX_WINNING_WIN_STREAK_POINTS:

            self.points += (
                self.win_streak * \
                    self.WINNING_WIN_STREAK_POINTS
                )
        else:
            self.points += (
                self.WINNING_WIN_STREAK_POINTS * \
                    self.MAX_WINNING_WIN_STREAK_POINTS
            )

        self.win_streak += 1

        if self.win_streak > self.best_win_streak:
            self.best_win_streak = self.win_streak

        self.save()

    def lose(self):
        self.win_streak = 0
        self.points -= self.LOSING_POINTS

        if self.points < 0:
            self.points = 0

        self.save()

points_manager = PointsManager()
