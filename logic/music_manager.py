import pygame
import os
from random import shuffle

from libraries.resource_path import resource_path
from libraries.logger import log

class MusicManager:
    def __init__(self):
        pygame.mixer.init()
        self.songs_list = os.listdir(resource_path("music"))
        self.remaining_songs = []
        self.current_song = None
        self.transition = pygame.mixer.Sound(resource_path("sounds/transition.mp3"))
        self.transition.set_volume(0.25)
        self.button_clicked = pygame.mixer.Sound(resource_path("sounds/8bit-click.wav"))
        self.button_clicked.set_volume(0.25)

        self.randomize_song()

    def randomize_song(self):
        if len(self.remaining_songs) == 0:
            self.remaining_songs = self.songs_list
            shuffle(self.remaining_songs)
            log.info("Randomizing the playlist.")

        song_file = self.remaining_songs.pop()
        self.current_song, _ = os.path.splitext(song_file)

    def play_music(self):
        self.randomize_song()
        song_path = resource_path(f"music/{self.current_song}.mp3")
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        log.info(f'Playing next song - "{self.current_song}".')

    def check_music(self):
        if not pygame.mixer.music.get_busy():
            self.play_music()

    def next_song(self):
        pygame.mixer.music.stop()
        self.play_music()

music_manager = MusicManager()
