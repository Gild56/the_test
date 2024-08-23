import json

from libraries.resource_path import resource_path
from libraries.logger import log

class PointsManager:
    def __init__(self):
        self.JSON_PATH = resource_path('json/save.json')
        self.WINNING_POINTS = 7
        self.MAX_WINNING_WIN_STREAK_POINTS = 5
        self.WINNING_WIN_STREAK_POINTS = 1
        self.LOSING_POINTS = 10

        self.points = 0
        self.win_streak = 0
        self.best_win_streak = 0

        self._import_data()

    def _save(self):
        with open(self.JSON_PATH, 'w') as f:
            json.dump({
                'points': self.points,
                'win_streak': self.win_streak,
                'best_win_streak': self.best_win_streak
            }, f)
        log.info("Data has been saved in the points.json file.")

    def _import_data(self):
        with open(self.JSON_PATH, 'r') as f:
            data = json.load(f)
            self.points = data.get('points', 0)
            self.win_streak = data.get('win_streak', 0)
            self.best_win_streak = data.get('best_win_streak', 0)
        log.info("Data has been imported from the points.json file.")

    def clear(self):
        self.points, self.win_streak, self.best_win_streak = 0, 0, 0
        self._save()

    def win(self):
        self.points += self.WINNING_POINTS

        if self.win_streak < self.MAX_WINNING_WIN_STREAK_POINTS:
            self.points += self.win_streak * self.WINNING_WIN_STREAK_POINTS
        else:
            self.points += self.WINNING_WIN_STREAK_POINTS * self.MAX_WINNING_WIN_STREAK_POINTS

        self.win_streak += 1

        if self.win_streak > self.best_win_streak:
            self.best_win_streak = self.win_streak

        self._save()

    def lose(self):
        self.win_streak = 0
        self.points -= self.LOSING_POINTS

        if self.points < 0:
            self.points = 0

        self._save()

points_manager = PointsManager()