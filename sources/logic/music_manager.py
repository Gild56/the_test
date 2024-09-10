import os
from random import shuffle

from kivy.core.audio import SoundLoader

from sources.libraries.resource_path import resource_path
from sources.libraries.logger import log

class MusicManager:
    def __init__(self):
        self.remaining_songs = []
        self.current_song = None
        self.current_music = None

        self.songs_list = os.listdir(
            resource_path("resources/music")
        )

        self.transition = SoundLoader.load(
            resource_path("resources/sounds/transition.mp3")
        )
        self.button_clicked = SoundLoader.load(
            resource_path("resources/sounds/8bit-click.wav")
        )
        self.win = SoundLoader.load(
            resource_path("resources/sounds/win.mp3")
        )
        self.lose = SoundLoader.load(
            resource_path("resources/sounds/lose.wav")
        )

        self.randomize_song()
        self.play_music()

    def randomize_song(self):
        if len(self.remaining_songs) == 0:
            self.remaining_songs = self.songs_list.copy()
            shuffle(self.remaining_songs)
            log.info("Randomizing the playlist.")

        song_file = self.remaining_songs.pop()
        self.current_song, _ = os.path.splitext(song_file)

    def play_music(self):
        if self.current_music:
            self.current_music.stop()

        self.randomize_song()
        song_path = resource_path(f"resources/music/{self.current_song}.mp3")
        self.current_music = SoundLoader.load(song_path)

        if self.current_music:
            self.current_music.play()
            log.info(f'Playing next song - "{self.current_song}".')

    def check_music(self):
        if self.current_music and not self.current_music.state == 'play':
            self.play_music()

    def next_song(self):
        if self.current_music:
            self.current_music.stop()
        self.play_music()

music_manager = MusicManager()
