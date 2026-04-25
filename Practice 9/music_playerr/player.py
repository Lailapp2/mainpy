import pygame

class Player:
    def __init__(self, songs):
        # ЭТА СТРОЧКА ОБЯЗАТЕЛЬНА:
        self.songs = songs 
        self.current_track = 0
        pygame.mixer.init()

    def play(self):
        pygame.mixer.music.load(self.songs[self.current_track])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.current_track = (self.current_track + 1) % len(self.songs)
        self.play()

    def prev(self):
        self.current_track = (self.current_track - 1) % len(self.songs)
        self.play()